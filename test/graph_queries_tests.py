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
    assert ("S", "a S b S") in prods


def test_named_pattern2(tmp_path):
    tmp_file = tmp_path / "file.txt"
    tmp_file.write_text("S = a S b S;\nA = a;")
    visitor = process(get_stream(True, os.path.normpath(tmp_file)))
    prods = visitor.get_prods()

    assert len(prods) == 2
    assert ("S", "a S b S") in prods
    assert ("A", "a") in prods


def test_named_pattern3(tmp_path):
    tmp_file = tmp_path / "file.txt"
    tmp_file.write_text("S = a S b S;\nconnect to [data_base];\nS = A B;")
    visitor = process(get_stream(True, os.path.normpath(tmp_file)))
    prods = visitor.get_prods()

    assert len(prods) == 1
    assert ("S", "a S b S | A B") in prods


def test_named_pattern4(tmp_path):
    tmp_file = tmp_path / "file.txt"
    tmp_file.write_text("S = a b c;\nS = (c S c)*;")
    visitor = process(get_stream(True, os.path.normpath(tmp_file)))
    prods = visitor.get_prods()

    assert len(prods) == 1
    assert ("S", "a b c | (c S c)*") in prods


def test_named_pattern5(tmp_path):
    tmp_file = tmp_path / "file.txt"
    tmp_file.write_text("A = (a B b)* | c d c (A b)* | (a | c)*;")
    visitor = process(get_stream(True, os.path.normpath(tmp_file)))
    prods = visitor.get_prods()

    assert len(prods) == 1
    assert ("A", "(a B b)* | c d c (A b)* | (a | c)*") in prods



def test_select_exists1(tmp_path, capsys):
    file_script = tmp_path / "script.txt"
    file_graph = tmp_path / "graph.txt"
    file_graph.write_text("0 a 1\n1 b 0")
    file_script.write_text("S = a S b S;\nS = ();\nselect exists from [" + os.path.normpath(file_graph) + "] where (_) - S -> (_);")
    process(get_stream(True, os.path.normpath(file_script)))
    out, err = capsys.readouterr()

    assert out == "exists\n"
    assert err == ""


def test_select_exists2(tmp_path, capsys):
    file_script = tmp_path / "script.txt"
    file_graph = tmp_path / "graph.txt"
    file_graph.write_text("0 a 1\n1 b 0")
    file_script.write_text("S = a S b S;\nS = ();\nselect exists from [" + os.path.normpath(file_graph) + "] where (_) - S -> (_);")
    process(get_stream(True, os.path.normpath(file_script)))
    out, err = capsys.readouterr()

    assert out == "exists\n"
    assert err == ""


def test_select_exists3(tmp_path, capsys):
    file_script = tmp_path / "script.txt"
    file_graph = tmp_path / "graph.txt"
    file_graph.write_text("0 a 1\n1 a 0")
    file_script.write_text("S = a S b S;\nselect exists from [" + os.path.normpath(file_graph) + "] where (_) - S -> (_);")
    process(get_stream(True, os.path.normpath(file_script)))
    out, err = capsys.readouterr()

    assert out == "does not exist\n"
    assert err == ""


def test_select_exists4(tmp_path, capsys):
    file_script = tmp_path / "script.txt"
    file_graph = tmp_path / "graph.txt"
    file_graph.write_text("0 a 1\n1 b 2\n2 c 3")
    file_script.write_text("select exists from [" + os.path.normpath(file_graph) + "] where (_) - a b c -> (_);")
    process(get_stream(True, os.path.normpath(file_script)))
    out, err = capsys.readouterr()

    assert out == "exists\n"
    assert err == ""


def test_select_exists5(tmp_path, capsys):
    file_script = tmp_path / "script.txt"
    file_graph = tmp_path / "graph.txt"
    file_graph.write_text("0 a 1\n1 b 2\n2 c 3")
    file_script.write_text("select exists from [" + os.path.normpath(file_graph) + "] where (_) - a b b -> (_);")
    process(get_stream(True, os.path.normpath(file_script)))
    out, err = capsys.readouterr()

    assert out == "does not exist\n"
    assert err == ""


def test_select_exists6(tmp_path, capsys):
    file_script = tmp_path / "script.txt"
    file_graph = tmp_path / "graph.txt"
    file_graph.write_text("0 b 1\n1 a 2\n2 b 1")
    file_script.write_text("A = a;\nB = b;\nselect exists from [" + os.path.normpath(file_graph) + "] where (_) - A B -> (_);")
    process(get_stream(True, os.path.normpath(file_script)))
    out, err = capsys.readouterr()

    assert out == "exists\n"
    assert err == ""


