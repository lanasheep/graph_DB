#!/usr/bin/env python3
import pytest
import os
from chomsky import is_term
from chomsky import parse_grammar
from chomsky import print_grammar
from chomsky import delete_long_prods
from chomsky import delete_eps_prods
from chomsky import delete_chain_prods
from chomsky import delete_useless_nonterm
from chomsky import delete_pair_term
from chomsky import to_CNF


def test_parse_grammar(tmp_path):
    tmp_file = tmp_path / "file.txt"
    tmp_file.write_text("S a S b S\nS eps")
    prods = parse_grammar(os.path.normpath(tmp_file))
    assert len(prods) == 2
    assert ("S", ["a", "S", "b", "S"]) in prods
    assert ("S", ["eps"]) in prods


def test_print_grammar(tmp_path):
    prods = [("S", ["A", "B"]), ("A", ["a"]), ("B", ["b"])]
    tmp_file = tmp_path / "file.txt"
    print_grammar(prods, os.path.normpath(tmp_file))
    assert open(os.path.normpath(tmp_file), "r").read() == "S A B\nA a\nB b\n"


def test_delete_long_prods():
    prods = [("S", ["A", "B", "C"]), ("A", ["B", "C", "C"]), ("A", ["a"]), ("B", ["b"]), ("C", ["c"])]
    res_prods = delete_long_prods(prods)

    assert not [prod for prod in res_prods if len(prod[1]) >= 3]


def test_delete_eps_prods():
    prods = [("S", ["A", "B"]), ("A", ["eps"]), ("A", ["a"]), ("B", ["eps"]), ("B", ["b"])]
    res_prods = delete_eps_prods(prods)

    assert len(res_prods) == 7
    assert ("S000", ["S"]) in res_prods
    assert ("S000", ["eps"]) in res_prods
    assert ("S", ["A"]) in res_prods
    assert ("S", ["B"]) in res_prods
    assert ("S", ["A", "B"]) in res_prods
    assert ("A", ["a"]) in res_prods
    assert ("B", ["b"]) in res_prods


def test_delete_chain_prods():
    prods = [("S", ["A"]), ("A", ["B"]), ("B", ["C"]), ("B", ["b"]), ("C", ["c"])]
    res_prods = delete_chain_prods(prods)

    assert len(res_prods) == 7
    assert ("S", ["b"]) in res_prods
    assert ("S", ["c"]) in res_prods
    assert ("A", ["b"]) in res_prods
    assert ("A", ["c"]) in res_prods
    assert ("B", ["b"]) in res_prods
    assert ("B", ["c"]) in res_prods
    assert ("C", ["c"]) in res_prods


def test_delete_useless_nonterm():
    prods = [("S", ["a"]), ("A", ["a"]), ("S", ["B"])]
    res_prods = delete_useless_nonterm("S", prods)

    assert len(res_prods) == 1
    assert ("S", ["a"]) in res_prods


def test_delete_pair_term():
    prods = [("S", ["a", "b"])]
    res_prods = delete_pair_term(prods)

    assert len(res_prods) == 3
    assert not [prod for prod in res_prods if len(prod[1]) == 2 and
                (is_term(prod[1][0]) or is_term(prod[1][1]))]


def test_to_CNF():
    prods = [("S", ["a", "S", "b"]), ("S", ["eps"])]
    res_prods = to_CNF(prods)

    assert len(res_prods) == 11
    assert ("S000", ["eps"]) in res_prods
    assert ("S000", ["N01", "N02"]) in res_prods
    assert ("N11", ["S"]) in res_prods
    assert ("N02", ["A00"]) in res_prods
    assert ("S", ["N21", "N22"]) in res_prods
    assert ("A00", ["N11", "N12"]) in res_prods
    assert ("N22", ["A00"]) in res_prods
    assert ("N01", ["a"]) in res_prods
    assert ("N21", ["a"]) in res_prods
    assert ("A00", ["b"]) in res_prods
    assert ("N12", ["b"]) in res_prods

