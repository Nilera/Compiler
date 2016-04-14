# Generated from D:/Python/Compiler/grammar\Grammar.g4 by ANTLR 4.5.1
# encoding: utf-8
from antlr4 import *
from io import StringIO


from entity.Program import Program
from entity.Variable import Variable
from entity.Function import *
from entity.Expression import *
from entity.Type import Type
from entity.Array import Array
from entity.Scalar import *
from entity.Statement import *

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3%")
        buf.write("\u0138\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\3\2\3\2\3\2\7\2\60\n\2")
        buf.write("\f\2\16\2\63\13\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\5\3")
        buf.write("=\n\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\5\4K\n\4\3\5\3\5\3\5\3\5\5\5Q\n\5\3\5\3\5\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\6\7\6[\n\6\f\6\16\6^\13\6\3\7\3\7\3\7\3\7\3")
        buf.write("\b\3\b\3\b\3\b\7\bh\n\b\f\b\16\bk\13\b\3\b\3\b\3\t\3\t")
        buf.write("\3\t\3\t\3\t\3\t\5\tu\n\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n")
        buf.write("\5\n~\n\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n")
        buf.write("\5\n\u008b\n\n\3\n\3\n\3\n\3\n\3\n\3\n\5\n\u0093\n\n\3")
        buf.write("\13\3\13\3\13\3\13\7\13\u0099\n\13\f\13\16\13\u009c\13")
        buf.write("\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\7\17\u00b2\n")
        buf.write("\17\f\17\16\17\u00b5\13\17\3\17\3\17\3\20\3\20\3\20\3")
        buf.write("\20\5\20\u00bd\n\20\3\21\3\21\3\21\3\21\3\21\5\21\u00c4")
        buf.write("\n\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\22\5\22\u00d4\n\22\3\22\3\22\3\22\3")
        buf.write("\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\22\6\22\u00ff\n\22\r\22\16\22\u0100")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\22\3\22\5\22\u010a\n\22\3")
        buf.write("\22\3\22\7\22\u010e\n\22\f\22\16\22\u0111\13\22\3\23\3")
        buf.write("\23\3\23\3\23\3\23\3\23\7\23\u0119\n\23\f\23\16\23\u011c")
        buf.write("\13\23\3\24\3\24\3\24\3\24\3\24\3\24\6\24\u0124\n\24\r")
        buf.write("\24\16\24\u0125\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\5\25\u0134\n\25\3\26\3\26\3\26\2")
        buf.write("\3\"\27\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*")
        buf.write("\2\7\3\2\24\25\3\2\26\30\3\2\31\34\3\2\35\36\3\2\"#\u0143")
        buf.write("\2\61\3\2\2\2\4<\3\2\2\2\6J\3\2\2\2\bL\3\2\2\2\nT\3\2")
        buf.write("\2\2\f_\3\2\2\2\16c\3\2\2\2\20t\3\2\2\2\22\u0092\3\2\2")
        buf.write("\2\24\u0094\3\2\2\2\26\u009f\3\2\2\2\30\u00a4\3\2\2\2")
        buf.write("\32\u00a7\3\2\2\2\34\u00ac\3\2\2\2\36\u00bc\3\2\2\2 \u00be")
        buf.write("\3\2\2\2\"\u00d3\3\2\2\2$\u0112\3\2\2\2&\u011d\3\2\2\2")
        buf.write("(\u0133\3\2\2\2*\u0135\3\2\2\2,-\5\4\3\2-.\b\2\1\2.\60")
        buf.write("\3\2\2\2/,\3\2\2\2\60\63\3\2\2\2\61/\3\2\2\2\61\62\3\2")
        buf.write("\2\2\62\64\3\2\2\2\63\61\3\2\2\2\64\65\7\2\2\3\65\3\3")
        buf.write("\2\2\2\66\67\5\6\4\2\678\b\3\1\28=\3\2\2\29:\5\32\16\2")
        buf.write(":;\b\3\1\2;=\3\2\2\2<\66\3\2\2\2<9\3\2\2\2=\5\3\2\2\2")
        buf.write(">?\5\34\17\2?@\7!\2\2@A\5\b\5\2AB\5\16\b\2BC\b\4\1\2C")
        buf.write("K\3\2\2\2DE\7\3\2\2EF\7!\2\2FG\5\b\5\2GH\5\16\b\2HI\b")
        buf.write("\4\1\2IK\3\2\2\2J>\3\2\2\2JD\3\2\2\2K\7\3\2\2\2LP\7\4")
        buf.write("\2\2MN\5\n\6\2NO\b\5\1\2OQ\3\2\2\2PM\3\2\2\2PQ\3\2\2\2")
        buf.write("QR\3\2\2\2RS\7\5\2\2S\t\3\2\2\2TU\5\f\7\2U\\\b\6\1\2V")
        buf.write("W\7\6\2\2WX\5\f\7\2XY\b\6\1\2Y[\3\2\2\2ZV\3\2\2\2[^\3")
        buf.write("\2\2\2\\Z\3\2\2\2\\]\3\2\2\2]\13\3\2\2\2^\\\3\2\2\2_`")
        buf.write("\5\34\17\2`a\7!\2\2ab\b\7\1\2b\r\3\2\2\2ci\7\7\2\2de\5")
        buf.write("\20\t\2ef\b\b\1\2fh\3\2\2\2gd\3\2\2\2hk\3\2\2\2ig\3\2")
        buf.write("\2\2ij\3\2\2\2jl\3\2\2\2ki\3\2\2\2lm\7\b\2\2m\17\3\2\2")
        buf.write("\2no\5\32\16\2op\b\t\1\2pu\3\2\2\2qr\5\22\n\2rs\b\t\1")
        buf.write("\2su\3\2\2\2tn\3\2\2\2tq\3\2\2\2u\21\3\2\2\2vw\7\t\2\2")
        buf.write("wx\5\26\f\2x}\5\24\13\2yz\7\n\2\2z{\5\24\13\2{|\b\n\1")
        buf.write("\2|~\3\2\2\2}y\3\2\2\2}~\3\2\2\2~\177\3\2\2\2\177\u0080")
        buf.write("\b\n\1\2\u0080\u0093\3\2\2\2\u0081\u0082\7\13\2\2\u0082")
        buf.write("\u0083\5\26\f\2\u0083\u0084\5\24\13\2\u0084\u0085\b\n")
        buf.write("\1\2\u0085\u0093\3\2\2\2\u0086\u008a\7\f\2\2\u0087\u0088")
        buf.write("\5\"\22\2\u0088\u0089\b\n\1\2\u0089\u008b\3\2\2\2\u008a")
        buf.write("\u0087\3\2\2\2\u008a\u008b\3\2\2\2\u008b\u008c\3\2\2\2")
        buf.write("\u008c\u008d\7\r\2\2\u008d\u0093\b\n\1\2\u008e\u008f\5")
        buf.write("\30\r\2\u008f\u0090\7\r\2\2\u0090\u0091\b\n\1\2\u0091")
        buf.write("\u0093\3\2\2\2\u0092v\3\2\2\2\u0092\u0081\3\2\2\2\u0092")
        buf.write("\u0086\3\2\2\2\u0092\u008e\3\2\2\2\u0093\23\3\2\2\2\u0094")
        buf.write("\u009a\7\7\2\2\u0095\u0096\5\20\t\2\u0096\u0097\b\13\1")
        buf.write("\2\u0097\u0099\3\2\2\2\u0098\u0095\3\2\2\2\u0099\u009c")
        buf.write("\3\2\2\2\u009a\u0098\3\2\2\2\u009a\u009b\3\2\2\2\u009b")
        buf.write("\u009d\3\2\2\2\u009c\u009a\3\2\2\2\u009d\u009e\7\b\2\2")
        buf.write("\u009e\25\3\2\2\2\u009f\u00a0\7\4\2\2\u00a0\u00a1\5\"")
        buf.write("\22\2\u00a1\u00a2\7\5\2\2\u00a2\u00a3\b\f\1\2\u00a3\27")
        buf.write("\3\2\2\2\u00a4\u00a5\5\"\22\2\u00a5\u00a6\b\r\1\2\u00a6")
        buf.write("\31\3\2\2\2\u00a7\u00a8\5\34\17\2\u00a8\u00a9\5 \21\2")
        buf.write("\u00a9\u00aa\7\r\2\2\u00aa\u00ab\b\16\1\2\u00ab\33\3\2")
        buf.write("\2\2\u00ac\u00b3\5\36\20\2\u00ad\u00ae\7\16\2\2\u00ae")
        buf.write("\u00af\7\17\2\2\u00af\u00b0\3\2\2\2\u00b0\u00b2\b\17\1")
        buf.write("\2\u00b1\u00ad\3\2\2\2\u00b2\u00b5\3\2\2\2\u00b3\u00b1")
        buf.write("\3\2\2\2\u00b3\u00b4\3\2\2\2\u00b4\u00b6\3\2\2\2\u00b5")
        buf.write("\u00b3\3\2\2\2\u00b6\u00b7\b\17\1\2\u00b7\35\3\2\2\2\u00b8")
        buf.write("\u00b9\7\20\2\2\u00b9\u00bd\b\20\1\2\u00ba\u00bb\7\21")
        buf.write("\2\2\u00bb\u00bd\b\20\1\2\u00bc\u00b8\3\2\2\2\u00bc\u00ba")
        buf.write("\3\2\2\2\u00bd\37\3\2\2\2\u00be\u00c3\7!\2\2\u00bf\u00c0")
        buf.write("\7\22\2\2\u00c0\u00c1\5\"\22\2\u00c1\u00c2\b\21\1\2\u00c2")
        buf.write("\u00c4\3\2\2\2\u00c3\u00bf\3\2\2\2\u00c3\u00c4\3\2\2\2")
        buf.write("\u00c4\u00c5\3\2\2\2\u00c5\u00c6\b\21\1\2\u00c6!\3\2\2")
        buf.write("\2\u00c7\u00c8\b\22\1\2\u00c8\u00c9\t\2\2\2\u00c9\u00ca")
        buf.write("\5\"\22\n\u00ca\u00cb\b\22\1\2\u00cb\u00d4\3\2\2\2\u00cc")
        buf.write("\u00cd\5(\25\2\u00cd\u00ce\b\22\1\2\u00ce\u00d4\3\2\2")
        buf.write("\2\u00cf\u00d0\7\23\2\2\u00d0\u00d1\5&\24\2\u00d1\u00d2")
        buf.write("\b\22\1\2\u00d2\u00d4\3\2\2\2\u00d3\u00c7\3\2\2\2\u00d3")
        buf.write("\u00cc\3\2\2\2\u00d3\u00cf\3\2\2\2\u00d4\u010f\3\2\2\2")
        buf.write("\u00d5\u00d6\f\t\2\2\u00d6\u00d7\t\3\2\2\u00d7\u00d8\5")
        buf.write("\"\22\n\u00d8\u00d9\b\22\1\2\u00d9\u010e\3\2\2\2\u00da")
        buf.write("\u00db\f\b\2\2\u00db\u00dc\t\2\2\2\u00dc\u00dd\5\"\22")
        buf.write("\t\u00dd\u00de\b\22\1\2\u00de\u010e\3\2\2\2\u00df\u00e0")
        buf.write("\f\7\2\2\u00e0\u00e1\t\4\2\2\u00e1\u00e2\5\"\22\b\u00e2")
        buf.write("\u00e3\b\22\1\2\u00e3\u010e\3\2\2\2\u00e4\u00e5\f\6\2")
        buf.write("\2\u00e5\u00e6\t\5\2\2\u00e6\u00e7\5\"\22\7\u00e7\u00e8")
        buf.write("\b\22\1\2\u00e8\u010e\3\2\2\2\u00e9\u00ea\f\5\2\2\u00ea")
        buf.write("\u00eb\7\37\2\2\u00eb\u00ec\5\"\22\6\u00ec\u00ed\b\22")
        buf.write("\1\2\u00ed\u010e\3\2\2\2\u00ee\u00ef\f\4\2\2\u00ef\u00f0")
        buf.write("\7 \2\2\u00f0\u00f1\5\"\22\5\u00f1\u00f2\b\22\1\2\u00f2")
        buf.write("\u010e\3\2\2\2\u00f3\u00f4\f\3\2\2\u00f4\u00f5\7\22\2")
        buf.write("\2\u00f5\u00f6\5\"\22\3\u00f6\u00f7\b\22\1\2\u00f7\u010e")
        buf.write("\3\2\2\2\u00f8\u00fe\f\r\2\2\u00f9\u00fa\7\16\2\2\u00fa")
        buf.write("\u00fb\5\"\22\2\u00fb\u00fc\b\22\1\2\u00fc\u00fd\7\17")
        buf.write("\2\2\u00fd\u00ff\3\2\2\2\u00fe\u00f9\3\2\2\2\u00ff\u0100")
        buf.write("\3\2\2\2\u0100\u00fe\3\2\2\2\u0100\u0101\3\2\2\2\u0101")
        buf.write("\u0102\3\2\2\2\u0102\u0103\b\22\1\2\u0103\u010e\3\2\2")
        buf.write("\2\u0104\u0105\f\f\2\2\u0105\u0109\7\4\2\2\u0106\u0107")
        buf.write("\5$\23\2\u0107\u0108\b\22\1\2\u0108\u010a\3\2\2\2\u0109")
        buf.write("\u0106\3\2\2\2\u0109\u010a\3\2\2\2\u010a\u010b\3\2\2\2")
        buf.write("\u010b\u010c\7\5\2\2\u010c\u010e\b\22\1\2\u010d\u00d5")
        buf.write("\3\2\2\2\u010d\u00da\3\2\2\2\u010d\u00df\3\2\2\2\u010d")
        buf.write("\u00e4\3\2\2\2\u010d\u00e9\3\2\2\2\u010d\u00ee\3\2\2\2")
        buf.write("\u010d\u00f3\3\2\2\2\u010d\u00f8\3\2\2\2\u010d\u0104\3")
        buf.write("\2\2\2\u010e\u0111\3\2\2\2\u010f\u010d\3\2\2\2\u010f\u0110")
        buf.write("\3\2\2\2\u0110#\3\2\2\2\u0111\u010f\3\2\2\2\u0112\u0113")
        buf.write("\5\"\22\2\u0113\u011a\b\23\1\2\u0114\u0115\7\6\2\2\u0115")
        buf.write("\u0116\5\"\22\2\u0116\u0117\b\23\1\2\u0117\u0119\3\2\2")
        buf.write("\2\u0118\u0114\3\2\2\2\u0119\u011c\3\2\2\2\u011a\u0118")
        buf.write("\3\2\2\2\u011a\u011b\3\2\2\2\u011b%\3\2\2\2\u011c\u011a")
        buf.write("\3\2\2\2\u011d\u0123\5\36\20\2\u011e\u011f\7\16\2\2\u011f")
        buf.write("\u0120\5\"\22\2\u0120\u0121\b\24\1\2\u0121\u0122\7\17")
        buf.write("\2\2\u0122\u0124\3\2\2\2\u0123\u011e\3\2\2\2\u0124\u0125")
        buf.write("\3\2\2\2\u0125\u0123\3\2\2\2\u0125\u0126\3\2\2\2\u0126")
        buf.write("\u0127\3\2\2\2\u0127\u0128\b\24\1\2\u0128\'\3\2\2\2\u0129")
        buf.write("\u012a\7\4\2\2\u012a\u012b\5\"\22\2\u012b\u012c\7\5\2")
        buf.write("\2\u012c\u012d\b\25\1\2\u012d\u0134\3\2\2\2\u012e\u012f")
        buf.write("\5*\26\2\u012f\u0130\b\25\1\2\u0130\u0134\3\2\2\2\u0131")
        buf.write("\u0132\7!\2\2\u0132\u0134\b\25\1\2\u0133\u0129\3\2\2\2")
        buf.write("\u0133\u012e\3\2\2\2\u0133\u0131\3\2\2\2\u0134)\3\2\2")
        buf.write("\2\u0135\u0136\t\6\2\2\u0136+\3\2\2\2\30\61<JP\\it}\u008a")
        buf.write("\u0092\u009a\u00b3\u00bc\u00c3\u00d3\u0100\u0109\u010d")
        buf.write("\u010f\u011a\u0125\u0133")
        return buf.getvalue()


