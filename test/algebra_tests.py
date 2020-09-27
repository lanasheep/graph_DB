#!/usr/bin/env python3
import pytest
import os

from chomsky import to_weak_CNF
from algebra import matrix_alg
from algebra import solve_tensor_alg
from algebra import solve_matrix_alg


def test_matrix1():
    prods = [("S", ["eps"]), ("S", ["a"])]
    graph = [(0, "b", 1), (1, "b", 0)]
    res = matrix_alg(to_weak_CNF(prods), graph)

    assert len(res) == 2
    assert ("S", 0, 0) in res
    assert ("S", 1, 1) in res


def test_matrix2():
    prods = [("S", ["A", "B"]), ("S", ["A", "S1"]), ("S1", ["S", "B"]), ("A", ["a"]), ("B", ["b"])]
    graph = [(0, "a", 1), (1, "a", 2), (2, "b", 3), (3, "b", 2)]
    res = matrix_alg(to_weak_CNF(prods), graph)

    assert len(res) == 8
    assert ("A", 0, 1) in res
    assert ("A", 1, 2) in res
    assert ("B", 2, 3) in res
    assert ("B", 3, 2) in res
    assert ("S", 1, 3) in res
    assert ("S1", 1, 2) in res
    assert ("S", 0, 2) in res
    assert ("S1", 0, 3) in res


def test_matrix3():
    prods = [("S", ["A", "B"]), ("A", ["a"]), ("A", ["eps"]), ("B", ["b"]), ("B", ["eps"])]
    graph = [(0, "a", 1), (1, "b", 2)]
    res = matrix_alg(to_weak_CNF(prods), graph)

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


def test_matrix4():
    prods = [("S", ["A", "B", "C"]), ("A", ["a"]), ("A", ["eps"]), ("B", ["b"]), ("C", ["c"])]
    graph = [(0, "a", 1), (1, "b", 2), (2, "c", 0)]
    res = matrix_alg(to_weak_CNF(prods), graph)

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


def test_matrix5():
    prods = [("S", ["A", "B"]), ("A", ["a"]), ("S", ["A", "S1"]), ("S1", ["S", "B"]), ("B", ["b"])]
    graph = [(0, "a", 1), (1, "a", 2), (2, "a", 0), (0, "b", 3), (3, "b", 0)]
    res = matrix_alg(to_weak_CNF(prods), graph)

    assert len(res) == 17
    assert ("S", 0, 0) in res
    assert ("S1", 0, 0) in res
    assert ("A", 0, 1) in res
    assert ("B", 0, 3) in res
    assert ("S", 0, 3) in res
    assert ("S1", 0, 3) in res
    assert ("S", 1, 0) in res
    assert ("S1", 1, 0) in res
    assert ("A", 1, 2) in res
    assert ("S1", 1, 3) in res
    assert ("S", 1, 3) in res
    assert ("S", 2, 0) in res
    assert ("S1", 2, 0) in res
    assert ("A", 2, 0) in res
    assert ("S", 2, 3) in res
    assert ("S1", 2, 3) in res
    assert ("B", 3, 0) in res


def test_solve_tensor1(tmp_path):
    file_grammar = tmp_path / "grammar.txt"
    file_graph = tmp_path / "graph.txt"
    file_res = tmp_path / "res.txt"
    file_grammar.write_text("S a | eps")
    file_graph.write_text("0 b 1\n1 b 0")
    solve_tensor_alg(file_grammar, file_graph, file_res)
    assert open(os.path.normpath(file_res), "r").read() == \
". [a] \n\
. . \n\
0 0\n\
1 1\n"


def test_solve_tensor2(tmp_path):
    file_grammar = tmp_path / "grammar.txt"
    file_graph = tmp_path / "graph.txt"
    file_res = tmp_path / "res.txt"
    file_grammar.write_text("S a b | a")
    file_graph.write_text("0 b 1\n1 a 0")
    solve_tensor_alg(file_grammar, file_graph, file_res)
    assert open(os.path.normpath(file_res), "r").read() == \
". . [a] \n\
. . . \n\
. [b] . \n\
1 0\n\
1 1\n"


def test_solve_tensor3(tmp_path):
    file_grammar = tmp_path / "grammar.txt"
    file_graph = tmp_path / "graph.txt"
    file_res = tmp_path / "res.txt"
    file_grammar.write_text("S A B | A S1\nS1 S B\nA a\nB b")
    file_graph.write_text("0 a 1\n1 a 2\n2 b 3\n3 b 2")
    solve_tensor_alg(file_grammar, file_graph, file_res)
    assert open(os.path.normpath(file_res), "r").read() == \
". . [A] . . . . . . . \n\
. . . . . . . . . . \n\
. [B, S1] . . . . . . . . \n\
. . . . . [S] . . . . \n\
. . . . . . . . . . \n\
. . . . [B] . . . . . \n\
. . . . . . . [a] . . \n\
. . . . . . . . . . \n\
. . . . . . . . . [b] \n\
. . . . . . . . . . \n\
0 2\n\
1 3\n"


def test_solve_tensor4(tmp_path):
    file_grammar = tmp_path / "grammar.txt"
    file_graph = tmp_path / "graph.txt"
    file_res = tmp_path / "res.txt"
    file_grammar.write_text("S (a S b)* | eps")
    file_graph.write_text("0 a 1\n1 a 2\n2 b 3\n3 b 4")
    solve_tensor_alg(file_grammar, file_graph, file_res)
    assert open(os.path.normpath(file_res), "r").read() == \
". . . [a] . \n\
. . . . . \n\
. . . [a] . \n\
. . . . [S] \n\
. . [b] . . \n\
0 0\n\
0 4\n\
1 1\n\
1 3\n\
2 2\n\
3 3\n\
4 4\n"


def test_solve_tensor5(tmp_path):
    file_grammar = tmp_path / "grammar.txt"
    file_graph = tmp_path / "graph.txt"
    file_res = tmp_path / "res.txt"
    file_grammar.write_text("S (a S1)* (b S1)*\nS1 c | d | eps")
    file_graph.write_text("0 a 1\n1 c 2\n2 b 3\n3 d 0")
    solve_tensor_alg(file_grammar, file_graph, file_res)
    assert open(os.path.normpath(file_res), "r").read() == \
". [b] . [a] . . \n\
. . [S1] . . . \n\
. [b] . . . . \n\
[S1] . . . . . \n\
. . . . . [c, d] \n\
. . . . . . \n\
0 0\n\
0 1\n\
0 2\n\
0 3\n\
2 0\n\
2 3\n"


def test_m():
    solve_matrix_alg("grammar4.txt", "graph.txt", "res.txt")


def test_t():
    solve_tensor_alg("grammar1.txt", "graph.txt", "res.txt")
