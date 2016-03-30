# Generated from D:/Python/Compiler\Grammar.g4 by ANTLR 4.5.1
# encoding: utf-8
from antlr4 import *
from io import StringIO


from entity.Program import Program
from entity.Variable import Variable
from entity.Function import *
from entity.Expression import *
from entity.Type import Type
from entity.Scalar import *
from entity.Statement import *

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3\"")
        buf.write("\u010c\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\3\2\3\2\3\2\7\2,\n\2\f\2\16\2/\13\2\3\2\3\2")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\5\39\n\3\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4G\n\4\3\5\3\5\3\5\3\5")
        buf.write("\5\5M\n\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\7\6W\n\6\f\6")
        buf.write("\16\6Z\13\6\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\7\bd\n\b\f")
        buf.write("\b\16\bg\13\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\5\tq\n\t")
        buf.write("\3\n\3\n\3\n\3\n\3\n\3\n\3\n\5\nz\n\n\3\n\3\n\3\n\3\n")
        buf.write("\3\n\3\n\3\n\3\n\3\n\3\n\3\n\5\n\u0087\n\n\3\n\3\n\3\n")
        buf.write("\3\n\3\n\3\n\5\n\u008f\n\n\3\13\3\13\3\13\3\13\7\13\u0095")
        buf.write("\n\13\f\13\16\13\u0098\13\13\3\13\3\13\3\f\3\f\3\f\3\f")
        buf.write("\3\f\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3")
        buf.write("\17\3\17\5\17\u00ad\n\17\3\20\3\20\3\20\3\20\3\20\5\20")
        buf.write("\u00b4\n\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3")
        buf.write("\21\3\21\5\21\u00c0\n\21\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\5\21\u00ea\n\21\3\21\3\21\7\21\u00ee\n\21\f\21\16")
        buf.write("\21\u00f1\13\21\3\22\3\22\3\22\3\22\3\22\3\22\7\22\u00f9")
        buf.write("\n\22\f\22\16\22\u00fc\13\22\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\5\23\u0108\n\23\3\24\3\24\3")
        buf.write("\24\2\3 \25\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"")
        buf.write("$&\2\7\3\2\21\22\3\2\23\25\3\2\26\31\3\2\32\33\3\2\37")
        buf.write(" \u0114\2-\3\2\2\2\48\3\2\2\2\6F\3\2\2\2\bH\3\2\2\2\n")
        buf.write("P\3\2\2\2\f[\3\2\2\2\16_\3\2\2\2\20p\3\2\2\2\22\u008e")
        buf.write("\3\2\2\2\24\u0090\3\2\2\2\26\u009b\3\2\2\2\30\u00a0\3")
        buf.write("\2\2\2\32\u00a3\3\2\2\2\34\u00ac\3\2\2\2\36\u00ae\3\2")
        buf.write("\2\2 \u00bf\3\2\2\2\"\u00f2\3\2\2\2$\u0107\3\2\2\2&\u0109")
        buf.write("\3\2\2\2()\5\4\3\2)*\b\2\1\2*,\3\2\2\2+(\3\2\2\2,/\3\2")
        buf.write("\2\2-+\3\2\2\2-.\3\2\2\2.\60\3\2\2\2/-\3\2\2\2\60\61\7")
        buf.write("\2\2\3\61\3\3\2\2\2\62\63\5\6\4\2\63\64\b\3\1\2\649\3")
        buf.write("\2\2\2\65\66\5\32\16\2\66\67\b\3\1\2\679\3\2\2\28\62\3")
        buf.write("\2\2\28\65\3\2\2\29\5\3\2\2\2:;\5\34\17\2;<\7\36\2\2<")
        buf.write("=\5\b\5\2=>\5\16\b\2>?\b\4\1\2?G\3\2\2\2@A\7\3\2\2AB\7")
        buf.write("\36\2\2BC\5\b\5\2CD\5\16\b\2DE\b\4\1\2EG\3\2\2\2F:\3\2")
        buf.write("\2\2F@\3\2\2\2G\7\3\2\2\2HL\7\4\2\2IJ\5\n\6\2JK\b\5\1")
        buf.write("\2KM\3\2\2\2LI\3\2\2\2LM\3\2\2\2MN\3\2\2\2NO\7\5\2\2O")
        buf.write("\t\3\2\2\2PQ\5\f\7\2QX\b\6\1\2RS\7\6\2\2ST\5\f\7\2TU\b")
        buf.write("\6\1\2UW\3\2\2\2VR\3\2\2\2WZ\3\2\2\2XV\3\2\2\2XY\3\2\2")
        buf.write("\2Y\13\3\2\2\2ZX\3\2\2\2[\\\5\34\17\2\\]\7\36\2\2]^\b")
        buf.write("\7\1\2^\r\3\2\2\2_e\7\7\2\2`a\5\20\t\2ab\b\b\1\2bd\3\2")
        buf.write("\2\2c`\3\2\2\2dg\3\2\2\2ec\3\2\2\2ef\3\2\2\2fh\3\2\2\2")
        buf.write("ge\3\2\2\2hi\7\b\2\2i\17\3\2\2\2jk\5\32\16\2kl\b\t\1\2")
        buf.write("lq\3\2\2\2mn\5\22\n\2no\b\t\1\2oq\3\2\2\2pj\3\2\2\2pm")
        buf.write("\3\2\2\2q\21\3\2\2\2rs\7\t\2\2st\5\26\f\2ty\5\24\13\2")
        buf.write("uv\7\n\2\2vw\5\24\13\2wx\b\n\1\2xz\3\2\2\2yu\3\2\2\2y")
        buf.write("z\3\2\2\2z{\3\2\2\2{|\b\n\1\2|\u008f\3\2\2\2}~\7\13\2")
        buf.write("\2~\177\5\26\f\2\177\u0080\5\24\13\2\u0080\u0081\b\n\1")
        buf.write("\2\u0081\u008f\3\2\2\2\u0082\u0086\7\f\2\2\u0083\u0084")
        buf.write("\5 \21\2\u0084\u0085\b\n\1\2\u0085\u0087\3\2\2\2\u0086")
        buf.write("\u0083\3\2\2\2\u0086\u0087\3\2\2\2\u0087\u0088\3\2\2\2")
        buf.write("\u0088\u0089\7\r\2\2\u0089\u008f\b\n\1\2\u008a\u008b\5")
        buf.write("\30\r\2\u008b\u008c\7\r\2\2\u008c\u008d\b\n\1\2\u008d")
        buf.write("\u008f\3\2\2\2\u008er\3\2\2\2\u008e}\3\2\2\2\u008e\u0082")
        buf.write("\3\2\2\2\u008e\u008a\3\2\2\2\u008f\23\3\2\2\2\u0090\u0096")
        buf.write("\7\7\2\2\u0091\u0092\5\20\t\2\u0092\u0093\b\13\1\2\u0093")
        buf.write("\u0095\3\2\2\2\u0094\u0091\3\2\2\2\u0095\u0098\3\2\2\2")
        buf.write("\u0096\u0094\3\2\2\2\u0096\u0097\3\2\2\2\u0097\u0099\3")
        buf.write("\2\2\2\u0098\u0096\3\2\2\2\u0099\u009a\7\b\2\2\u009a\25")
        buf.write("\3\2\2\2\u009b\u009c\7\4\2\2\u009c\u009d\5 \21\2\u009d")
        buf.write("\u009e\7\5\2\2\u009e\u009f\b\f\1\2\u009f\27\3\2\2\2\u00a0")
        buf.write("\u00a1\5 \21\2\u00a1\u00a2\b\r\1\2\u00a2\31\3\2\2\2\u00a3")
        buf.write("\u00a4\5\34\17\2\u00a4\u00a5\5\36\20\2\u00a5\u00a6\7\r")
        buf.write("\2\2\u00a6\u00a7\b\16\1\2\u00a7\33\3\2\2\2\u00a8\u00a9")
        buf.write("\7\16\2\2\u00a9\u00ad\b\17\1\2\u00aa\u00ab\7\17\2\2\u00ab")
        buf.write("\u00ad\b\17\1\2\u00ac\u00a8\3\2\2\2\u00ac\u00aa\3\2\2")
        buf.write("\2\u00ad\35\3\2\2\2\u00ae\u00b3\7\36\2\2\u00af\u00b0\7")
        buf.write("\20\2\2\u00b0\u00b1\5 \21\2\u00b1\u00b2\b\20\1\2\u00b2")
        buf.write("\u00b4\3\2\2\2\u00b3\u00af\3\2\2\2\u00b3\u00b4\3\2\2\2")
        buf.write("\u00b4\u00b5\3\2\2\2\u00b5\u00b6\b\20\1\2\u00b6\37\3\2")
        buf.write("\2\2\u00b7\u00b8\b\21\1\2\u00b8\u00b9\t\2\2\2\u00b9\u00ba")
        buf.write("\5 \21\n\u00ba\u00bb\b\21\1\2\u00bb\u00c0\3\2\2\2\u00bc")
        buf.write("\u00bd\5$\23\2\u00bd\u00be\b\21\1\2\u00be\u00c0\3\2\2")
        buf.write("\2\u00bf\u00b7\3\2\2\2\u00bf\u00bc\3\2\2\2\u00c0\u00ef")
        buf.write("\3\2\2\2\u00c1\u00c2\f\t\2\2\u00c2\u00c3\t\3\2\2\u00c3")
        buf.write("\u00c4\5 \21\n\u00c4\u00c5\b\21\1\2\u00c5\u00ee\3\2\2")
        buf.write("\2\u00c6\u00c7\f\b\2\2\u00c7\u00c8\t\2\2\2\u00c8\u00c9")
        buf.write("\5 \21\t\u00c9\u00ca\b\21\1\2\u00ca\u00ee\3\2\2\2\u00cb")
        buf.write("\u00cc\f\7\2\2\u00cc\u00cd\t\4\2\2\u00cd\u00ce\5 \21\b")
        buf.write("\u00ce\u00cf\b\21\1\2\u00cf\u00ee\3\2\2\2\u00d0\u00d1")
        buf.write("\f\6\2\2\u00d1\u00d2\t\5\2\2\u00d2\u00d3\5 \21\7\u00d3")
        buf.write("\u00d4\b\21\1\2\u00d4\u00ee\3\2\2\2\u00d5\u00d6\f\5\2")
        buf.write("\2\u00d6\u00d7\7\34\2\2\u00d7\u00d8\5 \21\6\u00d8\u00d9")
        buf.write("\b\21\1\2\u00d9\u00ee\3\2\2\2\u00da\u00db\f\4\2\2\u00db")
        buf.write("\u00dc\7\35\2\2\u00dc\u00dd\5 \21\5\u00dd\u00de\b\21\1")
        buf.write("\2\u00de\u00ee\3\2\2\2\u00df\u00e0\f\3\2\2\u00e0\u00e1")
        buf.write("\7\20\2\2\u00e1\u00e2\5 \21\3\u00e2\u00e3\b\21\1\2\u00e3")
        buf.write("\u00ee\3\2\2\2\u00e4\u00e5\f\13\2\2\u00e5\u00e9\7\4\2")
        buf.write("\2\u00e6\u00e7\5\"\22\2\u00e7\u00e8\b\21\1\2\u00e8\u00ea")
        buf.write("\3\2\2\2\u00e9\u00e6\3\2\2\2\u00e9\u00ea\3\2\2\2\u00ea")
        buf.write("\u00eb\3\2\2\2\u00eb\u00ec\7\5\2\2\u00ec\u00ee\b\21\1")
        buf.write("\2\u00ed\u00c1\3\2\2\2\u00ed\u00c6\3\2\2\2\u00ed\u00cb")
        buf.write("\3\2\2\2\u00ed\u00d0\3\2\2\2\u00ed\u00d5\3\2\2\2\u00ed")
        buf.write("\u00da\3\2\2\2\u00ed\u00df\3\2\2\2\u00ed\u00e4\3\2\2\2")
        buf.write("\u00ee\u00f1\3\2\2\2\u00ef\u00ed\3\2\2\2\u00ef\u00f0\3")
        buf.write("\2\2\2\u00f0!\3\2\2\2\u00f1\u00ef\3\2\2\2\u00f2\u00f3")
        buf.write("\5 \21\2\u00f3\u00fa\b\22\1\2\u00f4\u00f5\7\6\2\2\u00f5")
        buf.write("\u00f6\5 \21\2\u00f6\u00f7\b\22\1\2\u00f7\u00f9\3\2\2")
        buf.write("\2\u00f8\u00f4\3\2\2\2\u00f9\u00fc\3\2\2\2\u00fa\u00f8")
        buf.write("\3\2\2\2\u00fa\u00fb\3\2\2\2\u00fb#\3\2\2\2\u00fc\u00fa")
        buf.write("\3\2\2\2\u00fd\u00fe\7\4\2\2\u00fe\u00ff\5 \21\2\u00ff")
        buf.write("\u0100\7\5\2\2\u0100\u0101\b\23\1\2\u0101\u0108\3\2\2")
        buf.write("\2\u0102\u0103\5&\24\2\u0103\u0104\b\23\1\2\u0104\u0108")
        buf.write("\3\2\2\2\u0105\u0106\7\36\2\2\u0106\u0108\b\23\1\2\u0107")
        buf.write("\u00fd\3\2\2\2\u0107\u0102\3\2\2\2\u0107\u0105\3\2\2\2")
        buf.write("\u0108%\3\2\2\2\u0109\u010a\t\6\2\2\u010a\'\3\2\2\2\25")
        buf.write("-8FLXepy\u0086\u008e\u0096\u00ac\u00b3\u00bf\u00e9\u00ed")
        buf.write("\u00ef\u00fa\u0107")
        return buf.getvalue()


class GrammarParser ( Parser ):

    grammarFileName = "Grammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'void'", "'('", "')'", "','", "'{'", 
                     "'}'", "'if'", "'else'", "'while'", "'return'", "';'", 
                     "'boolean'", "'int'", "'='", "'+'", "'-'", "'*'", "'/'", 
                     "'%'", "'<='", "'>='", "'>'", "'<'", "'=='", "'!='", 
                     "'&&'", "'||'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "Identifier", "IntegerLiteral", "BooleanLiteral", 
                      "WS", "COMMENT" ]

    RULE_program = 0
    RULE_programElement = 1
    RULE_functionDeclaration = 2
    RULE_formalParameters = 3
    RULE_formalParameterList = 4
    RULE_formalParameter = 5
    RULE_block = 6
    RULE_blockStatement = 7
    RULE_statement = 8
    RULE_brackedStatement = 9
    RULE_parExpression = 10
    RULE_callFunction = 11
    RULE_variableDeclaration = 12
    RULE_valueType = 13
    RULE_variableDeclarator = 14
    RULE_expression = 15
    RULE_expressionList = 16
    RULE_primary = 17
    RULE_literal = 18

    ruleNames =  [ "program", "programElement", "functionDeclaration", "formalParameters", 
                   "formalParameterList", "formalParameter", "block", "blockStatement", 
                   "statement", "brackedStatement", "parExpression", "callFunction", 
                   "variableDeclaration", "valueType", "variableDeclarator", 
                   "expression", "expressionList", "primary", "literal" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    Identifier=28
    IntegerLiteral=29
    BooleanLiteral=30
    WS=31
    COMMENT=32

    def __init__(self, input:TokenStream):
        super().__init__(input)
        self.checkVersion("4.5.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



        self.program_states = Program()


    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._programElement = None # ProgramElementContext

        def EOF(self):
            return self.getToken(GrammarParser.EOF, 0)

        def programElement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.ProgramElementContext)
            else:
                return self.getTypedRuleContext(GrammarParser.ProgramElementContext,i)


        def getRuleIndex(self):
            return GrammarParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = GrammarParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << GrammarParser.T__0) | (1 << GrammarParser.T__11) | (1 << GrammarParser.T__12))) != 0):
                self.state = 38
                localctx._programElement = self.programElement()
                self.program_states.add(localctx._programElement.element)
                self.state = 45
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 46
            self.match(GrammarParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ProgramElementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.element =  None
            self._functionDeclaration = None # FunctionDeclarationContext
            self._variableDeclaration = None # VariableDeclarationContext

        def functionDeclaration(self):
            return self.getTypedRuleContext(GrammarParser.FunctionDeclarationContext,0)


        def variableDeclaration(self):
            return self.getTypedRuleContext(GrammarParser.VariableDeclarationContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_programElement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgramElement" ):
                listener.enterProgramElement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgramElement" ):
                listener.exitProgramElement(self)




    def programElement(self):

        localctx = GrammarParser.ProgramElementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_programElement)
        try:
            self.state = 54
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 48
                localctx._functionDeclaration = self.functionDeclaration()
                localctx.element = localctx._functionDeclaration.function
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 51
                localctx._variableDeclaration = self.variableDeclaration()
                localctx.element = localctx._variableDeclaration.variable
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FunctionDeclarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.function =  None
            self._valueType = None # ValueTypeContext
            self._Identifier = None # Token
            self._formalParameters = None # FormalParametersContext
            self._block = None # BlockContext

        def valueType(self):
            return self.getTypedRuleContext(GrammarParser.ValueTypeContext,0)


        def Identifier(self):
            return self.getToken(GrammarParser.Identifier, 0)

        def formalParameters(self):
            return self.getTypedRuleContext(GrammarParser.FormalParametersContext,0)


        def block(self):
            return self.getTypedRuleContext(GrammarParser.BlockContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_functionDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionDeclaration" ):
                listener.enterFunctionDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionDeclaration" ):
                listener.exitFunctionDeclaration(self)




    def functionDeclaration(self):

        localctx = GrammarParser.FunctionDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_functionDeclaration)
        try:
            self.state = 68
            token = self._input.LA(1)
            if token in [GrammarParser.T__11, GrammarParser.T__12]:
                self.enterOuterAlt(localctx, 1)
                self.state = 56
                localctx._valueType = self.valueType()
                self.state = 57
                localctx._Identifier = self.match(GrammarParser.Identifier)
                self.state = 58
                localctx._formalParameters = self.formalParameters()
                self.state = 59
                localctx._block = self.block()
                localctx.function = get_function(localctx._valueType.value_type, (None if localctx._Identifier is None else localctx._Identifier.text), localctx._formalParameters.params, localctx._block.statements)

            elif token in [GrammarParser.T__0]:
                self.enterOuterAlt(localctx, 2)
                self.state = 62
                self.match(GrammarParser.T__0)
                self.state = 63
                localctx._Identifier = self.match(GrammarParser.Identifier)
                self.state = 64
                localctx._formalParameters = self.formalParameters()
                self.state = 65
                localctx._block = self.block()
                localctx.function = get_function(None, (None if localctx._Identifier is None else localctx._Identifier.text), localctx._formalParameters.params, localctx._block.statements)

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FormalParametersContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.params =  None
            self._formalParameterList = None # FormalParameterListContext

        def formalParameterList(self):
            return self.getTypedRuleContext(GrammarParser.FormalParameterListContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_formalParameters

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFormalParameters" ):
                listener.enterFormalParameters(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFormalParameters" ):
                listener.exitFormalParameters(self)




    def formalParameters(self):

        localctx = GrammarParser.FormalParametersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_formalParameters)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self.match(GrammarParser.T__1)
            self.state = 74
            _la = self._input.LA(1)
            if _la==GrammarParser.T__11 or _la==GrammarParser.T__12:
                self.state = 71
                localctx._formalParameterList = self.formalParameterList()
                localctx.params = localctx._formalParameterList.params


            self.state = 76
            self.match(GrammarParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FormalParameterListContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.params =  None
            self._formalParameter = None # FormalParameterContext

        def formalParameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.FormalParameterContext)
            else:
                return self.getTypedRuleContext(GrammarParser.FormalParameterContext,i)


        def getRuleIndex(self):
            return GrammarParser.RULE_formalParameterList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFormalParameterList" ):
                listener.enterFormalParameterList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFormalParameterList" ):
                listener.exitFormalParameterList(self)




    def formalParameterList(self):

        localctx = GrammarParser.FormalParameterListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_formalParameterList)
        localctx.params = []
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            localctx._formalParameter = self.formalParameter()
            localctx.params.append(localctx._formalParameter.variable)
            self.state = 86
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==GrammarParser.T__3:
                self.state = 80
                self.match(GrammarParser.T__3)
                self.state = 81
                localctx._formalParameter = self.formalParameter()
                localctx.params.append(localctx._formalParameter.variable)
                self.state = 88
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FormalParameterContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.variable =  None
            self._valueType = None # ValueTypeContext
            self._Identifier = None # Token

        def valueType(self):
            return self.getTypedRuleContext(GrammarParser.ValueTypeContext,0)


        def Identifier(self):
            return self.getToken(GrammarParser.Identifier, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_formalParameter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFormalParameter" ):
                listener.enterFormalParameter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFormalParameter" ):
                listener.exitFormalParameter(self)




    def formalParameter(self):

        localctx = GrammarParser.FormalParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_formalParameter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            localctx._valueType = self.valueType()
            self.state = 90
            localctx._Identifier = self.match(GrammarParser.Identifier)
            localctx.variable = Variable(localctx._valueType.value_type, (None if localctx._Identifier is None else localctx._Identifier.text))
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BlockContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.statements =  None
            self._blockStatement = None # BlockStatementContext

        def blockStatement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.BlockStatementContext)
            else:
                return self.getTypedRuleContext(GrammarParser.BlockStatementContext,i)


        def getRuleIndex(self):
            return GrammarParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)




    def block(self):

        localctx = GrammarParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_block)
        localctx.statements = []
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self.match(GrammarParser.T__4)
            self.state = 99
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << GrammarParser.T__1) | (1 << GrammarParser.T__6) | (1 << GrammarParser.T__8) | (1 << GrammarParser.T__9) | (1 << GrammarParser.T__11) | (1 << GrammarParser.T__12) | (1 << GrammarParser.T__14) | (1 << GrammarParser.T__15) | (1 << GrammarParser.Identifier) | (1 << GrammarParser.IntegerLiteral) | (1 << GrammarParser.BooleanLiteral))) != 0):
                self.state = 94
                localctx._blockStatement = self.blockStatement()
                localctx.statements.append(localctx._blockStatement.state)
                self.state = 101
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 102
            self.match(GrammarParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BlockStatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.state =  None
            self._variableDeclaration = None # VariableDeclarationContext
            self._statement = None # StatementContext

        def variableDeclaration(self):
            return self.getTypedRuleContext(GrammarParser.VariableDeclarationContext,0)


        def statement(self):
            return self.getTypedRuleContext(GrammarParser.StatementContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_blockStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlockStatement" ):
                listener.enterBlockStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlockStatement" ):
                listener.exitBlockStatement(self)




    def blockStatement(self):

        localctx = GrammarParser.BlockStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_blockStatement)
        try:
            self.state = 110
            token = self._input.LA(1)
            if token in [GrammarParser.T__11, GrammarParser.T__12]:
                self.enterOuterAlt(localctx, 1)
                self.state = 104
                localctx._variableDeclaration = self.variableDeclaration()
                localctx.state = localctx._variableDeclaration.variable

            elif token in [GrammarParser.T__1, GrammarParser.T__6, GrammarParser.T__8, GrammarParser.T__9, GrammarParser.T__14, GrammarParser.T__15, GrammarParser.Identifier, GrammarParser.IntegerLiteral, GrammarParser.BooleanLiteral]:
                self.enterOuterAlt(localctx, 2)
                self.state = 107
                localctx._statement = self.statement()
                localctx.state = localctx._statement.state

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.state =  None
            self._parExpression = None # ParExpressionContext
            self._brackedStatement = None # BrackedStatementContext
            self._expression = None # ExpressionContext
            self._callFunction = None # CallFunctionContext

        def parExpression(self):
            return self.getTypedRuleContext(GrammarParser.ParExpressionContext,0)


        def brackedStatement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.BrackedStatementContext)
            else:
                return self.getTypedRuleContext(GrammarParser.BrackedStatementContext,i)


        def expression(self):
            return self.getTypedRuleContext(GrammarParser.ExpressionContext,0)


        def callFunction(self):
            return self.getTypedRuleContext(GrammarParser.CallFunctionContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = GrammarParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_statement)
        tmp_var = None
        self._la = 0 # Token type
        try:
            self.state = 140
            token = self._input.LA(1)
            if token in [GrammarParser.T__6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 112
                self.match(GrammarParser.T__6)
                self.state = 113
                localctx._parExpression = self.parExpression()
                self.state = 114
                localctx._brackedStatement = self.brackedStatement()
                self.state = 119
                _la = self._input.LA(1)
                if _la==GrammarParser.T__7:
                    self.state = 115
                    self.match(GrammarParser.T__7)
                    self.state = 116
                    localctx._brackedStatement = self.brackedStatement()
                    tmp_var = ElseStatement(localctx._brackedStatement.statements)


                localctx.state = IfStatement(localctx._parExpression.expr, localctx._brackedStatement.statements, tmp_var)

            elif token in [GrammarParser.T__8]:
                self.enterOuterAlt(localctx, 2)
                self.state = 123
                self.match(GrammarParser.T__8)
                self.state = 124
                localctx._parExpression = self.parExpression()
                self.state = 125
                localctx._brackedStatement = self.brackedStatement()
                localctx.state = WhileStatement(localctx._parExpression.expr, localctx._brackedStatement.statements)

            elif token in [GrammarParser.T__9]:
                self.enterOuterAlt(localctx, 3)
                self.state = 128
                self.match(GrammarParser.T__9)
                self.state = 132
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << GrammarParser.T__1) | (1 << GrammarParser.T__14) | (1 << GrammarParser.T__15) | (1 << GrammarParser.Identifier) | (1 << GrammarParser.IntegerLiteral) | (1 << GrammarParser.BooleanLiteral))) != 0):
                    self.state = 129
                    localctx._expression = self.expression(0)
                    tmp_var = localctx._expression.expr


                self.state = 134
                self.match(GrammarParser.T__10)
                localctx.state = ReturnStatement(tmp_var)

            elif token in [GrammarParser.T__1, GrammarParser.T__14, GrammarParser.T__15, GrammarParser.Identifier, GrammarParser.IntegerLiteral, GrammarParser.BooleanLiteral]:
                self.enterOuterAlt(localctx, 4)
                self.state = 136
                localctx._callFunction = self.callFunction()
                self.state = 137
                self.match(GrammarParser.T__10)
                localctx.state = localctx._callFunction.expr

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BrackedStatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.statements =  None
            self._blockStatement = None # BlockStatementContext

        def blockStatement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.BlockStatementContext)
            else:
                return self.getTypedRuleContext(GrammarParser.BlockStatementContext,i)


        def getRuleIndex(self):
            return GrammarParser.RULE_brackedStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBrackedStatement" ):
                listener.enterBrackedStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBrackedStatement" ):
                listener.exitBrackedStatement(self)




    def brackedStatement(self):

        localctx = GrammarParser.BrackedStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_brackedStatement)
        localctx.statements = []
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 142
            self.match(GrammarParser.T__4)
            self.state = 148
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << GrammarParser.T__1) | (1 << GrammarParser.T__6) | (1 << GrammarParser.T__8) | (1 << GrammarParser.T__9) | (1 << GrammarParser.T__11) | (1 << GrammarParser.T__12) | (1 << GrammarParser.T__14) | (1 << GrammarParser.T__15) | (1 << GrammarParser.Identifier) | (1 << GrammarParser.IntegerLiteral) | (1 << GrammarParser.BooleanLiteral))) != 0):
                self.state = 143
                localctx._blockStatement = self.blockStatement()
                localctx.statements.append(localctx._blockStatement.state)
                self.state = 150
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 151
            self.match(GrammarParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ParExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.expr =  None
            self._expression = None # ExpressionContext

        def expression(self):
            return self.getTypedRuleContext(GrammarParser.ExpressionContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_parExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParExpression" ):
                listener.enterParExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParExpression" ):
                listener.exitParExpression(self)




    def parExpression(self):

        localctx = GrammarParser.ParExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_parExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            self.match(GrammarParser.T__1)
            self.state = 154
            localctx._expression = self.expression(0)
            self.state = 155
            self.match(GrammarParser.T__2)
            localctx.expr = localctx._expression.expr
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CallFunctionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.expr =  None
            self._expression = None # ExpressionContext

        def expression(self):
            return self.getTypedRuleContext(GrammarParser.ExpressionContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_callFunction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCallFunction" ):
                listener.enterCallFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCallFunction" ):
                listener.exitCallFunction(self)




    def callFunction(self):

        localctx = GrammarParser.CallFunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_callFunction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 158
            localctx._expression = self.expression(0)
            localctx.expr = localctx._expression.expr
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class VariableDeclarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.variable =  None
            self._valueType = None # ValueTypeContext
            self._variableDeclarator = None # VariableDeclaratorContext

        def valueType(self):
            return self.getTypedRuleContext(GrammarParser.ValueTypeContext,0)


        def variableDeclarator(self):
            return self.getTypedRuleContext(GrammarParser.VariableDeclaratorContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_variableDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableDeclaration" ):
                listener.enterVariableDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableDeclaration" ):
                listener.exitVariableDeclaration(self)




    def variableDeclaration(self):

        localctx = GrammarParser.VariableDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_variableDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            localctx._valueType = self.valueType()
            self.state = 162
            localctx._variableDeclarator = self.variableDeclarator()
            self.state = 163
            self.match(GrammarParser.T__10)
            localctx.variable = Variable(localctx._valueType.value_type, localctx._variableDeclarator.name_value[0], localctx._variableDeclarator.name_value[1])
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ValueTypeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.value_type =  None


        def getRuleIndex(self):
            return GrammarParser.RULE_valueType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValueType" ):
                listener.enterValueType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValueType" ):
                listener.exitValueType(self)




    def valueType(self):

        localctx = GrammarParser.ValueTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_valueType)
        try:
            self.state = 170
            token = self._input.LA(1)
            if token in [GrammarParser.T__11]:
                self.enterOuterAlt(localctx, 1)
                self.state = 166
                self.match(GrammarParser.T__11)
                localctx.value_type = Type.boolean

            elif token in [GrammarParser.T__12]:
                self.enterOuterAlt(localctx, 2)
                self.state = 168
                self.match(GrammarParser.T__12)
                localctx.value_type = Type.int

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class VariableDeclaratorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.name_value =  None
            self._Identifier = None # Token
            self._expression = None # ExpressionContext

        def Identifier(self):
            return self.getToken(GrammarParser.Identifier, 0)

        def expression(self):
            return self.getTypedRuleContext(GrammarParser.ExpressionContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_variableDeclarator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableDeclarator" ):
                listener.enterVariableDeclarator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableDeclarator" ):
                listener.exitVariableDeclarator(self)




    def variableDeclarator(self):

        localctx = GrammarParser.VariableDeclaratorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_variableDeclarator)
        expr = None
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 172
            localctx._Identifier = self.match(GrammarParser.Identifier)
            self.state = 177
            _la = self._input.LA(1)
            if _la==GrammarParser.T__13:
                self.state = 173
                self.match(GrammarParser.T__13)
                self.state = 174
                localctx._expression = self.expression(0)
                expr = localctx._expression.expr


            localctx.name_value = ((None if localctx._Identifier is None else localctx._Identifier.text), expr)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.expr =  None
            self.e = None # ExpressionContext
            self.e1 = None # ExpressionContext
            self.n = None # ExpressionContext
            self.sign = None # Token
            self._primary = None # PrimaryContext
            self.e2 = None # ExpressionContext
            self._expressionList = None # ExpressionListContext

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(GrammarParser.ExpressionContext,i)


        def primary(self):
            return self.getTypedRuleContext(GrammarParser.PrimaryContext,0)


        def expressionList(self):
            return self.getTypedRuleContext(GrammarParser.ExpressionListContext,0)


        def getRuleIndex(self):
            return GrammarParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = GrammarParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 30
        self.enterRecursionRule(localctx, 30, self.RULE_expression, _p)
        tmp_var = None
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 189
            token = self._input.LA(1)
            if token in [GrammarParser.T__14, GrammarParser.T__15]:
                self.state = 182
                localctx.sign = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==GrammarParser.T__14 or _la==GrammarParser.T__15):
                    localctx.sign = self._errHandler.recoverInline(self)
                else:
                    self.consume()
                self.state = 183
                localctx.e = self.expression(8)
                localctx.expr = get_expression((None if localctx.sign is None else localctx.sign.text), None, localctx.e.expr)

            elif token in [GrammarParser.T__1, GrammarParser.Identifier, GrammarParser.IntegerLiteral, GrammarParser.BooleanLiteral]:
                self.state = 186
                localctx._primary = self.primary()
                localctx.expr = localctx._primary.expr

            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 237
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 235
                    la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
                    if la_ == 1:
                        localctx = GrammarParser.ExpressionContext(self, _parentctx, _parentState)
                        localctx.e1 = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 191
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 192
                        localctx.sign = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << GrammarParser.T__16) | (1 << GrammarParser.T__17) | (1 << GrammarParser.T__18))) != 0)):
                            localctx.sign = self._errHandler.recoverInline(self)
                        else:
                            self.consume()
                        self.state = 193
                        localctx.e2 = self.expression(8)
                        localctx.expr = get_expression((None if localctx.sign is None else localctx.sign.text), localctx.e1.expr, localctx.e2.expr)
                        pass

                    elif la_ == 2:
                        localctx = GrammarParser.ExpressionContext(self, _parentctx, _parentState)
                        localctx.e1 = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 196
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 197
                        localctx.sign = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==GrammarParser.T__14 or _la==GrammarParser.T__15):
                            localctx.sign = self._errHandler.recoverInline(self)
                        else:
                            self.consume()
                        self.state = 198
                        localctx.e2 = self.expression(7)
                        localctx.expr = get_expression((None if localctx.sign is None else localctx.sign.text), localctx.e1.expr, localctx.e2.expr)
                        pass

                    elif la_ == 3:
                        localctx = GrammarParser.ExpressionContext(self, _parentctx, _parentState)
                        localctx.e1 = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 201
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 202
                        localctx.sign = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << GrammarParser.T__19) | (1 << GrammarParser.T__20) | (1 << GrammarParser.T__21) | (1 << GrammarParser.T__22))) != 0)):
                            localctx.sign = self._errHandler.recoverInline(self)
                        else:
                            self.consume()
                        self.state = 203
                        localctx.e2 = self.expression(6)
                        localctx.expr = get_expression((None if localctx.sign is None else localctx.sign.text), localctx.e1.expr, localctx.e2.expr)
                        pass

                    elif la_ == 4:
                        localctx = GrammarParser.ExpressionContext(self, _parentctx, _parentState)
                        localctx.e1 = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 206
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 207
                        localctx.sign = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==GrammarParser.T__23 or _la==GrammarParser.T__24):
                            localctx.sign = self._errHandler.recoverInline(self)
                        else:
                            self.consume()
                        self.state = 208
                        localctx.e2 = self.expression(5)
                        localctx.expr = get_expression((None if localctx.sign is None else localctx.sign.text), localctx.e1.expr, localctx.e2.expr)
                        pass

                    elif la_ == 5:
                        localctx = GrammarParser.ExpressionContext(self, _parentctx, _parentState)
                        localctx.e1 = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 211
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 212
                        localctx.sign = self.match(GrammarParser.T__25)
                        self.state = 213
                        localctx.e2 = self.expression(4)
                        localctx.expr = get_expression((None if localctx.sign is None else localctx.sign.text), localctx.e1.expr, localctx.e2.expr)
                        pass

                    elif la_ == 6:
                        localctx = GrammarParser.ExpressionContext(self, _parentctx, _parentState)
                        localctx.e1 = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 216
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 217
                        localctx.sign = self.match(GrammarParser.T__26)
                        self.state = 218
                        localctx.e2 = self.expression(3)
                        localctx.expr = get_expression((None if localctx.sign is None else localctx.sign.text), localctx.e1.expr, localctx.e2.expr)
                        pass

                    elif la_ == 7:
                        localctx = GrammarParser.ExpressionContext(self, _parentctx, _parentState)
                        localctx.n = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 221
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 222
                        self.match(GrammarParser.T__13)
                        self.state = 223
                        localctx.e = self.expression(1)
                        localctx.expr = AssignmentOperator(localctx.n.expr, localctx.e.expr)
                        pass

                    elif la_ == 8:
                        localctx = GrammarParser.ExpressionContext(self, _parentctx, _parentState)
                        localctx.e = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 226
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 227
                        self.match(GrammarParser.T__1)
                        self.state = 231
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << GrammarParser.T__1) | (1 << GrammarParser.T__14) | (1 << GrammarParser.T__15) | (1 << GrammarParser.Identifier) | (1 << GrammarParser.IntegerLiteral) | (1 << GrammarParser.BooleanLiteral))) != 0):
                            self.state = 228
                            localctx._expressionList = self.expressionList()
                            tmp_var = localctx._expressionList.args


                        self.state = 233
                        self.match(GrammarParser.T__2)
                        localctx.expr = get_call_function_statement((None if localctx.e is None else self._input.getText((localctx.e.start,localctx.e.stop))), tmp_var)
                        pass

             
                self.state = 239
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class ExpressionListContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.args =  None
            self._expression = None # ExpressionContext

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(GrammarParser.ExpressionContext,i)


        def getRuleIndex(self):
            return GrammarParser.RULE_expressionList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionList" ):
                listener.enterExpressionList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionList" ):
                listener.exitExpressionList(self)




    def expressionList(self):

        localctx = GrammarParser.ExpressionListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_expressionList)
        localctx.args = []
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 240
            localctx._expression = self.expression(0)
            localctx.args.append(localctx._expression.expr)
            self.state = 248
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==GrammarParser.T__3:
                self.state = 242
                self.match(GrammarParser.T__3)
                self.state = 243
                localctx._expression = self.expression(0)
                localctx.args.append(localctx._expression.expr)
                self.state = 250
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PrimaryContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.expr =  None
            self._expression = None # ExpressionContext
            self._literal = None # LiteralContext
            self._Identifier = None # Token

        def expression(self):
            return self.getTypedRuleContext(GrammarParser.ExpressionContext,0)


        def literal(self):
            return self.getTypedRuleContext(GrammarParser.LiteralContext,0)


        def Identifier(self):
            return self.getToken(GrammarParser.Identifier, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_primary

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimary" ):
                listener.enterPrimary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimary" ):
                listener.exitPrimary(self)




    def primary(self):

        localctx = GrammarParser.PrimaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_primary)
        try:
            self.state = 261
            token = self._input.LA(1)
            if token in [GrammarParser.T__1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 251
                self.match(GrammarParser.T__1)
                self.state = 252
                localctx._expression = self.expression(0)
                self.state = 253
                self.match(GrammarParser.T__2)
                localctx.expr = localctx._expression.expr

            elif token in [GrammarParser.IntegerLiteral, GrammarParser.BooleanLiteral]:
                self.enterOuterAlt(localctx, 2)
                self.state = 256
                localctx._literal = self.literal()
                localctx.expr = get_scalar((None if localctx._literal is None else self._input.getText((localctx._literal.start,localctx._literal.stop))))

            elif token in [GrammarParser.Identifier]:
                self.enterOuterAlt(localctx, 3)
                self.state = 259
                localctx._Identifier = self.match(GrammarParser.Identifier)
                localctx.expr = get_scalar((None if localctx._Identifier is None else localctx._Identifier.text))

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LiteralContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IntegerLiteral(self):
            return self.getToken(GrammarParser.IntegerLiteral, 0)

        def BooleanLiteral(self):
            return self.getToken(GrammarParser.BooleanLiteral, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral" ):
                listener.enterLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral" ):
                listener.exitLiteral(self)




    def literal(self):

        localctx = GrammarParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 263
            _la = self._input.LA(1)
            if not(_la==GrammarParser.IntegerLiteral or _la==GrammarParser.BooleanLiteral):
                self._errHandler.recoverInline(self)
            else:
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[15] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 1)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 9)
         