class GrammarParser ( Parser ):

    grammarFileName = "Grammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'void'", "'('", "')'", "','", "'{'", 
                     "'}'", "'if'", "'else'", "'while'", "'return'", "';'", 
                     "'['", "']'", "'boolean'", "'int'", "'='", "'new'", 
                     "'+'", "'-'", "'*'", "'/'", "'%'", "'<='", "'>='", 
                     "'>'", "'<'", "'=='", "'!='", "'&&'", "'||'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "Identifier", 
                      "IntegerLiteral", "BooleanLiteral", "WS", "COMMENT" ]

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
    RULE_primitiveType = 14
    RULE_variableDeclarator = 15
    RULE_expression = 16
    RULE_expressionList = 17
    RULE_creator = 18
    RULE_primary = 19
    RULE_literal = 20

    ruleNames =  [ "program", "programElement", "functionDeclaration", "formalParameters", 
                   "formalParameterList", "formalParameter", "block", "blockStatement", 
                   "statement", "brackedStatement", "parExpression", "callFunction", 
                   "variableDeclaration", "valueType", "primitiveType", 
                   "variableDeclarator", "expression", "expressionList", 
                   "creator", "primary", "literal" ]

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
    T__27=28
    T__28=29
    T__29=30
    Identifier=31
    IntegerLiteral=32
    BooleanLiteral=33
    WS=34
    COMMENT=35

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
            self.state = 47
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << GrammarParser.T__0) | (1 << GrammarParser.T__13) | (1 << GrammarParser.T__14))) != 0):
                self.state = 42
                localctx._programElement = self.programElement()
                self.program_states.add(localctx._programElement.element)
                self.state = 49
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 50
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
            self.state = 58
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 52
                localctx._functionDeclaration = self.functionDeclaration()
                localctx.element = localctx._functionDeclaration.function
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 55
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
            self.state = 72
            token = self._input.LA(1)
            if token in [GrammarParser.T__13, GrammarParser.T__14]:
                self.enterOuterAlt(localctx, 1)
                self.state = 60
                localctx._valueType = self.valueType()
                self.state = 61
                localctx._Identifier = self.match(GrammarParser.Identifier)
                self.state = 62
                localctx._formalParameters = self.formalParameters()
                self.state = 63
                localctx._block = self.block()
                localctx.function = get_function(localctx._valueType.value_type, (None if localctx._Identifier is None else localctx._Identifier.text), localctx._formalParameters.params, localctx._block.statements)

            elif token in [GrammarParser.T__0]:
                self.enterOuterAlt(localctx, 2)
                self.state = 66
                self.match(GrammarParser.T__0)
                self.state = 67
                localctx._Identifier = self.match(GrammarParser.Identifier)
                self.state = 68
                localctx._formalParameters = self.formalParameters()
                self.state = 69
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
            self.state = 74
            self.match(GrammarParser.T__1)
            self.state = 78
            _la = self._input.LA(1)
            if _la==GrammarParser.T__13 or _la==GrammarParser.T__14:
                self.state = 75
                localctx._formalParameterList = self.formalParameterList()
                localctx.params = localctx._formalParameterList.params


            self.state = 80
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
            self.state = 82
            localctx._formalParameter = self.formalParameter()
            localctx.params.append(localctx._formalParameter.variable)
            self.state = 90
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==GrammarParser.T__3:
                self.state = 84
                self.match(GrammarParser.T__3)
                self.state = 85
                localctx._formalParameter = self.formalParameter()
                localctx.params.append(localctx._formalParameter.variable)
                self.state = 92
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
            self.state = 93
            localctx._valueType = self.valueType()
            self.state = 94
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
            self.state = 97
            self.match(GrammarParser.T__4)
            self.state = 103
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << GrammarParser.T__1) | (1 << GrammarParser.T__6) | (1 << GrammarParser.T__8) | (1 << GrammarParser.T__9) | (1 << GrammarParser.T__13) | (1 << GrammarParser.T__14) | (1 << GrammarParser.T__16) | (1 << GrammarParser.T__17) | (1 << GrammarParser.T__18) | (1 << GrammarParser.Identifier) | (1 << GrammarParser.IntegerLiteral) | (1 << GrammarParser.BooleanLiteral))) != 0):
                self.state = 98
                localctx._blockStatement = self.blockStatement()
                localctx.statements.append(localctx._blockStatement.state)
                self.state = 105
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 106
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
            self.state = 114
            token = self._input.LA(1)
            if token in [GrammarParser.T__13, GrammarParser.T__14]:
                self.enterOuterAlt(localctx, 1)
                self.state = 108
                localctx._variableDeclaration = self.variableDeclaration()
                localctx.state = localctx._variableDeclaration.variable

            elif token in [GrammarParser.T__1, GrammarParser.T__6, GrammarParser.T__8, GrammarParser.T__9, GrammarParser.T__16, GrammarParser.T__17, GrammarParser.T__18, GrammarParser.Identifier, GrammarParser.IntegerLiteral, GrammarParser.BooleanLiteral]:
                self.enterOuterAlt(localctx, 2)
                self.state = 111
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
            self.b1 = None # BrackedStatementContext
            self.b2 = None # BrackedStatementContext
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
            self.state = 144
            token = self._input.LA(1)
            if token in [GrammarParser.T__6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 116
                self.match(GrammarParser.T__6)
                self.state = 117
                localctx._parExpression = self.parExpression()
                self.state = 118
                localctx.b1 = self.brackedStatement()
                self.state = 123
                _la = self._input.LA(1)
                if _la==GrammarParser.T__7:
                    self.state = 119
                    self.match(GrammarParser.T__7)
                    self.state = 120
                    localctx.b2 = self.brackedStatement()
                    tmp_var = ElseStatement(localctx.b2.statements)


                localctx.state = IfStatement(localctx._parExpression.expr, localctx.b1.statements, tmp_var)

            elif token in [GrammarParser.T__8]:
                self.enterOuterAlt(localctx, 2)
                self.state = 127
                self.match(GrammarParser.T__8)
                self.state = 128
                localctx._parExpression = self.parExpression()
                self.state = 129
                localctx.b1 = self.brackedStatement()
                localctx.state = WhileStatement(localctx._parExpression.expr, localctx.b1.statements)

            elif token in [GrammarParser.T__9]:
                self.enterOuterAlt(localctx, 3)
                self.state = 132
                self.match(GrammarParser.T__9)
                self.state = 136
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << GrammarParser.T__1) | (1 << GrammarParser.T__16) | (1 << GrammarParser.T__17) | (1 << GrammarParser.T__18) | (1 << GrammarParser.Identifier) | (1 << GrammarParser.IntegerLiteral) | (1 << GrammarParser.BooleanLiteral))) != 0):
                    self.state = 133
                    localctx._expression = self.expression(0)
                    tmp_var = localctx._expression.expr


                self.state = 138
                self.match(GrammarParser.T__10)
                localctx.state = ReturnStatement(tmp_var)

            elif token in [GrammarParser.T__1, GrammarParser.T__16, GrammarParser.T__17, GrammarParser.T__18, GrammarParser.Identifier, GrammarParser.IntegerLiteral, GrammarParser.BooleanLiteral]:
                self.enterOuterAlt(localctx, 4)
                self.state = 140
                localctx._callFunction = self.callFunction()
                self.state = 141
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
            self.state = 146
            self.match(GrammarParser.T__4)
            self.state = 152
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << GrammarParser.T__1) | (1 << GrammarParser.T__6) | (1 << GrammarParser.T__8) | (1 << GrammarParser.T__9) | (1 << GrammarParser.T__13) | (1 << GrammarParser.T__14) | (1 << GrammarParser.T__16) | (1 << GrammarParser.T__17) | (1 << GrammarParser.T__18) | (1 << GrammarParser.Identifier) | (1 << GrammarParser.IntegerLiteral) | (1 << GrammarParser.BooleanLiteral))) != 0):
                self.state = 147
                localctx._blockStatement = self.blockStatement()
                localctx.statements.append(localctx._blockStatement.state)
                self.state = 154
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 155
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
            self.state = 157
            self.match(GrammarParser.T__1)
            self.state = 158
            localctx._expression = self.expression(0)
            self.state = 159
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
            self.state = 162
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
            self.state = 165
            localctx._valueType = self.valueType()
            self.state = 166
            localctx._variableDeclarator = self.variableDeclarator()
            self.state = 167
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
            self._primitiveType = None # PrimitiveTypeContext

        def primitiveType(self):
            return self.getTypedRuleContext(GrammarParser.PrimitiveTypeContext,0)


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
        dimension = 0
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 170
            localctx._primitiveType = self.primitiveType()
            self.state = 177
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==GrammarParser.T__11:
                self.state = 171
                self.match(GrammarParser.T__11)
                self.state = 172
                self.match(GrammarParser.T__12)
                dimension += 1
                self.state = 179
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            localctx.value_type = primitiveType.value_type if dimension == 0 else Array(localctx._primitiveType.value_type, dimension)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PrimitiveTypeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.value_type =  None


        def getRuleIndex(self):
            return GrammarParser.RULE_primitiveType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimitiveType" ):
                listener.enterPrimitiveType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimitiveType" ):
                listener.exitPrimitiveType(self)




    def primitiveType(self):

        localctx = GrammarParser.PrimitiveTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_primitiveType)
        try:
            self.state = 186
            token = self._input.LA(1)
            if token in [GrammarParser.T__13]:
                self.enterOuterAlt(localctx, 1)
                self.state = 182
                self.match(GrammarParser.T__13)
                localctx.value_type = Type.boolean

            elif token in [GrammarParser.T__14]:
                self.enterOuterAlt(localctx, 2)
                self.state = 184
                self.match(GrammarParser.T__14)
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
        self.enterRule(localctx, 30, self.RULE_variableDeclarator)
        expr = None
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 188
            localctx._Identifier = self.match(GrammarParser.Identifier)
            self.state = 193
            _la = self._input.LA(1)
            if _la==GrammarParser.T__15:
                self.state = 189
                self.match(GrammarParser.T__15)
                self.state = 190
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
            self.e1 = None # ExpressionContext
            self.e = None # ExpressionContext
            self.n = None # ExpressionContext
            self.sign = None # Token
            self._primary = None # PrimaryContext
            self._creator = None # CreatorContext
            self.e2 = None # ExpressionContext
            self._expressionList = None # ExpressionListContext

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(GrammarParser.ExpressionContext,i)


        def primary(self):
            return self.getTypedRuleContext(GrammarParser.PrimaryContext,0)


        def creator(self):
            return self.getTypedRuleContext(GrammarParser.CreatorContext,0)


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
        _startState = 32
        self.enterRecursionRule(localctx, 32, self.RULE_expression, _p)
        tmp_var = None
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 209
            token = self._input.LA(1)
            if token in [GrammarParser.T__17, GrammarParser.T__18]:
                self.state = 198
                localctx.sign = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==GrammarParser.T__17 or _la==GrammarParser.T__18):
                    localctx.sign = self._errHandler.recoverInline(self)
                else:
                    self.consume()
                self.state = 199
                localctx.e = self.expression(8)
                localctx.expr = get_expression((None if localctx.sign is None else localctx.sign.text), None, localctx.e.expr)

            elif token in [GrammarParser.T__1, GrammarParser.Identifier, GrammarParser.IntegerLiteral, GrammarParser.BooleanLiteral]:
                self.state = 202
                localctx._primary = self.primary()
                localctx.expr = localctx._primary.expr

            elif token in [GrammarParser.T__16]:
                self.state = 205
                self.match(GrammarParser.T__16)
                self.state = 206
                localctx._creator = self.creator()
                localctx.expr = localctx._creator.constr

            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 269
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 267
                    la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
                    if la_ == 1:
                        localctx = GrammarParser.ExpressionContext(self, _parentctx, _parentState)
                        localctx.e1 = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 211
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 212
                        localctx.sign = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << GrammarParser.T__19) | (1 << GrammarParser.T__20) | (1 << GrammarParser.T__21))) != 0)):
                            localctx.sign = self._errHandler.recoverInline(self)
                        else:
                            self.consume()
                        self.state = 213
                        localctx.e2 = self.expression(8)
                        localctx.expr = get_expression((None if localctx.sign is None else localctx.sign.text), localctx.e1.expr, localctx.e2.expr)
                        pass

                    elif la_ == 2:
                        localctx = GrammarParser.ExpressionContext(self, _parentctx, _parentState)
                        localctx.e1 = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 216
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 217
                        localctx.sign = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==GrammarParser.T__17 or _la==GrammarParser.T__18):
                            localctx.sign = self._errHandler.recoverInline(self)
                        else:
                            self.consume()
                        self.state = 218
                        localctx.e2 = self.expression(7)
                        localctx.expr = get_expression((None if localctx.sign is None else localctx.sign.text), localctx.e1.expr, localctx.e2.expr)
                        pass

                    elif la_ == 3:
                        localctx = GrammarParser.ExpressionContext(self, _parentctx, _parentState)
                        localctx.e1 = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 221
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 222
                        localctx.sign = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << GrammarParser.T__22) | (1 << GrammarParser.T__23) | (1 << GrammarParser.T__24) | (1 << GrammarParser.T__25))) != 0)):
                            localctx.sign = self._errHandler.recoverInline(self)
                        else:
                            self.consume()
                        self.state = 223
                        localctx.e2 = self.expression(6)
                        localctx.expr = get_expression((None if localctx.sign is None else localctx.sign.text), localctx.e1.expr, localctx.e2.expr)
                        pass

                    elif la_ == 4:
                        localctx = GrammarParser.ExpressionContext(self, _parentctx, _parentState)
                        localctx.e1 = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 226
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 227
                        localctx.sign = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==GrammarParser.T__26 or _la==GrammarParser.T__27):
                            localctx.sign = self._errHandler.recoverInline(self)
                        else:
                            self.consume()
                        self.state = 228
                        localctx.e2 = self.expression(5)
                        localctx.expr = get_expression((None if localctx.sign is None else localctx.sign.text), localctx.e1.expr, localctx.e2.expr)
                        pass

                    elif la_ == 5:
                        localctx = GrammarParser.ExpressionContext(self, _parentctx, _parentState)
                        localctx.e1 = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 231
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 232
                        localctx.sign = self.match(GrammarParser.T__28)
                        self.state = 233
                        localctx.e2 = self.expression(4)
                        localctx.expr = get_expression((None if localctx.sign is None else localctx.sign.text), localctx.e1.expr, localctx.e2.expr)
                        pass

                    elif la_ == 6:
                        localctx = GrammarParser.ExpressionContext(self, _parentctx, _parentState)
                        localctx.e1 = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 236
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 237
                        localctx.sign = self.match(GrammarParser.T__29)
                        self.state = 238
                        localctx.e2 = self.expression(3)
                        localctx.expr = get_expression((None if localctx.sign is None else localctx.sign.text), localctx.e1.expr, localctx.e2.expr)
                        pass

                    elif la_ == 7:
                        localctx = GrammarParser.ExpressionContext(self, _parentctx, _parentState)
                        localctx.n = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 241
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 242
                        self.match(GrammarParser.T__15)
                        self.state = 243
                        localctx.e = self.expression(1)
                        localctx.expr = AssignmentOperator(localctx.n.expr, localctx.e.expr)
                        pass

                    elif la_ == 8:
                        localctx = GrammarParser.ExpressionContext(self, _parentctx, _parentState)
                        localctx.e1 = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 246
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 252 
                        self._errHandler.sync(self)
                        _alt = 1
                        while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                            if _alt == 1:
                                self.state = 247
                                self.match(GrammarParser.T__11)
                                self.state = 248
                                localctx.e2 = self.expression(0)
                                tmp_var = [localctx.e2.expr] if tmp_var is None else tmp_var.append(localctx.e2.expr)
                                self.state = 250
                                self.match(GrammarParser.T__12)

                            else:
                                raise NoViableAltException(self)
                            self.state = 254 
                            self._errHandler.sync(self)
                            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

                        localctx.expr = ArrayGetter(localctx.e1.expr, tmp_var)
                        pass

                    elif la_ == 9:
                        localctx = GrammarParser.ExpressionContext(self, _parentctx, _parentState)
                        localctx.e = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 258
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 259
                        self.match(GrammarParser.T__1)
                        self.state = 263
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << GrammarParser.T__1) | (1 << GrammarParser.T__16) | (1 << GrammarParser.T__17) | (1 << GrammarParser.T__18) | (1 << GrammarParser.Identifier) | (1 << GrammarParser.IntegerLiteral) | (1 << GrammarParser.BooleanLiteral))) != 0):
                            self.state = 260
                            localctx._expressionList = self.expressionList()
                            tmp_var = localctx._expressionList.args


                        self.state = 265
                        self.match(GrammarParser.T__2)
                        localctx.expr = get_call_function_statement((None if localctx.e is None else self._input.getText((localctx.e.start,localctx.e.stop))), tmp_var)
                        pass

             
                self.state = 271
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

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
        self.enterRule(localctx, 34, self.RULE_expressionList)
        localctx.args = []
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 272
            localctx._expression = self.expression(0)
            localctx.args.append(localctx._expression.expr)
            self.state = 280
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==GrammarParser.T__3:
                self.state = 274
                self.match(GrammarParser.T__3)
                self.state = 275
                localctx._expression = self.expression(0)
                localctx.args.append(localctx._expression.expr)
                self.state = 282
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CreatorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.constr =  None
            self._primitiveType = None # PrimitiveTypeContext
            self._expression = None # ExpressionContext

        def primitiveType(self):
            return self.getTypedRuleContext(GrammarParser.PrimitiveTypeContext,0)


        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(GrammarParser.ExpressionContext,i)


        def getRuleIndex(self):
            return GrammarParser.RULE_creator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCreator" ):
                listener.enterCreator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCreator" ):
                listener.exitCreator(self)




    def creator(self):

        localctx = GrammarParser.CreatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_creator)
        dimensions_sizes = []
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 283
            localctx._primitiveType = self.primitiveType()
            self.state = 289 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 284
                    self.match(GrammarParser.T__11)
                    self.state = 285
                    localctx._expression = self.expression(0)
                    dimensions_sizes.append(localctx._expression.expr)
                    self.state = 287
                    self.match(GrammarParser.T__12)

                else:
                    raise NoViableAltException(self)
                self.state = 291 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

            localctx.constr = ArrayCreator(localctx._primitiveType.value_type, dimensions_sizes)
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
        self.enterRule(localctx, 38, self.RULE_primary)
        try:
            self.state = 305
            token = self._input.LA(1)
            if token in [GrammarParser.T__1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 295
                self.match(GrammarParser.T__1)
                self.state = 296
                localctx._expression = self.expression(0)
                self.state = 297
                self.match(GrammarParser.T__2)
                localctx.expr = localctx._expression.expr

            elif token in [GrammarParser.IntegerLiteral, GrammarParser.BooleanLiteral]:
                self.enterOuterAlt(localctx, 2)
                self.state = 300
                localctx._literal = self.literal()
                localctx.expr = get_scalar((None if localctx._literal is None else self._input.getText((localctx._literal.start,localctx._literal.stop))))

            elif token in [GrammarParser.Identifier]:
                self.enterOuterAlt(localctx, 3)
                self.state = 303
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
        self.enterRule(localctx, 40, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 307
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
        self._predicates[16] = self.expression_sempred
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
                return self.precpred(self._ctx, 11)
         

            if predIndex == 8:
                return self.precpred(self._ctx, 10)
         




