#!/usr/bin/env python3
from collections import defaultdict
from queue import Queue

eps = "eps"


def is_term(symbol):
    return symbol[0].islower()


def parse_grammar(filename):
    prods = []
    with open(filename) as file:
        for line in file.readlines():
            prods.append((line[0], line.split()[1:]))

    return prods


def print_grammar(prods, filename):
    with open(filename, "w") as file:
        for prod in prods:
            file.write(prod[0] + " " + " ".join(prod[1]) + "\n")


def add_new_start(start, prods):
    nonterms = set()
    for prod in prods:
        nonterms.add(prod[0])
        for symb in prod[1]:
            if not is_term(symb):
                nonterms.add(symb)
                
    cnt = 0
    find = False

    while not find:
        if not (start + str(cnt)) in nonterms:
            find = True
        else:
            cnt += 1

    prods.append((start + str(cnt), [start]))
    prods.append((start + str(cnt), [eps]))
    start = start + str(cnt)

    return start, prods


def delete_long_prods(prods):
    nonterms = set()
    for prod in prods:
        nonterms.add(prod[0])
        for symb in prod[1]:
            if not is_term(symb):
                nonterms.add(symb)

    new_prods = []
    cnt = 0
    for prod in prods:
        if (len(prod[1]) > 2):
            new_nonterms = []
            for i in range(len(prod[1]) - 1):
                num = 0
                find = False
                while not find:
                    if not ("A" + str(num)) in nonterms:
                        find = True
                    else:
                        num += 1
                new_nonterms.append("A" + str(num))
            nonterms |= set(new_nonterms)
            last = prod[0]
            for i, new_nonterm in enumerate(new_nonterms):
                if i + 2 < len(prod[1]):
                    new_prods.append((last, [prod[1][i], new_nonterms[i]]))
                    last = new_nonterm
                else:
                    new_prods.append((last, [prod[1][i], prod[1][i + 1]]))
            cnt += 1
        else:
            new_prods.append(prod)

    return new_prods


def delete_eps_prods(start, prods):
    new_prods = []
    eps_prod_nonterms = set()
    for prod in prods:
         if prod[1][0] == eps:
             eps_prod_nonterms.add(prod[0])
         else:
             new_prods.append(prod)

    last_len = 0

    while last_len != len(eps_prod_nonterms):
        last_len = len(eps_prod_nonterms)
        for prod in new_prods:
            if len([symb for symb in prod[1] if symb in eps_prod_nonterms]) == len(prod[1]):
                eps_prod_nonterms.add(prod[0])

    res_prods = []
    for prod in new_prods:
        for perm in range(1 << len(prod[1])):
            perm_list = [symb for i, symb in enumerate(prod[1]) if ((perm >> i) & 1) == True]
            if len([symb for symb in perm_list if symb in eps_prod_nonterms]) == len(perm_list) \
                    and len(perm_list) != len(prod[1]):
                res_prods.append((prod[0], [symb for i, symb in enumerate(prod[1]) if ((perm >> i) & 1) == False]))

    return add_new_start(start, res_prods)


def delete_chain_prods(prods):
    lists = defaultdict(list)
    for prod in prods:
        lists[prod[0]].append(prod[1])

    nonterms = set()
    for prod in prods:
        if not is_term(prod[0]):
            nonterms.add(prod[0])

    pairs = []
    for nonterm in nonterms:
        used = set()
        q = Queue()
        q.put(nonterm)
        used.add(nonterm)
        while q.empty() == False:
            cur_nonterm = q.get()
            for lst in lists[cur_nonterm]:
                if len(lst) == 1 and not is_term(lst[0]) and not lst[0] in used:
                    used.add(lst[0])
                    pairs.append((nonterm, lst[0]))
                    q.put(lst[0])

    new_prods = []
    for first, second in pairs:
        new_prods += [(first, lst) for lst in lists[second]]
    new_prods += [prod for prod in prods if not prod in new_prods]

    return [prod for prod in new_prods if not (len(prod[1]) == 1 and not is_term(prod[1][0]))]


def delete_useless_nonterm(start, prods):
    prof_nonterm = set()
    for prod in prods:
        for symb in prod[1]:
            if is_term(symb):
                prof_nonterm.add(symb)

    last_len = 0

    while last_len != len(prof_nonterm):
        last_len = len(prof_nonterm)
        for prod in prods:
            if len([symb for symb in prod[1] if symb in prof_nonterm]) == len(prod[1]):
                prof_nonterm.add(prod[0])

    new_prods = []
    for prod in prods:
        if (prod[0] in prof_nonterm) and len([symb for symb in prod[1] if symb in prof_nonterm]) == len(prod[1]):
            new_prods.append(prod)

    lists = defaultdict(list)
    for prod in new_prods:
        lists[prod[0]].append(prod[1])

    res_prods = []
    used = set()
    q = Queue()
    q.put(start)
    used.add(start)

    while q.empty() == False:
        nonterm = q.get()
        for lst in lists[nonterm]:
            res_prods.append((nonterm, lst))
            for element in lst:
                if not is_term(element) and not element in used:
                    used.add(element)
                    q.put(element)

    return res_prods


def delete_pair_term(prods):
    new_prods = []
    cnt = 0
    for prod in prods:
        if len(prod[1]) == 2 and (is_term(prod[1][0]) or is_term(prod[1][1])):
            if is_term(prod[1][0]) and is_term(prod[1][1]):
                new_nonterm1 = "N" + str(cnt) + "1"
                new_nonterm2 = "N" + str(cnt) + "2"
                new_prods.append((prod[0], [new_nonterm1, new_nonterm2]))
                new_prods.append((new_nonterm1, [prod[1][0]]))
                new_prods.append((new_nonterm2, [prod[1][1]]))
            else:
                if is_term(prod[1][0]):
                    new_nonterm1 = "N" + str(cnt) + "1"
                    new_prods.append((prod[0], [new_nonterm1, prod[1][1]]))
                    new_prods.append((new_nonterm1, [prod[1][0]]))
                else:
                    new_nonterm2 = "N" + str(cnt) + "2"
                    new_prods.append((prod[0], [prod[1][0], new_nonterm2]))
                    new_prods.append((new_nonterm2, [prod[1][1]]))
            cnt += 1
        else:
            new_prods.append(prod)

    return new_prods


def to_CNF(prods):
    start = "S"
    prods = delete_long_prods(prods)
    start, prods = delete_eps_prods(start, prods)
    prods = delete_chain_prods(prods)
    prods = delete_useless_nonterm(start, prods)
    prods = delete_pair_term(prods)

    return start, prods


def to_weak_CNF(prods):
    start = "S"
    prods = delete_long_prods(prods)
    prods = delete_chain_prods(prods)
    prods = delete_useless_nonterm(start, prods)
    prods = delete_pair_term(prods)

    return prods


def convert(filename_in, filename_out):
    print_grammar(to_CNF(parse_grammar(filename_in)), filename_out)
