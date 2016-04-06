# Generated from D:/Python/Compiler\Grammar.g4 by ANTLR 4.5.1
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
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\2\"")
        buf.write("\u00e1\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\4\3\4\3\5")
        buf.write("\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3")
        buf.write("\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3")
        buf.write("\13\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16")
        buf.write("\3\16\3\16\3\17\3\17\3\20\3\20\3\21\3\21\3\22\3\22\3\23")
        buf.write("\3\23\3\24\3\24\3\25\3\25\3\25\3\26\3\26\3\26\3\27\3\27")
        buf.write("\3\30\3\30\3\31\3\31\3\31\3\32\3\32\3\32\3\33\3\33\3\33")
        buf.write("\3\34\3\34\3\34\3\35\3\35\7\35\u00a6\n\35\f\35\16\35\u00a9")
        buf.write("\13\35\3\36\3\36\5\36\u00ad\n\36\3\37\3\37\3\37\3\37\3")
        buf.write("\37\3\37\3\37\3\37\3\37\5\37\u00b8\n\37\3 \3 \3 \7 \u00bd")
        buf.write("\n \f \16 \u00c0\13 \5 \u00c2\n \3!\3!\3\"\3\"\5\"\u00c8")
        buf.write("\n\"\3#\3#\3$\3$\3%\3%\3&\6&\u00d1\n&\r&\16&\u00d2\3&")
        buf.write("\3&\3\'\3\'\3\'\3\'\7\'\u00db\n\'\f\'\16\'\u00de\13\'")
        buf.write("\3\'\3\'\2\2(\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13")
        buf.write("\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26")
        buf.write("+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?\2A\2C")
        buf.write("\2E\2G\2I\2K!M\"\3\2\b\4\2NNnn\3\2\63;\4\2C\\c|\6\2\62")
        buf.write(";C\\aac|\5\2\13\f\16\17\"\"\4\2\f\f\17\17\u00e2\2\3\3")
        buf.write("\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2")
        buf.write("\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2")
        buf.write("\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2")
        buf.write("\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2")
        buf.write("\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3")
        buf.write("\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2")
        buf.write("\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2K\3\2\2\2\2M\3")
        buf.write("\2\2\2\3O\3\2\2\2\5T\3\2\2\2\7V\3\2\2\2\tX\3\2\2\2\13")
        buf.write("Z\3\2\2\2\r\\\3\2\2\2\17^\3\2\2\2\21a\3\2\2\2\23f\3\2")
        buf.write("\2\2\25l\3\2\2\2\27s\3\2\2\2\31u\3\2\2\2\33}\3\2\2\2\35")
        buf.write("\u0081\3\2\2\2\37\u0083\3\2\2\2!\u0085\3\2\2\2#\u0087")
        buf.write("\3\2\2\2%\u0089\3\2\2\2\'\u008b\3\2\2\2)\u008d\3\2\2\2")
        buf.write("+\u0090\3\2\2\2-\u0093\3\2\2\2/\u0095\3\2\2\2\61\u0097")
        buf.write("\3\2\2\2\63\u009a\3\2\2\2\65\u009d\3\2\2\2\67\u00a0\3")
        buf.write("\2\2\29\u00a3\3\2\2\2;\u00aa\3\2\2\2=\u00b7\3\2\2\2?\u00c1")
        buf.write("\3\2\2\2A\u00c3\3\2\2\2C\u00c7\3\2\2\2E\u00c9\3\2\2\2")
        buf.write("G\u00cb\3\2\2\2I\u00cd\3\2\2\2K\u00d0\3\2\2\2M\u00d6\3")
        buf.write("\2\2\2OP\7x\2\2PQ\7q\2\2QR\7k\2\2RS\7f\2\2S\4\3\2\2\2")
        buf.write("TU\7*\2\2U\6\3\2\2\2VW\7+\2\2W\b\3\2\2\2XY\7.\2\2Y\n\3")
        buf.write("\2\2\2Z[\7}\2\2[\f\3\2\2\2\\]\7\177\2\2]\16\3\2\2\2^_")
        buf.write("\7k\2\2_`\7h\2\2`\20\3\2\2\2ab\7g\2\2bc\7n\2\2cd\7u\2")
        buf.write("\2de\7g\2\2e\22\3\2\2\2fg\7y\2\2gh\7j\2\2hi\7k\2\2ij\7")
        buf.write("n\2\2jk\7g\2\2k\24\3\2\2\2lm\7t\2\2mn\7g\2\2no\7v\2\2")
        buf.write("op\7w\2\2pq\7t\2\2qr\7p\2\2r\26\3\2\2\2st\7=\2\2t\30\3")
        buf.write("\2\2\2uv\7d\2\2vw\7q\2\2wx\7q\2\2xy\7n\2\2yz\7g\2\2z{")
        buf.write("\7c\2\2{|\7p\2\2|\32\3\2\2\2}~\7k\2\2~\177\7p\2\2\177")
        buf.write("\u0080\7v\2\2\u0080\34\3\2\2\2\u0081\u0082\7?\2\2\u0082")
        buf.write("\36\3\2\2\2\u0083\u0084\7-\2\2\u0084 \3\2\2\2\u0085\u0086")
        buf.write("\7/\2\2\u0086\"\3\2\2\2\u0087\u0088\7,\2\2\u0088$\3\2")
        buf.write("\2\2\u0089\u008a\7\61\2\2\u008a&\3\2\2\2\u008b\u008c\7")
        buf.write("\'\2\2\u008c(\3\2\2\2\u008d\u008e\7>\2\2\u008e\u008f\7")
        buf.write("?\2\2\u008f*\3\2\2\2\u0090\u0091\7@\2\2\u0091\u0092\7")
        buf.write("?\2\2\u0092,\3\2\2\2\u0093\u0094\7@\2\2\u0094.\3\2\2\2")
        buf.write("\u0095\u0096\7>\2\2\u0096\60\3\2\2\2\u0097\u0098\7?\2")
        buf.write("\2\u0098\u0099\7?\2\2\u0099\62\3\2\2\2\u009a\u009b\7#")
        buf.write("\2\2\u009b\u009c\7?\2\2\u009c\64\3\2\2\2\u009d\u009e\7")
        buf.write("(\2\2\u009e\u009f\7(\2\2\u009f\66\3\2\2\2\u00a0\u00a1")
        buf.write("\7~\2\2\u00a1\u00a2\7~\2\2\u00a28\3\2\2\2\u00a3\u00a7")
        buf.write("\5G$\2\u00a4\u00a6\5I%\2\u00a5\u00a4\3\2\2\2\u00a6\u00a9")
        buf.write("\3\2\2\2\u00a7\u00a5\3\2\2\2\u00a7\u00a8\3\2\2\2\u00a8")
        buf.write(":\3\2\2\2\u00a9\u00a7\3\2\2\2\u00aa\u00ac\5? \2\u00ab")
        buf.write("\u00ad\5A!\2\u00ac\u00ab\3\2\2\2\u00ac\u00ad\3\2\2\2\u00ad")
        buf.write("<\3\2\2\2\u00ae\u00af\7v\2\2\u00af\u00b0\7t\2\2\u00b0")
        buf.write("\u00b1\7w\2\2\u00b1\u00b8\7g\2\2\u00b2\u00b3\7h\2\2\u00b3")
        buf.write("\u00b4\7c\2\2\u00b4\u00b5\7n\2\2\u00b5\u00b6\7u\2\2\u00b6")
        buf.write("\u00b8\7g\2\2\u00b7\u00ae\3\2\2\2\u00b7\u00b2\3\2\2\2")
        buf.write("\u00b8>\3\2\2\2\u00b9\u00c2\7\62\2\2\u00ba\u00be\5E#\2")
        buf.write("\u00bb\u00bd\5C\"\2\u00bc\u00bb\3\2\2\2\u00bd\u00c0\3")
        buf.write("\2\2\2\u00be\u00bc\3\2\2\2\u00be\u00bf\3\2\2\2\u00bf\u00c2")
        buf.write("\3\2\2\2\u00c0\u00be\3\2\2\2\u00c1\u00b9\3\2\2\2\u00c1")
        buf.write("\u00ba\3\2\2\2\u00c2@\3\2\2\2\u00c3\u00c4\t\2\2\2\u00c4")
        buf.write("B\3\2\2\2\u00c5\u00c8\7\62\2\2\u00c6\u00c8\5E#\2\u00c7")
        buf.write("\u00c5\3\2\2\2\u00c7\u00c6\3\2\2\2\u00c8D\3\2\2\2\u00c9")
        buf.write("\u00ca\t\3\2\2\u00caF\3\2\2\2\u00cb\u00cc\t\4\2\2\u00cc")
        buf.write("H\3\2\2\2\u00cd\u00ce\t\5\2\2\u00ceJ\3\2\2\2\u00cf\u00d1")
        buf.write("\t\6\2\2\u00d0\u00cf\3\2\2\2\u00d1\u00d2\3\2\2\2\u00d2")
        buf.write("\u00d0\3\2\2\2\u00d2\u00d3\3\2\2\2\u00d3\u00d4\3\2\2\2")
        buf.write("\u00d4\u00d5\b&\2\2\u00d5L\3\2\2\2\u00d6\u00d7\7\61\2")
        buf.write("\2\u00d7\u00d8\7\61\2\2\u00d8\u00dc\3\2\2\2\u00d9\u00db")
        buf.write("\n\7\2\2\u00da\u00d9\3\2\2\2\u00db\u00de\3\2\2\2\u00dc")
        buf.write("\u00da\3\2\2\2\u00dc\u00dd\3\2\2\2\u00dd\u00df\3\2\2\2")
        buf.write("\u00de\u00dc\3\2\2\2\u00df\u00e0\b\'\2\2\u00e0N\3\2\2")
        buf.write("\2\13\2\u00a7\u00ac\u00b7\u00be\u00c1\u00c7\u00d2\u00dc")
        buf.write("\3\b\2\2")
        return buf.getvalue()


class GrammarLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]


    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    T__11 = 12
    T__12 = 13
    T__13 = 14
    T__14 = 15
    T__15 = 16
    T__16 = 17
    T__17 = 18
    T__18 = 19
    T__19 = 20
    T__20 = 21
    T__21 = 22
    T__22 = 23
    T__23 = 24
    T__24 = 25
    T__25 = 26
    T__26 = 27
    Identifier = 28
    IntegerLiteral = 29
    BooleanLiteral = 30
    WS = 31
    COMMENT = 32

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'void'", "'('", "')'", "','", "'{'", "'}'", "'if'", "'else'", 
            "'while'", "'return'", "';'", "'boolean'", "'int'", "'='", "'+'", 
            "'-'", "'*'", "'/'", "'%'", "'<='", "'>='", "'>'", "'<'", "'=='", 
            "'!='", "'&&'", "'||'" ]

    symbolicNames = [ "<INVALID>",
            "Identifier", "IntegerLiteral", "BooleanLiteral", "WS", "COMMENT" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "T__13", 
                  "T__14", "T__15", "T__16", "T__17", "T__18", "T__19", 
                  "T__20", "T__21", "T__22", "T__23", "T__24", "T__25", 
                  "T__26", "Identifier", "IntegerLiteral", "BooleanLiteral", 
                  "Number", "NumberSuffix", "Digit", "NonZeroDigit", "Letter", 
                  "LetterOrDigit", "WS", "COMMENT" ]

    grammarFileName = "Grammar.g4"

    def __init__(self, input=None):
        super().__init__(input)
        self.checkVersion("4.5.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


