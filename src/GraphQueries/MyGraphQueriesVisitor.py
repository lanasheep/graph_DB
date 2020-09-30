#!/usr/bin/env python3
import os
from antlr4 import *
from algebra import matrix_alg
from chomsky import is_term
from chomsky import get_new_nonterm
from chomsky import to_weak_CNF
from cyk import parse_graph
if __name__ is not None and "." in __name__:
    from .GraphQueriesParser import GraphQueriesParser
else:
    from GraphQueriesParser import GraphQueriesParser

# This class defines a complete generic visitor for a parse tree produced by GraphQueriesParser.

class MyGraphQueriesVisitor(ParseTreeVisitor):
    def __init__(self, parent=None):
        self.addr = ""
        self.prods = []


    def get_addr(self):
        return self.addr


    def get_prods(self):
        return self.prods


    # Visit a parse tree produced by GraphQueriesParser#script.
    def visitScript(self, ctx:GraphQueriesParser.ScriptContext):
        self.visitChildren(ctx)


    # Visit a parse tree produced by GraphQueriesParser#stmt.
    def visitStmt(self, ctx:GraphQueriesParser.StmtContext):
        if ctx.children[0].getText() == "connect":
            self.addr = ctx.STRING().getText()[1:-1]
        elif ctx.children[0].getText() == "list":
            for file in sorted(os.listdir(self.addr)):
                print(open(os.path.join(self.addr, file), "r").read() + "\n")
        else:
            self.visitChildren(ctx)


    # Visit a parse tree produced by GraphQueriesParser#named_pattern.
    def visitNamed_pattern(self, ctx:GraphQueriesParser.Named_patternContext):
        new_prod = (ctx.NT_NAME().getText(), self.visitPattern(ctx.pattern()))
        if new_prod not in self.prods:
            self.prods.append(new_prod)


    # Visit a parse tree produced by GraphQueriesParser#select_stmt.
    def visitSelect_stmt(self, ctx:GraphQueriesParser.Select_stmtContext):
        if ctx.obj_expr().children[0].getText() == "exists":
            pattern = self.visitPattern(ctx.where_expr().pattern())
            nonterms = set()
            for prod in self.prods:
                nonterms.add(prod[0])
                for symb in prod[1]:
                    if not is_term(symb):
                        nonterms.add(symb)
            add_nonterm = get_new_nonterm("S", nonterms)
            graph = parse_graph(ctx.STRING().getText()[1:-1])
            ans = matrix_alg(to_weak_CNF(self.prods + [(add_nonterm, pattern)], add_nonterm), graph)
            if add_nonterm in [nonterm for nonterm, _, _ in ans]:
                print("exists")
            else:
                print("does not exist")


    # Visit a parse tree produced by GraphQueriesParser#obj_expr.
    def visitObj_expr(self, ctx:GraphQueriesParser.Obj_exprContext):
        pass


    # Visit a parse tree produced by GraphQueriesParser#vs_info.
    def visitVs_info(self, ctx:GraphQueriesParser.Vs_infoContext):
        pass


    # Visit a parse tree produced by GraphQueriesParser#v_info.
    def visitV_info(self, ctx:GraphQueriesParser.V_infoContext):
        pass


    # Visit a parse tree produced by GraphQueriesParser#where_expr.
    def visitWhere_expr(self, ctx:GraphQueriesParser.Where_exprContext):
        pass


    # Visit a parse tree produced by GraphQueriesParser#v_expr.
    def visitV_expr(self, ctx:GraphQueriesParser.V_exprContext):
        return ctx.getChild(0).getText()


    # Visit a parse tree produced by GraphQueriesParser#pattern.
    def visitPattern(self, ctx:GraphQueriesParser.PatternContext):
        return self.visitElem(ctx.elem())


    # Visit a parse tree produced by GraphQueriesParser#elem.
    def visitElem(self, ctx:GraphQueriesParser.ElemContext):
        if len(ctx.children) == 1:
            return self.visitSeq(ctx.seq())
        else:
            return ["eps"]


    # Visit a parse tree produced by GraphQueriesParser#seq.
    def visitSeq(self, ctx:GraphQueriesParser.SeqContext):
        if len(ctx.children) == 2:
            return [self.visitSeq_elem(ctx.seq_elem())] + self.visitSeq(ctx.seq())
        else:
            return [self.visitSeq_elem(ctx.seq_elem())]


    # Visit a parse tree produced by GraphQueriesParser#seq_elem.
    def visitSeq_elem(self, ctx:GraphQueriesParser.Seq_elemContext):
        return self.visitPrim_pattern(ctx.prim_pattern())


    # Visit a parse tree produced by GraphQueriesParser#prim_pattern.
    def visitPrim_pattern(self, ctx:GraphQueriesParser.Prim_patternContext):
        return ctx.getChild(0).getText()



del GraphQueriesParser
