#!/usr/bin/env python3
import scipy
from collections import defaultdict
from automata import reg2min_dfa
from chomsky import eps
from chomsky import is_term
from chomsky import parse_grammar
from chomsky import print_grammar
from chomsky import to_weak_CNF
from cyk import parse_graph
from cyk import print_res


def parse_ext_grammar(filename):
    prods = []
    with open(filename) as file:
        for line in file.readlines():
            lst = line.split()[1:]
            prods.append((line.split()[0], " ".join(lst)))

    return prods


def print_res_tensor(start, matrix_automata, matrix_graph, m, n, filename):
    ans = [[[] for _ in range(m + 1)] for _ in range(m + 1)]

    for symb in matrix_automata.keys():
        for i in range(m):
            for j in range(m):
                if matrix_automata[symb][i, j]:
                    ans[i][j].append(str(symb.value))

    with open(filename, "w") as file:
        for i in range(m):
            for j in range(m):
                if ans[i][j]:
                    ans[i][j].sort()
                    file.write("[" + ", ".join(ans[i][j]) + "] ")
                else:
                    file.write(". ")
            file.write("\n")

        for i in range(n):
            for j in range(n):
                if matrix_graph[start][i, j]:
                    file.write(str(i) + " " + str(j) + "\n")


def matrix_alg(prods, graph):
    dict = defaultdict(list)
    nonterms = set()

    for prod in prods:
        if (len(prod[1]) == 1) and is_term(prod[1][0]):
            dict[prod[1][0]].append(prod[0])
        nonterms.add(prod[0])

    vert = set()
    for v, _, u in graph:
        vert.add(v)
        vert.add(u)

    n = len(vert)
    rows = defaultdict(list)
    cols = defaultdict(list)
    data = defaultdict(list)

    for v, symb, u in graph:
        for x in dict[symb]:
            rows[x].append(v)
            cols[x].append(u)
            data[x].append(True)

    for i in range(n):
        for x in dict[eps]:
            rows[x].append(i)
            cols[x].append(i)
            data[x].append(True)

    res = defaultdict()
    for nonterm in nonterms:
        res[nonterm] = scipy.sparse.csr_matrix((data[nonterm], (rows[nonterm], cols[nonterm])), shape=(n, n), dtype=bool)

    change = True
    while change:
        change = False
        for prod in prods:
            if len(prod[1]) == 2 and not is_term(prod[1][0]) and not is_term(prod[1][1]):
                a = prod[0]
                b = prod[1][0]
                c = prod[1][1]
                if (res[a] != res[a] + res[b] * res[c]).count_nonzero() > 0:
                    change = True
                    res[a] = res[a] + res[b] * res[c]

    ans = []
    for symb in res.keys():
        for i in range(n):
            for j in range(n):
                if res[symb][i, j]:
                    ans.append((symb, i, j))

    return ans


def build_automata(prods):
    start_set = defaultdict(str)
    final_set = defaultdict(str)
    nodes = defaultdict()
    nonterms = set()
    eps_nonterms = set()
    edges = []
    cnt = 0
    sz = 0
    for prod in prods:
        automata = reg2min_dfa(prod[1])
        nonterm = prod[0]
        nonterms.add(nonterm)
        dict = automata.to_dict()
        state_values = set()
        for u in dict.keys():
            state_values.add(u.value)
            for symb in dict[u].keys():
                v = dict[u][symb]
                state_values.add(v.value)
        lst = sorted(list(state_values))
        for value in lst:
            nodes[value, cnt] = sz
            sz += 1
        for u in dict.keys():
            for symb in dict[u].keys():
                if symb.value == eps:
                    continue
                v = dict[u][symb]
                edges.append((nodes[(u.value, cnt)], symb, nodes[(v.value, cnt)]))
        if eps in prod[1] or automata.start_state in automata.final_states:
            eps_nonterms.add(nonterm)
        start_set[nodes[(automata.start_state.value, cnt)]] = nonterm
        for state in list(automata.final_states):
            final_set[nodes[(state.value, cnt)]] = nonterm
        cnt += 1

    matrix_automata = defaultdict()
    rows = defaultdict(list)
    cols = defaultdict(list)
    data = defaultdict(list)

    for u, symb, v in edges:
        rows[symb].append(u)
        cols[symb].append(v)
        data[symb].append(True)

    for symb in data.keys():
        matrix_automata[symb] = scipy.sparse.csr_matrix((data[symb], (rows[symb], cols[symb])), shape=(sz, sz), dtype=bool)

    start_lst = ["" for _ in range(sz + 1)]
    final_lst = ["" for _ in range(sz + 1)]

    for num, nonterm in start_set.items():
        start_lst[num] = nonterm

    for num, nonterm in final_set.items():
        final_lst[num] = nonterm

    return matrix_automata, start_lst, final_lst, edges, eps_nonterms, nonterms, sz


def tensor_alg(prods, graph):
    matrix_automata, start_set, final_set, edges, eps_nonterms, nonterms, m = build_automata(prods)

    vert = set()
    for v, _, u in graph:
        vert.add(v)
        vert.add(u)

    n = len(vert)
    rows = defaultdict(list)
    cols = defaultdict(list)
    data = defaultdict(list)

    for v, symb, u in graph:
        rows[symb].append(v)
        cols[symb].append(u)
        data[symb].append(True)

    for i in range(n):
        for nonterm in eps_nonterms:
            rows[nonterm].append(i)
            cols[nonterm].append(i)
            data[nonterm].append(True)

    matrix_graph = defaultdict()
    symbols = matrix_automata.keys() | data.keys() | nonterms
    for symb in symbols:
        matrix_graph[symb] = scipy.sparse.csr_matrix((data[symb], (rows[symb], cols[symb])), shape=(n, n), dtype=bool)

    symbols_ = matrix_automata.keys() & matrix_graph.keys()
    change = True
    k = m * n
    while change:
        change = False
        matrix_prod = scipy.sparse.csr_matrix((k, k), dtype=bool)
        for symb in symbols_:
            matrix_prod += scipy.sparse.kron(matrix_automata[symb], matrix_graph[symb])
        pow = k - 1
        while pow:
            pow //= 2
            matrix_prod += matrix_prod * matrix_prod
        r_nnz, c_nnz = matrix_prod.nonzero()
        for i, j in zip(r_nnz, c_nnz):
            if matrix_prod[i, j]:
                s = i // n
                f = j // n
                if start_set[s] != "" and final_set[f] != "":
                    x = i % n
                    y = j % n
                    if start_set[s] == final_set[f]:
                        if matrix_graph[start_set[s]][x, y] == False:
                            change = True
                            matrix_graph[start_set[s]][x, y] = True

    return matrix_automata, matrix_graph, m, n


def solve_matrix_alg(filename_grammar, filename_graph, filename_res):
    prods = to_weak_CNF(parse_grammar(filename_grammar))
    res = matrix_alg(prods, parse_graph(filename_graph))
    print_grammar(prods, filename_res)
    print_res("S", res, filename_res)


def solve_tensor_alg(filename_grammar, filename_graph, filename_res):
    matrix_automata, matrix_graph, m, n = tensor_alg(parse_ext_grammar(filename_grammar), parse_graph(filename_graph))
    print_res_tensor("S", matrix_automata, matrix_graph, m, n, filename_res)
