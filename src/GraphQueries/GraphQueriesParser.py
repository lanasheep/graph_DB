# Generated from GraphQueries.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\33")
        buf.write("g\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\3\2\3\2")
        buf.write("\3\2\7\2\36\n\2\f\2\16\2!\13\2\3\2\3\2\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\5\3+\n\3\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3")
        buf.write("\7\3\7\3\b\3\b\3\t\3\t\3\t\3\t\3\t\5\tL\n\t\3\n\3\n\3")
        buf.write("\n\5\nQ\n\n\3\13\3\13\3\13\3\13\5\13W\n\13\3\f\3\f\3\f")
        buf.write("\3\f\5\f]\n\f\3\r\3\r\3\r\3\r\3\r\3\r\5\re\n\r\3\r\2\2")
        buf.write("\16\2\4\6\b\n\f\16\20\22\24\26\30\2\4\3\2\17\21\4\2\t")
        buf.write("\t\27\27\2d\2\37\3\2\2\2\4*\3\2\2\2\6,\3\2\2\2\b\60\3")
        buf.write("\2\2\2\n\67\3\2\2\2\f9\3\2\2\2\16D\3\2\2\2\20K\3\2\2\2")
        buf.write("\22P\3\2\2\2\24V\3\2\2\2\26\\\3\2\2\2\30d\3\2\2\2\32\33")
        buf.write("\5\4\3\2\33\34\7\6\2\2\34\36\3\2\2\2\35\32\3\2\2\2\36")
        buf.write("!\3\2\2\2\37\35\3\2\2\2\37 \3\2\2\2 \"\3\2\2\2!\37\3\2")
        buf.write("\2\2\"#\7\2\2\3#\3\3\2\2\2$%\7\25\2\2%&\7\26\2\2&+\7\32")
        buf.write("\2\2\'+\7\24\2\2(+\5\b\5\2)+\5\6\4\2*$\3\2\2\2*\'\3\2")
        buf.write("\2\2*(\3\2\2\2*)\3\2\2\2+\5\3\2\2\2,-\7\31\2\2-.\7\r\2")
        buf.write("\2./\5\20\t\2/\7\3\2\2\2\60\61\7\16\2\2\61\62\5\n\6\2")
        buf.write("\62\63\7\22\2\2\63\64\7\32\2\2\64\65\7\23\2\2\65\66\5")
        buf.write("\f\7\2\66\t\3\2\2\2\678\t\2\2\28\13\3\2\2\29:\7\3\2\2")
        buf.write(":;\5\16\b\2;<\7\4\2\2<=\7\13\2\2=>\5\20\t\2>?\7\13\2\2")
        buf.write("?@\7\f\2\2@A\7\3\2\2AB\5\16\b\2BC\7\4\2\2C\r\3\2\2\2D")
        buf.write("E\t\3\2\2E\17\3\2\2\2FL\5\22\n\2GH\5\22\n\2HI\7\7\2\2")
        buf.write("IJ\5\20\t\2JL\3\2\2\2KF\3\2\2\2KG\3\2\2\2L\21\3\2\2\2")
        buf.write("MQ\5\24\13\2NO\7\3\2\2OQ\7\4\2\2PM\3\2\2\2PN\3\2\2\2Q")
        buf.write("\23\3\2\2\2RW\5\26\f\2ST\5\26\f\2TU\5\24\13\2UW\3\2\2")
        buf.write("\2VR\3\2\2\2VS\3\2\2\2W\25\3\2\2\2X]\5\30\r\2YZ\5\30\r")
        buf.write("\2Z[\7\n\2\2[]\3\2\2\2\\X\3\2\2\2\\Y\3\2\2\2]\27\3\2\2")
        buf.write("\2^e\7\30\2\2_e\7\31\2\2`a\7\3\2\2ab\5\20\t\2bc\7\4\2")
        buf.write("\2ce\3\2\2\2d^\3\2\2\2d_\3\2\2\2d`\3\2\2\2e\31\3\2\2\2")
        buf.write("\t\37*KPV\\d")
        return buf.getvalue()


