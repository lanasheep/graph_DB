#!/usr/bin/env python3
from collections import defaultdict
from queue import Queue
from chomsky import is_term
from chomsky import parse_grammar
from chomsky import eps


def parse_word(filename):
    return open(filename).read()


def parse_graph(filename):
    graph = []
    with open(filename) as file:
        for line in file.readlines():
            graph.append((int(line.split()[0]), line.split()[1], int(line.split()[2])))

    return graph


def print_res(start, res, filename):
    with open(filename, "w") as file:
        for (nonterm, u, v) in res:
            if nonterm == start:
                file.write(str(u) + " " + str(v) + "\n")


def CYK(start, prods, word):
    dict = defaultdict(list)
    for prod in prods:
        if (len(prod[1]) == 1) and is_term(prod[1][0]):
            dict[prod[1][0]].append(prod[0])

    n = len(word)
    dp = [[[] for _ in range(n + 1)] for _ in range(n + 1)]

    for i, symb in enumerate(word):
        dp[i][i + 1] += dict[symb]

    if not n or (n == 1 and word[0] == ""):
        return start in dict[eps]

    for len_seg in range(2, n + 1):
        for prod in prods:
            if len(prod[1]) == 2 and not is_term(prod[1][0]) and not is_term(prod[1][1]):
                a = prod[1][0]
                b = prod[1][1]
                for left in range(n - len_seg + 1):
                    for mid in range(left + 1, left + len_seg):
                        if a in dp[left][mid] and b in dp[mid][left + len_seg]:
                            dp[left][left + len_seg].append(prod[0])

    return start in dp[0][n]


def Hellings(prods, graph):
    dict = defaultdict(list)
    res = []

    for prod in prods:
        if (len(prod[1]) == 1) and is_term(prod[1][0]):
            dict[prod[1][0]].append(prod[0])

    vert = set()
    for v, symb, u in graph:
        vert.add(v)
        vert.add(u)
        for x in dict[symb]:
            res.append((x, v, u))

    n = len(vert)
    for i in range(n):
        for x in dict[eps]:
            res.append((x, i, i))

    q = Queue()
    for element in res:
        q.put(element)

    filtered_prods = [prod for prod in prods if len(prod[1]) == 2 and \
                      (not is_term(prod[1][0])) and (not is_term(prod[1][1]))]

    while not q.empty():
        nonterm, u, v = q.get()
        for nonterm_, u_, v_ in res:
            if v == u_:
                for prod in filtered_prods:
                    if (prod[1][0] == nonterm) and (prod[1][1] == nonterm_) and ((prod[0], u, v_) not in res):
                        q.put((prod[0], u, v_))
                        res.append((prod[0], u, v_))
        for nonterm_, u_, v_ in res:
            if v_ == u:
                for prod in filtered_prods:
                    if (prod[1][0] == nonterm_) and (prod[1][1] == nonterm) and ((prod[0], u_, v) not in res):
                        q.put((prod[0], u_, v))
                        res.append((prod[0], u_, v))

    return res


def solve_CYK(filename_grammar, filename_word):
    if CYK(parse_grammar(filename_grammar), parse_word(filename_word)):
        print("YES")
    else:
        print("NO")


def solve_Hellings(filename_grammar, filename_graph, filename_res):
    res = Hellings(parse_grammar(filename_grammar), parse_graph(filename_graph))
    print_res("S", res, filename_res)

