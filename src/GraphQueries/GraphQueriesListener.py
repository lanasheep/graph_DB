# Generated from GraphQueries.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .GraphQueriesParser import GraphQueriesParser
else:
    from GraphQueriesParser import GraphQueriesParser

# This class defines a complete listener for a parse tree produced by GraphQueriesParser.
class GraphQueriesListener(ParseTreeListener):
    def __init__(self, parent=None):
        self.nodes = []
        self.edges = []
        self.stack = []

    # Enter a parse tree produced by GraphQueriesParser#script.
    def enterScript(self, ctx:GraphQueriesParser.ScriptContext):
        num = len(self.nodes)
        self.nodes.append((num, "script"))
        self.stack.append(num)

    # Exit a parse tree produced by GraphQueriesParser#script.
    def exitScript(self, ctx:GraphQueriesParser.ScriptContext):
        self.stack.pop()

    # Enter a parse tree produced by GraphQueriesParser#stmt.
    def enterStmt(self, ctx:GraphQueriesParser.StmtContext):
        num = len(self.nodes)
        self.nodes.append((len(self.nodes), "stmt"))
        self.edges.append((self.stack[-1], num))
        self.stack.append(num)

    # Exit a parse tree produced by GraphQueriesParser#stmt.
    def exitStmt(self, ctx:GraphQueriesParser.StmtContext):
        self.stack.pop()

    # Enter a parse tree produced by GraphQueriesParser#named_pattern.
    def enterNamed_pattern(self, ctx:GraphQueriesParser.Named_patternContext):
        num = len(self.nodes)
        self.nodes.append((len(self.nodes), "named_pattern"))
        self.edges.append((self.stack[-1], num))
        self.stack.append(num)

    # Exit a parse tree produced by GraphQueriesParser#named_pattern.
    def exitNamed_pattern(self, ctx:GraphQueriesParser.Named_patternContext):
        self.stack.pop()

    # Enter a parse tree produced by GraphQueriesParser#select_stmt.
    def enterSelect_stmt(self, ctx:GraphQueriesParser.Select_stmtContext):
        num = len(self.nodes)
        self.nodes.append((len(self.nodes), "select_stmt"))
        self.edges.append((self.stack[-1], num))
        self.stack.append(num)

    # Exit a parse tree produced by GraphQueriesParser#select_stmt.
    def exitSelect_stmt(self, ctx:GraphQueriesParser.Select_stmtContext):
        self.stack.pop()

    # Enter a parse tree produced by GraphQueriesParser#obj_expr.
    def enterObj_expr(self, ctx:GraphQueriesParser.Obj_exprContext):
        num = len(self.nodes)
        self.nodes.append((len(self.nodes), "obj_expr"))
        self.edges.append((self.stack[-1], num))
        self.stack.append(num)

    # Exit a parse tree produced by GraphQueriesParser#obj_expr.
    def exitObj_expr(self, ctx:GraphQueriesParser.Obj_exprContext):
        self.stack.pop()

    # Enter a parse tree produced by GraphQueriesParser#vs_info.
    def enterVs_info(self, ctx:GraphQueriesParser.Vs_infoContext):
        num = len(self.nodes)
        self.nodes.append((len(self.nodes), "vs_info"))
        self.edges.append((self.stack[-1], num))
        self.stack.append(num)

    # Exit a parse tree produced by GraphQueriesParser#vs_info.
    def exitVs_info(self, ctx:GraphQueriesParser.Vs_infoContext):
        self.stack.pop()

    # Enter a parse tree produced by GraphQueriesParser#v_info.
    def enterV_info(self, ctx:GraphQueriesParser.V_infoContext):
        num = len(self.nodes)
        self.nodes.append((len(self.nodes), "v_info"))
        self.edges.append((self.stack[-1], num))
        self.stack.append(num)

    # Exit a parse tree produced by GraphQueriesParser#v_info.
    def exitV_info(self, ctx:GraphQueriesParser.V_infoContext):
        self.stack.pop()

    # Enter a parse tree produced by GraphQueriesParser#where_expr.
    def enterWhere_expr(self, ctx:GraphQueriesParser.Where_exprContext):
        num = len(self.nodes)
        self.nodes.append((len(self.nodes), "where_expr"))
        self.edges.append((self.stack[-1], num))
        self.stack.append(num)

    # Exit a parse tree produced by GraphQueriesParser#where_expr.
    def exitWhere_expr(self, ctx:GraphQueriesParser.Where_exprContext):
        self.stack.pop()


    # Enter a parse tree produced by GraphQueriesParser#v_expr.
    def enterV_expr(self, ctx:GraphQueriesParser.V_exprContext):
        num = len(self.nodes)
        self.nodes.append((len(self.nodes), "v_expr"))
        self.edges.append((self.stack[-1], num))
        self.stack.append(num)

    # Exit a parse tree produced by GraphQueriesParser#v_expr.
    def exitV_expr(self, ctx:GraphQueriesParser.V_exprContext):
        self.stack.pop()

    # Enter a parse tree produced by GraphQueriesParser#pattern.
    def enterPattern(self, ctx:GraphQueriesParser.PatternContext):
        num = len(self.nodes)
        self.nodes.append((len(self.nodes), "pattern"))
        self.edges.append((self.stack[-1], num))
        self.stack.append(num)

    # Exit a parse tree produced by GraphQueriesParser#pattern.
    def exitPattern(self, ctx:GraphQueriesParser.PatternContext):
        self.stack.pop()

    # Enter a parse tree produced by GraphQueriesParser#elem.
    def enterElem(self, ctx:GraphQueriesParser.ElemContext):
        num = len(self.nodes)
        self.nodes.append((len(self.nodes), "elem"))
        self.edges.append((self.stack[-1], num))
        self.stack.append(num)

    # Exit a parse tree produced by GraphQueriesParser#elem.
    def exitElem(self, ctx:GraphQueriesParser.ElemContext):
        self.stack.pop()


    # Enter a parse tree produced by GraphQueriesParser#seq.
    def enterSeq(self, ctx:GraphQueriesParser.SeqContext):
        num = len(self.nodes)
        self.nodes.append((len(self.nodes), "seq"))
        self.edges.append((self.stack[-1], num))
        self.stack.append(num)

    # Exit a parse tree produced by GraphQueriesParser#seq.
    def exitSeq(self, ctx:GraphQueriesParser.SeqContext):
        self.stack.pop()


    # Enter a parse tree produced by GraphQueriesParser#seq_elem.
    def enterSeq_elem(self, ctx:GraphQueriesParser.Seq_elemContext):
        num = len(self.nodes)
        self.nodes.append((len(self.nodes), "seq_elem"))
        self.edges.append((self.stack[-1], num))
        self.stack.append(num)

    # Exit a parse tree produced by GraphQueriesParser#seq_elem.
    def exitSeq_elem(self, ctx:GraphQueriesParser.Seq_elemContext):
        self.stack.pop()


    # Enter a parse tree produced by GraphQueriesParser#prim_pattern.
    def enterPrim_pattern(self, ctx:GraphQueriesParser.Prim_patternContext):
        num = len(self.nodes)
        self.nodes.append((len(self.nodes), "prim_pattern"))
        self.edges.append((self.stack[-1], num))
        self.stack.append(num)

    # Exit a parse tree produced by GraphQueriesParser#prim_pattern.
    def exitPrim_pattern(self, ctx:GraphQueriesParser.Prim_patternContext):
        self.stack.pop()



del GraphQueriesParser
