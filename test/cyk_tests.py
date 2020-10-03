#!/usr/bin/env python3
import pytest
import os
from cyk import parse_word
from cyk import parse_graph
from cyk import print_res
from cyk import CYK
from cyk import Hellings
from chomsky import to_CNF
from chomsky import to_weak_CNF


def test_parse_word(tmp_path):
    tmp_file = tmp_path / "file.txt"
    tmp_file.write_text("aaabb")
    word = parse_word(os.path.normpath(tmp_file))

    assert word == "aaabb"


def test_parse_graph(tmp_path):
    tmp_file = tmp_path / "file.txt"
    tmp_file.write_text("0 a 1\n1 b 2")
    graph = parse_graph(os.path.normpath(tmp_file))

    assert len(graph) == 2
    assert (0, "a", 1) in graph
    assert (1, "b", 2) in graph


def test_print_res(tmp_path):
    tmp_file = tmp_path / "file.txt"
    res = [("A", 0, 1), ("A", 2, 2), ("S", 2, 1), ("S", 0, 2), ("B", 0, 2)]
    print_res("S", res, tmp_file)

    assert open(os.path.normpath(tmp_file), "r").read() == "2 1\n0 2\n"


def test_CYK1():
    prods = [("S", ["a", "S", "b", "S"]), ("S", ["eps"])]
    start, prods = to_CNF(prods)

    assert CYK(start, prods, "aabaabbb")
    assert CYK(start, prods, "")
    assert not CYK(start, prods, "aabaaabbb")
    assert not CYK(start, prods, "accb")


def test_CYK2():
    prods = [("S", ["a", "S"]), ("S", ["b", "S"]), ("S", ["S", "a"]), ("S", ["S", "b"]), ("S", ["eps"])]
    start, prods = to_CNF(prods)

    assert CYK(start, prods, "a")
    assert CYK(start, prods, "b")
    assert CYK(start, prods, "")
    assert CYK(start, prods, "bbbaaaaa")
    assert not CYK(start, prods, "c")


def test_CYK3():
    prods = [("S", ["A", "B", "C"]), ("A", ["a", "A"]), ("A", ["eps"]),
             ("B", ["b", "B"]), ("B", ["eps"]), ("C", ["c", "C"]), ("C", ["eps"])]
    start, prods = to_CNF(prods)

    assert CYK(start, prods, "abc")
    assert CYK(start, prods, "")
    assert CYK(start, prods, "aabbbbccccc")
    assert CYK(start, prods, "aaac")
    assert not CYK(start, prods, "ba")
    assert not CYK(start, prods, "acb")


def test_Hellings1():
    prods = [("S", ["eps"]), ("S", ["a"])]
    graph = [(0, "b", 1), (1, "b", 0)]
    res = Hellings(to_weak_CNF(prods), graph)

    assert len(res) == 2
    assert ("S", 0, 0) in res
    assert ("S", 1, 1) in res


def test_Hellings2():
    prods = [("S", ["A", "B"]), ("S", ["A", "S1"]), ("S1", ["S", "B"]), ("A", ["a"]), ("B", ["b"])]
    graph = [(0, "a", 1), (1, "a", 2), (2, "b", 3), (3, "b", 2)]
    res = Hellings(to_weak_CNF(prods), graph)

    assert len(res) == 8
    assert ("A", 0, 1) in res
    assert ("A", 1, 2) in res
    assert ("B", 2, 3) in res
    assert ("B", 3, 2) in res
    assert ("S", 1, 3) in res
    assert ("S1", 1, 2) in res
    assert ("S", 0, 2) in res
    assert ("S1", 0, 3) in res


def test_Hellings3():
    prods = [("S", ["A", "B"]), ("A", ["a"]), ("A", ["eps"]), ("B", ["b"]), ("B", ["eps"])]
    graph = [(0, "a", 1), (1, "b", 2)]
    res = Hellings(to_weak_CNF(prods), graph)

    assert len(res) == 14
    assert ("A", 0, 0) in res
    assert ("B", 0, 0) in res
    assert ("S", 0, 0) in res
    assert ("A", 1, 1) in res
    assert ("B", 1, 1) in res
    assert ("S", 1, 1) in res
    assert ("A", 2, 2) in res
    assert ("B", 2, 2) in res
    assert ("S", 2, 2) in res
    assert ("S", 0, 2) in res
    assert ("S", 0, 1) in res
    assert ("S", 1, 2) in res
    assert ("A", 0, 1) in res
    assert ("B", 1, 2) in res


def test_Hellings4():
    prods = [("S", ["A", "B", "C"]), ("A", ["a"]), ("A", ["eps"]), ("B", ["b"]), ("C", ["c"])]
    graph = [(0, "a", 1), (1, "b", 2), (2, "c", 0)]
    res = Hellings(to_weak_CNF(prods), graph)

    assert len(res) == 9
    assert ("A", 0, 1) in res
    assert ("B", 1, 2) in res
    assert ("C", 2, 0) in res
    assert ("A", 0, 0) in res
    assert ("A", 1, 1) in res
    assert ("A", 2, 2) in res
    assert ("S", 1, 0) in res
    assert ("S", 0, 0) in res
    assert ("A0", 1, 0) in res