class GraphQueriesParser ( Parser ):

    grammarFileName = "GraphQueries.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "','", "';'", "'|'", "'.'", 
                     "'_'", "'*'", "'-'", "'>'", "'='", "'select'", "'get'", 
                     "'count'", "'exists'", "'from'", "'where'", "'list'", 
                     "'connect'", "'to'" ]

    symbolicNames = [ "<INVALID>", "LBR", "RBR", "COMMA", "SEMI", "MID", 
                      "DOT", "UNDERSCORE", "OP_STAR", "OP_MINUS", "OP_GR", 
                      "OP_EQ", "KW_SELECT", "KW_GET", "KW_COUNT", "KW_EXISTS", 
                      "KW_FROM", "KW_WHERE", "KW_LIST", "KW_CONNECT", "KW_TO", 
                      "INT", "SYMB", "NT_NAME", "STRING", "WS" ]

    RULE_script = 0
    RULE_stmt = 1
    RULE_named_pattern = 2
    RULE_select_stmt = 3
    RULE_func = 4
    RULE_where_expr = 5
    RULE_v_expr = 6
    RULE_pattern = 7
    RULE_elem = 8
    RULE_seq = 9
    RULE_seq_elem = 10
    RULE_prim_pattern = 11

    ruleNames =  [ "script", "stmt", "named_pattern", "select_stmt", "func", 
                   "where_expr", "v_expr", "pattern", "elem", "seq", "seq_elem", 
                   "prim_pattern" ]

    EOF = Token.EOF
    LBR=1
    RBR=2
    COMMA=3
    SEMI=4
    MID=5
    DOT=6
    UNDERSCORE=7
    OP_STAR=8
    OP_MINUS=9
    OP_GR=10
    OP_EQ=11
    KW_SELECT=12
    KW_GET=13
    KW_COUNT=14
    KW_EXISTS=15
    KW_FROM=16
    KW_WHERE=17
    KW_LIST=18
    KW_CONNECT=19
    KW_TO=20
    INT=21
    SYMB=22
    NT_NAME=23
    STRING=24
    WS=25

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ScriptContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(GraphQueriesParser.EOF, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GraphQueriesParser.StmtContext)
            else:
                return self.getTypedRuleContext(GraphQueriesParser.StmtContext,i)


        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(GraphQueriesParser.SEMI)
            else:
                return self.getToken(GraphQueriesParser.SEMI, i)

        def getRuleIndex(self):
            return GraphQueriesParser.RULE_script

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterScript" ):
                listener.enterScript(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitScript" ):
                listener.exitScript(self)




    def script(self):

        localctx = GraphQueriesParser.ScriptContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_script)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << GraphQueriesParser.KW_SELECT) | (1 << GraphQueriesParser.KW_LIST) | (1 << GraphQueriesParser.KW_CONNECT) | (1 << GraphQueriesParser.NT_NAME))) != 0):
                self.state = 24
                self.stmt()
                self.state = 25
                self.match(GraphQueriesParser.SEMI)
                self.state = 31
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 32
            self.match(GraphQueriesParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_CONNECT(self):
            return self.getToken(GraphQueriesParser.KW_CONNECT, 0)

        def KW_TO(self):
            return self.getToken(GraphQueriesParser.KW_TO, 0)

        def STRING(self):
            return self.getToken(GraphQueriesParser.STRING, 0)

        def KW_LIST(self):
            return self.getToken(GraphQueriesParser.KW_LIST, 0)

        def select_stmt(self):
            return self.getTypedRuleContext(GraphQueriesParser.Select_stmtContext,0)


        def named_pattern(self):
            return self.getTypedRuleContext(GraphQueriesParser.Named_patternContext,0)


        def getRuleIndex(self):
            return GraphQueriesParser.RULE_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStmt" ):
                listener.enterStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStmt" ):
                listener.exitStmt(self)




    def stmt(self):

        localctx = GraphQueriesParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stmt)
        try:
            self.state = 40
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [GraphQueriesParser.KW_CONNECT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 34
                self.match(GraphQueriesParser.KW_CONNECT)
                self.state = 35
                self.match(GraphQueriesParser.KW_TO)
                self.state = 36
                self.match(GraphQueriesParser.STRING)
                pass
            elif token in [GraphQueriesParser.KW_LIST]:
                self.enterOuterAlt(localctx, 2)
                self.state = 37
                self.match(GraphQueriesParser.KW_LIST)
                pass
            elif token in [GraphQueriesParser.KW_SELECT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 38
                self.select_stmt()
                pass
            elif token in [GraphQueriesParser.NT_NAME]:
                self.enterOuterAlt(localctx, 4)
                self.state = 39
                self.named_pattern()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Named_patternContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NT_NAME(self):
            return self.getToken(GraphQueriesParser.NT_NAME, 0)

        def OP_EQ(self):
            return self.getToken(GraphQueriesParser.OP_EQ, 0)

        def pattern(self):
            return self.getTypedRuleContext(GraphQueriesParser.PatternContext,0)


        def getRuleIndex(self):
            return GraphQueriesParser.RULE_named_pattern

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNamed_pattern" ):
                listener.enterNamed_pattern(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNamed_pattern" ):
                listener.exitNamed_pattern(self)




    def named_pattern(self):

        localctx = GraphQueriesParser.Named_patternContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_named_pattern)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self.match(GraphQueriesParser.NT_NAME)
            self.state = 43
            self.match(GraphQueriesParser.OP_EQ)
            self.state = 44
            self.pattern()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Select_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_SELECT(self):
            return self.getToken(GraphQueriesParser.KW_SELECT, 0)

        def func(self):
            return self.getTypedRuleContext(GraphQueriesParser.FuncContext,0)


        def KW_FROM(self):
            return self.getToken(GraphQueriesParser.KW_FROM, 0)

        def STRING(self):
            return self.getToken(GraphQueriesParser.STRING, 0)

        def KW_WHERE(self):
            return self.getToken(GraphQueriesParser.KW_WHERE, 0)

        def where_expr(self):
            return self.getTypedRuleContext(GraphQueriesParser.Where_exprContext,0)


        def getRuleIndex(self):
            return GraphQueriesParser.RULE_select_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSelect_stmt" ):
                listener.enterSelect_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSelect_stmt" ):
                listener.exitSelect_stmt(self)




    def select_stmt(self):

        localctx = GraphQueriesParser.Select_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_select_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self.match(GraphQueriesParser.KW_SELECT)
            self.state = 47
            self.func()
            self.state = 48
            self.match(GraphQueriesParser.KW_FROM)
            self.state = 49
            self.match(GraphQueriesParser.STRING)
            self.state = 50
            self.match(GraphQueriesParser.KW_WHERE)
            self.state = 51
            self.where_expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_GET(self):
            return self.getToken(GraphQueriesParser.KW_GET, 0)

        def KW_COUNT(self):
            return self.getToken(GraphQueriesParser.KW_COUNT, 0)

        def KW_EXISTS(self):
            return self.getToken(GraphQueriesParser.KW_EXISTS, 0)

        def getRuleIndex(self):
            return GraphQueriesParser.RULE_func

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunc" ):
                listener.enterFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunc" ):
                listener.exitFunc(self)




    def func(self):

        localctx = GraphQueriesParser.FuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_func)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << GraphQueriesParser.KW_GET) | (1 << GraphQueriesParser.KW_COUNT) | (1 << GraphQueriesParser.KW_EXISTS))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Where_exprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBR(self, i:int=None):
            if i is None:
                return self.getTokens(GraphQueriesParser.LBR)
            else:
                return self.getToken(GraphQueriesParser.LBR, i)

        def v_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GraphQueriesParser.V_exprContext)
            else:
                return self.getTypedRuleContext(GraphQueriesParser.V_exprContext,i)


        def RBR(self, i:int=None):
            if i is None:
                return self.getTokens(GraphQueriesParser.RBR)
            else:
                return self.getToken(GraphQueriesParser.RBR, i)

        def OP_MINUS(self, i:int=None):
            if i is None:
                return self.getTokens(GraphQueriesParser.OP_MINUS)
            else:
                return self.getToken(GraphQueriesParser.OP_MINUS, i)

        def pattern(self):
            return self.getTypedRuleContext(GraphQueriesParser.PatternContext,0)


        def OP_GR(self):
            return self.getToken(GraphQueriesParser.OP_GR, 0)

        def getRuleIndex(self):
            return GraphQueriesParser.RULE_where_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhere_expr" ):
                listener.enterWhere_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhere_expr" ):
                listener.exitWhere_expr(self)




    def where_expr(self):

        localctx = GraphQueriesParser.Where_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_where_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self.match(GraphQueriesParser.LBR)
            self.state = 56
            self.v_expr()
            self.state = 57
            self.match(GraphQueriesParser.RBR)
            self.state = 58
            self.match(GraphQueriesParser.OP_MINUS)
            self.state = 59
            self.pattern()
            self.state = 60
            self.match(GraphQueriesParser.OP_MINUS)
            self.state = 61
            self.match(GraphQueriesParser.OP_GR)
            self.state = 62
            self.match(GraphQueriesParser.LBR)
            self.state = 63
            self.v_expr()
            self.state = 64
            self.match(GraphQueriesParser.RBR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class V_exprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(GraphQueriesParser.INT, 0)

        def UNDERSCORE(self):
            return self.getToken(GraphQueriesParser.UNDERSCORE, 0)

        def getRuleIndex(self):
            return GraphQueriesParser.RULE_v_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterV_expr" ):
                listener.enterV_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitV_expr" ):
                listener.exitV_expr(self)




    def v_expr(self):

        localctx = GraphQueriesParser.V_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_v_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            _la = self._input.LA(1)
            if not(_la==GraphQueriesParser.UNDERSCORE or _la==GraphQueriesParser.INT):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PatternContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elem(self):
            return self.getTypedRuleContext(GraphQueriesParser.ElemContext,0)


        def MID(self):
            return self.getToken(GraphQueriesParser.MID, 0)

        def pattern(self):
            return self.getTypedRuleContext(GraphQueriesParser.PatternContext,0)


        def getRuleIndex(self):
            return GraphQueriesParser.RULE_pattern

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPattern" ):
                listener.enterPattern(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPattern" ):
                listener.exitPattern(self)




    def pattern(self):

        localctx = GraphQueriesParser.PatternContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_pattern)
        try:
            self.state = 73
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 68
                self.elem()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 69
                self.elem()
                self.state = 70
                self.match(GraphQueriesParser.MID)
                self.state = 71
                self.pattern()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElemContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def seq(self):
            return self.getTypedRuleContext(GraphQueriesParser.SeqContext,0)


        def LBR(self):
            return self.getToken(GraphQueriesParser.LBR, 0)

        def RBR(self):
            return self.getToken(GraphQueriesParser.RBR, 0)

        def getRuleIndex(self):
            return GraphQueriesParser.RULE_elem

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElem" ):
                listener.enterElem(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElem" ):
                listener.exitElem(self)




    def elem(self):

        localctx = GraphQueriesParser.ElemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_elem)
        try:
            self.state = 78
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 75
                self.seq()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 76
                self.match(GraphQueriesParser.LBR)
                self.state = 77
                self.match(GraphQueriesParser.RBR)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SeqContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def seq_elem(self):
            return self.getTypedRuleContext(GraphQueriesParser.Seq_elemContext,0)


        def seq(self):
            return self.getTypedRuleContext(GraphQueriesParser.SeqContext,0)


        def getRuleIndex(self):
            return GraphQueriesParser.RULE_seq

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSeq" ):
                listener.enterSeq(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSeq" ):
                listener.exitSeq(self)




    def seq(self):

        localctx = GraphQueriesParser.SeqContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_seq)
        try:
            self.state = 84
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 80
                self.seq_elem()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 81
                self.seq_elem()
                self.state = 82
                self.seq()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Seq_elemContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def prim_pattern(self):
            return self.getTypedRuleContext(GraphQueriesParser.Prim_patternContext,0)


        def OP_STAR(self):
            return self.getToken(GraphQueriesParser.OP_STAR, 0)

        def getRuleIndex(self):
            return GraphQueriesParser.RULE_seq_elem

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSeq_elem" ):
                listener.enterSeq_elem(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSeq_elem" ):
                listener.exitSeq_elem(self)




    def seq_elem(self):

        localctx = GraphQueriesParser.Seq_elemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_seq_elem)
        try:
            self.state = 90
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 86
                self.prim_pattern()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 87
                self.prim_pattern()
                self.state = 88
                self.match(GraphQueriesParser.OP_STAR)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Prim_patternContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SYMB(self):
            return self.getToken(GraphQueriesParser.SYMB, 0)

        def NT_NAME(self):
            return self.getToken(GraphQueriesParser.NT_NAME, 0)

        def LBR(self):
            return self.getToken(GraphQueriesParser.LBR, 0)

        def pattern(self):
            return self.getTypedRuleContext(GraphQueriesParser.PatternContext,0)


        def RBR(self):
            return self.getToken(GraphQueriesParser.RBR, 0)

        def getRuleIndex(self):
            return GraphQueriesParser.RULE_prim_pattern

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrim_pattern" ):
                listener.enterPrim_pattern(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrim_pattern" ):
                listener.exitPrim_pattern(self)




    def prim_pattern(self):

        localctx = GraphQueriesParser.Prim_patternContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_prim_pattern)
        try:
            self.state = 98
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [GraphQueriesParser.SYMB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 92
                self.match(GraphQueriesParser.SYMB)
                pass
            elif token in [GraphQueriesParser.NT_NAME]:
                self.enterOuterAlt(localctx, 2)
                self.state = 93
                self.match(GraphQueriesParser.NT_NAME)
                pass
            elif token in [GraphQueriesParser.LBR]:
                self.enterOuterAlt(localctx, 3)
                self.state = 94
                self.match(GraphQueriesParser.LBR)
                self.state = 95
                self.pattern()
                self.state = 96
                self.match(GraphQueriesParser.RBR)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





