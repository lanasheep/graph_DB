# Generated from GraphQueries.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .GraphQueriesParser import GraphQueriesParser
else:
    from GraphQueriesParser import GraphQueriesParser

# This class defines a complete listener for a parse tree produced by GraphQueriesParser.
class GraphQueriesListener(ParseTreeListener):

    # Enter a parse tree produced by GraphQueriesParser#script.
    def enterScript(self, ctx:GraphQueriesParser.ScriptContext):
        pass

    # Exit a parse tree produced by GraphQueriesParser#script.
    def exitScript(self, ctx:GraphQueriesParser.ScriptContext):
        pass


    # Enter a parse tree produced by GraphQueriesParser#stmt.
    def enterStmt(self, ctx:GraphQueriesParser.StmtContext):
        pass

    # Exit a parse tree produced by GraphQueriesParser#stmt.
    def exitStmt(self, ctx:GraphQueriesParser.StmtContext):
        pass


    # Enter a parse tree produced by GraphQueriesParser#named_pattern.
    def enterNamed_pattern(self, ctx:GraphQueriesParser.Named_patternContext):
        pass

    # Exit a parse tree produced by GraphQueriesParser#named_pattern.
    def exitNamed_pattern(self, ctx:GraphQueriesParser.Named_patternContext):
        pass


    # Enter a parse tree produced by GraphQueriesParser#select_stmt.
    def enterSelect_stmt(self, ctx:GraphQueriesParser.Select_stmtContext):
        pass

    # Exit a parse tree produced by GraphQueriesParser#select_stmt.
    def exitSelect_stmt(self, ctx:GraphQueriesParser.Select_stmtContext):
        pass


    # Enter a parse tree produced by GraphQueriesParser#func.
    def enterFunc(self, ctx:GraphQueriesParser.FuncContext):
        pass

    # Exit a parse tree produced by GraphQueriesParser#func.
    def exitFunc(self, ctx:GraphQueriesParser.FuncContext):
        pass


    # Enter a parse tree produced by GraphQueriesParser#where_expr.
    def enterWhere_expr(self, ctx:GraphQueriesParser.Where_exprContext):
        pass

    # Exit a parse tree produced by GraphQueriesParser#where_expr.
    def exitWhere_expr(self, ctx:GraphQueriesParser.Where_exprContext):
        pass


    # Enter a parse tree produced by GraphQueriesParser#v_expr.
    def enterV_expr(self, ctx:GraphQueriesParser.V_exprContext):
        pass

    # Exit a parse tree produced by GraphQueriesParser#v_expr.
    def exitV_expr(self, ctx:GraphQueriesParser.V_exprContext):
        pass


    # Enter a parse tree produced by GraphQueriesParser#pattern.
    def enterPattern(self, ctx:GraphQueriesParser.PatternContext):
        pass

    # Exit a parse tree produced by GraphQueriesParser#pattern.
    def exitPattern(self, ctx:GraphQueriesParser.PatternContext):
        pass


    # Enter a parse tree produced by GraphQueriesParser#elem.
    def enterElem(self, ctx:GraphQueriesParser.ElemContext):
        pass

    # Exit a parse tree produced by GraphQueriesParser#elem.
    def exitElem(self, ctx:GraphQueriesParser.ElemContext):
        pass


    # Enter a parse tree produced by GraphQueriesParser#seq.
    def enterSeq(self, ctx:GraphQueriesParser.SeqContext):
        pass

    # Exit a parse tree produced by GraphQueriesParser#seq.
    def exitSeq(self, ctx:GraphQueriesParser.SeqContext):
        pass


    # Enter a parse tree produced by GraphQueriesParser#seq_elem.
    def enterSeq_elem(self, ctx:GraphQueriesParser.Seq_elemContext):
        pass

    # Exit a parse tree produced by GraphQueriesParser#seq_elem.
    def exitSeq_elem(self, ctx:GraphQueriesParser.Seq_elemContext):
        pass


    # Enter a parse tree produced by GraphQueriesParser#prim_pattern.
    def enterPrim_pattern(self, ctx:GraphQueriesParser.Prim_patternContext):
        pass

    # Exit a parse tree produced by GraphQueriesParser#prim_pattern.
    def exitPrim_pattern(self, ctx:GraphQueriesParser.Prim_patternContext):
        pass



del GraphQueriesParser