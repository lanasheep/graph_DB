#!/usr/bin/env python3
import pytest
import os
from antlr_parser import get_stream
from antlr_parser import check
from antlr_parser import print_tree_dot


def test_check_named_pattern(tmp_path, capsys):
    tmp_file = tmp_path / "file.txt"
    tmp_file.write_text("S = a S b S | ();")
    check(get_stream(True, os.path.normpath(tmp_file)))
    out, err = capsys.readouterr()

    assert out == "ok, script is correct\n"
    assert err == ""


def test_check_script(tmp_path, capsys):
    tmp_file = tmp_path / "file.txt"
    tmp_file.write_text("connect to [/home/user/graph_db];\nS = a S b S | ();\n\
select count u from [g1.txt] where (v.id = 10) - S -> (u);")
    check(get_stream(True, os.path.normpath(tmp_file)))
    out, err = capsys.readouterr()

    assert out == "ok, script is correct\n"
    assert err == ""


def test_check_select_stmt(tmp_path, capsys):
    tmp_file = tmp_path / "file.txt"
    tmp_file.write_text("select exists (u,v) from [g1.txt] where (u) - (a | b)* | c -> (v);")
    check(get_stream(True, os.path.normpath(tmp_file)))
    out, err = capsys.readouterr()

    assert out == "ok, script is correct\n"
    assert err == ""


def test_check_empty_script(tmp_path, capsys):
    tmp_file = tmp_path / "file.txt"
    tmp_file.write_text("")
    check(get_stream(True, os.path.normpath(tmp_file)))
    out, err = capsys.readouterr()

    assert out == "ok, script is correct\n"
    assert err == ""


def test_check_forgot_semicolon(tmp_path, capsys):
    tmp_file = tmp_path / "file.txt"
    tmp_file.write_text("S = a S b S | ()")
    check(get_stream(True, os.path.normpath(tmp_file)))
    out, err = capsys.readouterr()

    assert out == "error, script isn't correct\n"


def test_check_wrong_syntax(tmp_path, capsys):
    tmp_file = tmp_path / "file.txt"
    tmp_file.write_text("select count u from [g1.txt] where (v.id = 10) - S -> u;")
    check(get_stream(True, os.path.normpath(tmp_file)))
    out, err = capsys.readouterr()

    assert out == "error, script isn't correct\n"


def test_check_incorrect_pattern(tmp_path, capsys):
    tmp_file = tmp_path / "file.txt"
    tmp_file.write_text("A = ((a | b)+ | (c)*) |")
    check(get_stream(True, os.path.normpath(tmp_file)))
    out, err = capsys.readouterr()

    assert out == "error, script isn't correct\n"


def test_print_tree_dot1(tmp_path):
    file_in = tmp_path / "file_in.txt"
    file_out = tmp_path / "file_out.txt"
    file_in.write_text("connect to [data_base];")
    stream = get_stream(True, os.path.normpath(file_in))
    print_tree_dot(stream, file_out)
    assert open(os.path.normpath(file_out), "r").read() == \
"""digraph {
	0 [label=script];
	1 [label=stmt];
	0 -> 1;
}"""


def test_print_tree_dot2(tmp_path):
    file_in = tmp_path / "file_in.txt"
    file_out = tmp_path / "file_out.txt"
    file_in.write_text("S = a;")
    stream = get_stream(True, os.path.normpath(file_in))
    print_tree_dot(stream, file_out)
    assert open(os.path.normpath(file_out), "r").read() == \
"""digraph {
	0 [label=script];
	1 [label=stmt];
	2 [label=named_pattern];
	3 [label=pattern];
	4 [label=elem];
	5 [label=seq];
	6 [label=seq_elem];
	7 [label=prim_pattern];
	0 -> 1;
	1 -> 2;
	2 -> 3;
	3 -> 4;
	4 -> 5;
	5 -> 6;
	6 -> 7;
}"""