def test_select_exists7(tmp_path, capsys):
    file_script = tmp_path / "script.txt"
    file_graph = tmp_path / "graph.txt"
    file_graph.write_text("0 a 1\n1 a 0")
    file_script.write_text("S = a S b S;\nS = ();\nselect exists from [" + os.path.normpath(file_graph) + "] where (_) - S -> (_);")
    process(get_stream(True, os.path.normpath(file_script)))
    out, err = capsys.readouterr()

    assert out == "exists\n"
    assert err == ""


def test_select_exists8(tmp_path, capsys):
    file_script = tmp_path / "script.txt"
    file_graph = tmp_path / "graph.txt"
    file_graph.write_text("0 a 1\n1 b 2\n2 a 3")
    file_script.write_text("S = a | ();\nselect exists from [" + os.path.normpath(file_graph) + "] where (0) - a b S -> (3);")
    process(get_stream(True, os.path.normpath(file_script)))
    out, err = capsys.readouterr()

    assert out == "exists\n"
    assert err == ""


def test_select_exists9(tmp_path, capsys):
    file_script = tmp_path / "script.txt"
    file_graph = tmp_path / "graph.txt"
    file_graph.write_text("0 a 1\n1 b 2\n2 a 3")
    file_script.write_text("S = a | ();\nselect exists from [" + os.path.normpath(file_graph) + "] where (0) - a b b S -> (3);")
    process(get_stream(True, os.path.normpath(file_script)))
    out, err = capsys.readouterr()

    assert out == "does not exist\n"
    assert err == ""


def test_select_exists10(tmp_path, capsys):
    file_script = tmp_path / "script.txt"
    file_graph = tmp_path / "graph.txt"
    file_graph.write_text("0 a 1\n1 b 2\n2 a 3")
    file_script.write_text("S = a | ();\nselect exists from [" + os.path.normpath(file_graph) + "] where (0) - a S S S -> (_);")
    process(get_stream(True, os.path.normpath(file_script)))
    out, err = capsys.readouterr()

    assert out == "exists\n"
    assert err == ""


def test_select_count1(tmp_path, capsys):
    file_script = tmp_path / "script.txt"
    file_graph = tmp_path / "graph.txt"
    file_graph.write_text("0 a 1\n1 b 2\n1 c 3")
    file_script.write_text("S = a (b | c);\nselect count from [" + os.path.normpath(file_graph) + "] where (0) - S -> (_);")
    process(get_stream(True, os.path.normpath(file_script)))
    out, err = capsys.readouterr()

    assert out == "2\n"
    assert err == ""


def test_select_count2(tmp_path, capsys):
    file_script = tmp_path / "script.txt"
    file_graph = tmp_path / "graph.txt"
    file_graph.write_text("0 a 1\n1 b 2\n1 c 3\n2 a 4")
    file_script.write_text("S = a | b | eps;\nselect count from [" + os.path.normpath(file_graph) + "] where (0) - S -> (_);")
    process(get_stream(True, os.path.normpath(file_script)))
    out, err = capsys.readouterr()

    assert out == "2\n"
    assert err == ""


def test_select_count3(tmp_path, capsys):
    file_script = tmp_path / "script.txt"
    file_graph = tmp_path / "graph.txt"
    file_graph.write_text("0 a 1\n1 b 2\n1 c 3\n2 a 4")
    file_script.write_text("select count from [" + os.path.normpath(file_graph) + "] where (0) - (a | b)* -> (_);")
    process(get_stream(True, os.path.normpath(file_script)))
    out, err = capsys.readouterr()

    assert out == "4\n"
    assert err == ""


def test_select_count4(tmp_path, capsys):
    file_script = tmp_path / "script.txt"
    file_graph = tmp_path / "graph.txt"
    file_graph.write_text("0 a 1\n1 b 2\n1 c 3\n2 a 4")
    file_script.write_text("select count from [" + os.path.normpath(file_graph) + "] where (_) - a b -> (0);")
    process(get_stream(True, os.path.normpath(file_script)))
    out, err = capsys.readouterr()

    assert out == "0\n"
    assert err == ""


def test_select_count5(tmp_path, capsys):
    file_script = tmp_path / "script.txt"
    file_graph = tmp_path / "graph.txt"
    file_graph.write_text("0 a 1\n1 b 2\n1 c 3\n2 a 4")
    file_script.write_text("select count from [" + os.path.normpath(file_graph) + "] where (_) - a b -> (_);")
    process(get_stream(True, os.path.normpath(file_script)))
    out, err = capsys.readouterr()

    assert out == "1\n"
    assert err == ""


