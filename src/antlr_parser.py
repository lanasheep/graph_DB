#!/usr/bin/env python3
from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener
from GraphQueriesLexer import GraphQueriesLexer
from GraphQueriesParser import GraphQueriesParser
from GraphQueriesListener import GraphQueriesListener


class ParseError(Exception):
    pass


class ErrorListener_(ErrorListener):
    def __init__(self):
        super(ErrorListener_, self).__init__()

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise ParseError()

    def reportAmbiguity(self, recognizer, dfa, startIndex, stopIndex, exact, ambigAlts, configs):
        raise ParseError()

    def reportAttemptingFullContext(self, recognizer, dfa, startIndex, stopIndex, conflictingAlts, configs):
        raise ParseError()

    def reportContextSensitivity(self, recognizer, dfa, startIndex, stopIndex, prediction, configs):
        raise ParseError()


def get_stream(from_file, filename=None):
    if from_file:
        return FileStream(filename)
    else:
        return StdinStream()


def parse(stream):
    lexer = GraphQueriesLexer(stream)
    ct_stream = CommonTokenStream(lexer)
    parser = GraphQueriesParser(ct_stream)
    parser.addErrorListener(ErrorListener_())

    try:
        return parser.script()
    except:
        return None


def check(stream):
    if parse(stream) is None:
        print("error, script isn't correct")
    else:
        print("ok, script is correct")


def print_tree_dot(stream, filename):
    tree = parse(stream)
    if tree is None:
        return
    walker = ParseTreeWalker()
    listener = GraphQueriesListener()
    walker.walk(listener, tree)

    with open(filename, "w") as file:
        file.write("digraph {\n")
        for (node, label) in listener.nodes:
            file.write("\t" + str(node) + " [label=" + str(label) + "];\n")
        for (v1, v2) in listener.edges:
            file.write("\t" + str(v1) + " -> " + str(v2) + ";\n")
        file.write("}")



