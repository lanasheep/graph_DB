#!/usr/bin/env python3
import pytest
import os
from antlr_parser import get_stream
from antlr_parser import parse
from MyGraphQueriesVisitor import MyGraphQueriesVisitor


def process(stream):
    tree = parse(stream)
    visitor = MyGraphQueriesVisitor()
    visitor.visit(tree)

    return visitor


def test_connect1(tmp_path):
    tmp_file = tmp_path / "file.txt"
    tmp_file.write_text("connect to [home/graph_db];")
    visitor = process(get_stream(True, os.path.normpath(tmp_file)))

    assert visitor.get_addr() == "home/graph_db"


def test_connect2(tmp_path):
    tmp_file = tmp_path / "file.txt"
    tmp_file.write_text("connect to [home/graph_db];\nconnect to [home/another_graph_db];")
    visitor = process(get_stream(True, os.path.normpath(tmp_file)))

    assert visitor.get_addr() == "home/another_graph_db"


def test_list(tmp_path, capsys):
    top_dir = tmp_path / "top_dir"
    top_dir.mkdir()
    file1 = top_dir / "graph1.txt"
    file2 = top_dir / "graph2.txt"
    file1.write_text("0 a 1\n1 b 2")
    file2.write_text("0 a 1\n1 a 0")
    file_in = tmp_path / "file.txt"
    file_in.write_text("connect to [" + os.path.normpath(top_dir) + "];\nlist;")
    process(get_stream(True, os.path.normpath(file_in)))
    out, err = capsys.readouterr()

    assert out == "0 a 1\n1 b 2\n\n0 a 1\n1 a 0\n\n"
    assert err == ""


def test_named_pattern1(tmp_path):
    tmp_file = tmp_path / "file.txt"
    tmp_file.write_text("S = a S b S;")
    visitor = process(get_stream(True, os.path.normpath(tmp_file)))
    prods = visitor.get_prods()

    assert len(prods) == 1
    assert ("S", ["a", "S", "b", "S"]) in prods


def test_named_pattern2(tmp_path):
    tmp_file = tmp_path / "file.txt"
    tmp_file.write_text("S = a S b S;\nS = c;")
    visitor = process(get_stream(True, os.path.normpath(tmp_file)))
    prods = visitor.get_prods()

    assert len(prods) == 2
    assert ("S", ["a", "S", "b", "S"]) in prods
    assert ("S", ["c"]) in prods


def test_named_pattern3(tmp_path):
    tmp_file = tmp_path / "file.txt"
    tmp_file.write_text("S = a S b S;\nconnect to [data_base];\nS = A B;")
    visitor = process(get_stream(True, os.path.normpath(tmp_file)))
    prods = visitor.get_prods()

    assert len(prods) == 2
    assert ("S", ["a", "S", "b", "S"]) in prods
    assert ("S", ["A", "B"]) in prods


def test_named_pattern4(tmp_path):
    tmp_file = tmp_path / "file.txt"
    tmp_file.write_text("S = a b c; S = a b c;")
    visitor = process(get_stream(True, os.path.normpath(tmp_file)))
    prods = visitor.get_prods()

    assert len(prods) == 1
    assert ("S", ["a", "b", "c"]) in prods


def test_select_exists1(tmp_path, capsys):
    file_script = tmp_path / "script.txt"
    file_graph = tmp_path / "graph.txt"
    file_graph.write_text("0 a 1\n1 b 0")
    file_script.write_text("S = a S b S;\nS = ();\nselect exists u from [" + os.path.normpath(file_graph) + "] where (u) - S -> (v);")
    visitor = process(get_stream(True, os.path.normpath(file_script)))
    out, err = capsys.readouterr()

    assert out == "exists\n"
    assert err == ""


def test_select_exists2(tmp_path, capsys):
    file_script = tmp_path / "script.txt"
    file_graph = tmp_path / "graph.txt"
    file_graph.write_text("0 a 1\n1 b 0")
    file_script.write_text("S = a S b S;\nS = ();\nselect exists (u, v) from [" + os.path.normpath(file_graph) + "] where (u) - S -> (v);")
    process(get_stream(True, os.path.normpath(file_script)))
    out, err = capsys.readouterr()

    assert out == "exists\n"
    assert err == ""


def test_select_exists3(tmp_path, capsys):
    file_script = tmp_path / "script.txt"
    file_graph = tmp_path / "graph.txt"
    file_graph.write_text("0 a 1\n1 a 0")
    file_script.write_text("S = a S b S;\nselect exists v from [" + os.path.normpath(file_graph) + "] where (u) - S -> (v);")
    process(get_stream(True, os.path.normpath(file_script)))
    out, err = capsys.readouterr()

    assert out == "does not exist\n"
    assert err == ""


def test_select_exists4(tmp_path, capsys):
    file_script = tmp_path / "script.txt"
    file_graph = tmp_path / "graph.txt"
    file_graph.write_text("0 a 1\n1 b 2\n2 c 3")
    file_script.write_text("select exists u from [" + os.path.normpath(file_graph) + "] where (u) - a b c -> (v);")
    process(get_stream(True, os.path.normpath(file_script)))
    out, err = capsys.readouterr()

    assert out == "exists\n"
    assert err == ""


def test_select_exists5(tmp_path, capsys):
    file_script = tmp_path / "script.txt"
    file_graph = tmp_path / "graph.txt"
    file_graph.write_text("0 a 1\n1 b 2\n2 c 3")
    file_script.write_text("select exists v from [" + os.path.normpath(file_graph) + "] where (u) - a b b -> (v);")
    process(get_stream(True, os.path.normpath(file_script)))
    out, err = capsys.readouterr()

    assert out == "does not exist\n"
    assert err == ""


def test_select_exists6(tmp_path, capsys):
    file_script = tmp_path / "script.txt"
    file_graph = tmp_path / "graph.txt"
    file_graph.write_text("0 b 1\n1 a 2\n2 b 1")
    file_script.write_text("A = a;\nB = b;\nselect exists u from [" + os.path.normpath(file_graph) + "] where (u) - A B -> (v);")
    process(get_stream(True, os.path.normpath(file_script)))
    out, err = capsys.readouterr()

    assert out == "exists\n"
    assert err == ""


def test_select_exists7(tmp_path, capsys):
    file_script = tmp_path / "script.txt"
    file_graph = tmp_path / "graph.txt"
    file_graph.write_text("0 a 1\n1 a 0")
    file_script.write_text("S = a S b S;\nS = ();\nselect exists v from [" + os.path.normpath(file_graph) + "] where (u) - S -> (v);")
    process(get_stream(True, os.path.normpath(file_script)))
    out, err = capsys.readouterr()

    assert out == "exists\n"
    assert err == ""