def test_select_count6(tmp_path, capsys):
    file_script = tmp_path / "script.txt"
    file_graph = tmp_path / "graph.txt"
    file_graph.write_text("0 a 1\n1 b 2\n1 c 3\n2 a 4")
    file_script.write_text("select count from [" + os.path.normpath(file_graph) + "] where (1) - (a | b)* | c -> (_);")
    process(get_stream(True, os.path.normpath(file_script)))
    out, err = capsys.readouterr()

    assert out == "4\n"
    assert err == ""


def test_select_count7(tmp_path, capsys):
    file_script = tmp_path / "script.txt"
    file_graph = tmp_path / "graph.txt"
    file_graph.write_text("0 a 1\n1 b 2\n2 a 3")
    file_script.write_text("S = a | ();\nselect count from [" + os.path.normpath(file_graph) + "] where (_) - S S S -> (_);")
    process(get_stream(True, os.path.normpath(file_script)))
    out, err = capsys.readouterr()

    assert out == "6\n"
    assert err == ""


def test_select_get1(tmp_path, capsys):
    file_script = tmp_path / "script.txt"
    file_graph = tmp_path / "graph.txt"
    file_graph.write_text("0 a 1\n1 b 2\n1 c 3")
    file_script.write_text("S = a (b | c);\nselect get from [" + os.path.normpath(file_graph) + "] where (0) - S -> (_);")
    process(get_stream(True, os.path.normpath(file_script)))
    out, err = capsys.readouterr()

    assert out == "0 2\n0 3\n"
    assert err == ""


def test_select_get2(tmp_path, capsys):
    file_script = tmp_path / "script.txt"
    file_graph = tmp_path / "graph.txt"
    file_graph.write_text("0 a 1\n1 b 2\n1 c 3\n2 a 4")
    file_script.write_text("select get from [" + os.path.normpath(file_graph) + "] where (0) - (a | b)* -> (_);")
    process(get_stream(True, os.path.normpath(file_script)))
    out, err = capsys.readouterr()

    assert out == "0 0\n0 1\n0 2\n0 4\n"
    assert err == ""


def test_select_get3(tmp_path, capsys):
    file_script = tmp_path / "script.txt"
    file_graph = tmp_path / "graph.txt"
    file_graph.write_text("0 a 1\n1 b 2\n1 c 3\n2 a 4")
    file_script.write_text("select get from [" + os.path.normpath(file_graph) + "] where (_) - a b -> (0);")
    process(get_stream(True, os.path.normpath(file_script)))
    out, err = capsys.readouterr()

    assert out == ""
    assert err == ""


def test_select_get4(tmp_path, capsys):
    file_script = tmp_path / "script.txt"
    file_graph = tmp_path / "graph.txt"
    file_graph.write_text("0 a 1\n1 b 2\n1 c 3\n2 a 4")
    file_script.write_text("select get from [" + os.path.normpath(file_graph) + "] where (_) - (a | b)* | c -> (_);")
    process(get_stream(True, os.path.normpath(file_script)))
    out, err = capsys.readouterr()

    assert out == "0 0\n0 1\n0 2\n0 4\n1 1\n1 2\n1 3\n1 4\n2 2\n2 4\n3 3\n4 4\n"
    assert err == ""


def test_select_get5(tmp_path, capsys):
    file_script = tmp_path / "script.txt"
    file_graph = tmp_path / "graph.txt"
    file_graph.write_text("0 a 1\n1 b 2\n2 a 3")
    file_script.write_text("S = A B;\nA = a | ();\nB = b | ();\nselect get from [" + os.path.normpath(file_graph) + "]\
     where (_) - S -> (2);")
    process(get_stream(True, os.path.normpath(file_script)))
    out, err = capsys.readouterr()

    assert out == "0 2\n1 2\n2 2\n"
    assert err == ""


def test_script(tmp_path, capsys):
    file_script = tmp_path / "script.txt"
    file_graph = tmp_path / "graph.txt"
    file_graph.write_text("0 a 1\n1 b 2\n1 c 3\n2 a 4")
    file_script.write_text("select count from [" + os.path.normpath(file_graph) + "] where (0) - (a | b)* -> (_);\n\
    S = (a | b)*;\nselect get from [" + os.path.normpath(file_graph) + "] where (0) - S -> (_);")
    process(get_stream(True, os.path.normpath(file_script)))
    out, err = capsys.readouterr()

    assert out == "4\n0 0\n0 1\n0 2\n0 4\n"
    assert err == ""
