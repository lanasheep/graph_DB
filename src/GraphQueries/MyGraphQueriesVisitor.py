#!/usr/bin/env python3
import os
from collections import defaultdict
from antlr4 import *
from chomsky import to_weak_CNF
from algebra import matrix_alg
from algebra import tensor_alg
from chomsky import get_new_nonterm
from cyk import parse_graph
from cyk import Hellings
if __name__ is not None and "." in __name__:
    from .GraphQueriesParser import GraphQueriesParser
else:
    from GraphQueriesParser import GraphQueriesParser

# This class defines a complete generic visitor for a parse tree produced by GraphQueriesParser.

class MyGraphQueriesVisitor(ParseTreeVisitor):
    def __init__(self, parent=None):
        self.addr = ""
        self.prods = defaultdict(str)


    def get_addr(self):
        return self.addr


    def get_prods(self):
        return self.prods.items()


    def select_get_tensors(self, start, finish, pattern, graph):
        nonterms = self.prods.keys()
        add_nonterm = get_new_nonterm("S", nonterms)
        _, matrix, _, n = tensor_alg(list(self.prods.items()) + [(add_nonterm, pattern)], graph)
        res = []
        if start == "_" and finish == "_":
            for i in range(n):
                for j in range(n):
                    if matrix[add_nonterm][i, j]:
                        res.append((i, j))
        elif start == "_":
            for i in range(n):
                if matrix[add_nonterm][i, int(finish)]:
                    res.append((i, int(finish)))
        elif finish == "_":
            for i in range(n):
                if matrix[add_nonterm][int(start), i]:
                    res.append((int(start), i))
        else:
            if matrix[add_nonterm][int(start), int(finish)]:
                res.append((int(start), int(finish)))

        return res


    def select_get(self, start, finish, pattern, graph, alg):
        nonterms = self.prods.keys()
        add_nonterm = get_new_nonterm("S", nonterms)
        new_prods = []
        for nonterm in self.prods.keys():
            lst = self.prods[nonterm].split(" | ")
            new_prods += [(nonterm, element.split()) for element in lst]
        new_prods = to_weak_CNF(new_prods + [(add_nonterm, pattern.split())], add_nonterm)
        if alg == "hellings":
            res = Hellings(new_prods, graph)
        else:
            res = matrix_alg(new_prods, graph)
        return [(u, v) for (nonterm, u, v) in res if nonterm == add_nonterm]


    # Visit a parse tree produced by GraphQueriesParser#script.
    def visitScript(self, ctx:GraphQueriesParser.ScriptContext):
        self.visitChildren(ctx)


    # Visit a parse tree produced by GraphQueriesParser#stmt.
    def visitStmt(self, ctx:GraphQueriesParser.StmtContext):
        if ctx.getChild(0).getText() == "connect":
            self.addr = ctx.STRING().getText()[1:-1]
        elif ctx.getChild(0).getText() == "list":
            if ctx.getChild(1).getText() == "all":
                if ctx.getChildCount() == 3:
                    path = ctx.STRING().getText()[1:-1]
                else:
                    path = self.addr
                for file in sorted(os.listdir(path)):
                    print(open(os.path.join(path, file), "r").read() + "\n")
            else:
                filename = ctx.STRING().getText()[1:-1]
                labels = set()
                with open(os.path.join(filename))  as file:
                    for line in file.readlines():
                        labels.add(line.split()[1])
                print(" ".join(sorted(list(labels))))
        else:
            self.visitChildren(ctx)


    # Visit a parse tree produced by GraphQueriesParser#named_pattern.
    def visitNamed_pattern(self, ctx:GraphQueriesParser.Named_patternContext):
        nonterm = ctx.NT_NAME().getText()
        if self.prods[nonterm]:
            self.prods[nonterm] += " | " + self.visitPattern(ctx.pattern())
        else:
            self.prods[nonterm] = self.visitPattern(ctx.pattern())


    # Visit a parse tree produced by GraphQueriesParser#select_stmt.
    def visitSelect_stmt(self, ctx:GraphQueriesParser.Select_stmtContext):
        pattern = self.visitPattern(ctx.where_expr().pattern())
        if ctx.getChildCount() == 6 or (ctx.getChildCount() == 7 and ctx.alg().getChild(1).getText() == "tensors"):
            res = self.select_get_tensors(ctx.where_expr().getChild(1).getText(), ctx.where_expr().getChild(8).getText(), pattern, \
                              parse_graph(ctx.STRING().getText()[1:-1]))
        else:
            res = self.select_get(ctx.where_expr().getChild(1).getText(), ctx.where_expr().getChild(8).getText(), pattern, \
                              parse_graph(ctx.STRING().getText()[1:-1]), ctx.alg().getChild(1).getText())
        if ctx.func().getText() == "exists":
            if res:
                print("exists")
            else:
                print("does not exist")
        elif ctx.func().getText() == "count":
            print(len(res))
        else:
            for u, v in res:
                print(str(u) + " " + str(v))


    # Visit a parse tree produced by GraphQueriesParser#pattern.
    def visitPattern(self, ctx:GraphQueriesParser.PatternContext):
        if ctx.getChildCount() == 3:
            return self.visitElem(ctx.elem()) + " " + ctx.MID().getText() + " " + self.visitPattern(ctx.pattern())
        return self.visitElem(ctx.elem())


    # Visit a parse tree produced by GraphQueriesParser#elem.
    def visitElem(self, ctx:GraphQueriesParser.ElemContext):
        if ctx.getChildCount() == 1:
            return self.visitSeq(ctx.seq())
        else:
            return "eps"


    # Visit a parse tree produced by GraphQueriesParser#seq.
    def visitSeq(self, ctx:GraphQueriesParser.SeqContext):
        if ctx.getChildCount() == 2:
            return self.visitSeq_elem(ctx.seq_elem()) + " " + self.visitSeq(ctx.seq())
        else:
            return self.visitSeq_elem(ctx.seq_elem())


    # Visit a parse tree produced by GraphQueriesParser#seq_elem.
    def visitSeq_elem(self, ctx:GraphQueriesParser.Seq_elemContext):
        if ctx.getChildCount() == 2:
            return self.visitPrim_pattern(ctx.prim_pattern()) + ctx.getChild(1).getText()
        return self.visitPrim_pattern(ctx.prim_pattern())


    # Visit a parse tree produced by GraphQueriesParser#prim_pattern.
    def visitPrim_pattern(self, ctx:GraphQueriesParser.Prim_patternContext):
        if ctx.getChildCount() == 3:
            return ctx.LBR().getText() + self.visitPattern(ctx.pattern()) + ctx.RBR().getText()
        else: return ctx.getChild(0).getText()


del GraphQueriesParser
