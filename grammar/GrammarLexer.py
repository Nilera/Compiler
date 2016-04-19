# Generated from /home/isamborskiy/Python/Compiler/grammar/Grammar.g4 by ANTLR 4.5.1
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
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\2&")
        buf.write("\u00f0\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\3\2\3\2\3\2\3\2\3\2\3")
        buf.write("\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\b\3\t")
        buf.write("\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3")
        buf.write("\17\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\23\3\23\3\23\3\23")
        buf.write("\3\24\3\24\3\25\3\25\3\26\3\26\3\27\3\27\3\30\3\30\3\31")
        buf.write("\3\31\3\31\3\32\3\32\3\32\3\33\3\33\3\34\3\34\3\35\3\35")
        buf.write("\3\35\3\36\3\36\3\36\3\37\3\37\3\37\3 \3 \3 \3!\3!\7!")
        buf.write("\u00b9\n!\f!\16!\u00bc\13!\3\"\3\"\3#\3#\3#\3#\3#\3#\3")
        buf.write("#\3#\3#\5#\u00c9\n#\3$\3$\3$\7$\u00ce\n$\f$\16$\u00d1")
        buf.write("\13$\5$\u00d3\n$\3%\3%\5%\u00d7\n%\3&\3&\3\'\3\'\3(\3")
        buf.write("(\3)\6)\u00e0\n)\r)\16)\u00e1\3)\3)\3*\3*\3*\3*\7*\u00ea")
        buf.write("\n*\f*\16*\u00ed\13*\3*\3*\2\2+\3\3\5\4\7\5\t\6\13\7\r")
        buf.write("\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!")
        buf.write("\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67")
        buf.write("\359\36;\37= ?!A\"C#E$G\2I\2K\2M\2O\2Q%S&\3\2\7\3\2\63")
        buf.write(";\4\2C\\c|\6\2\62;C\\aac|\5\2\13\f\16\17\"\"\4\2\f\f\17")
        buf.write("\17\u00f1\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2")
        buf.write("\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2")
        buf.write("\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2")
        buf.write("\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#")
        buf.write("\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2")
        buf.write("\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65")
        buf.write("\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2")
        buf.write("\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2Q\3\2\2")
        buf.write("\2\2S\3\2\2\2\3U\3\2\2\2\5Z\3\2\2\2\7\\\3\2\2\2\t^\3\2")
        buf.write("\2\2\13`\3\2\2\2\rb\3\2\2\2\17d\3\2\2\2\21g\3\2\2\2\23")
        buf.write("l\3\2\2\2\25r\3\2\2\2\27y\3\2\2\2\31{\3\2\2\2\33}\3\2")
        buf.write("\2\2\35\177\3\2\2\2\37\u0087\3\2\2\2!\u008b\3\2\2\2#\u0090")
        buf.write("\3\2\2\2%\u0092\3\2\2\2\'\u0096\3\2\2\2)\u0098\3\2\2\2")
        buf.write("+\u009a\3\2\2\2-\u009c\3\2\2\2/\u009e\3\2\2\2\61\u00a0")
        buf.write("\3\2\2\2\63\u00a3\3\2\2\2\65\u00a6\3\2\2\2\67\u00a8\3")
        buf.write("\2\2\29\u00aa\3\2\2\2;\u00ad\3\2\2\2=\u00b0\3\2\2\2?\u00b3")
        buf.write("\3\2\2\2A\u00b6\3\2\2\2C\u00bd\3\2\2\2E\u00c8\3\2\2\2")
        buf.write("G\u00d2\3\2\2\2I\u00d6\3\2\2\2K\u00d8\3\2\2\2M\u00da\3")
        buf.write("\2\2\2O\u00dc\3\2\2\2Q\u00df\3\2\2\2S\u00e5\3\2\2\2UV")
        buf.write("\7x\2\2VW\7q\2\2WX\7k\2\2XY\7f\2\2Y\4\3\2\2\2Z[\7*\2\2")
        buf.write("[\6\3\2\2\2\\]\7+\2\2]\b\3\2\2\2^_\7.\2\2_\n\3\2\2\2`")
        buf.write("a\7}\2\2a\f\3\2\2\2bc\7\177\2\2c\16\3\2\2\2de\7k\2\2e")
        buf.write("f\7h\2\2f\20\3\2\2\2gh\7g\2\2hi\7n\2\2ij\7u\2\2jk\7g\2")
        buf.write("\2k\22\3\2\2\2lm\7y\2\2mn\7j\2\2no\7k\2\2op\7n\2\2pq\7")
        buf.write("g\2\2q\24\3\2\2\2rs\7t\2\2st\7g\2\2tu\7v\2\2uv\7w\2\2")
        buf.write("vw\7t\2\2wx\7p\2\2x\26\3\2\2\2yz\7=\2\2z\30\3\2\2\2{|")
        buf.write("\7]\2\2|\32\3\2\2\2}~\7_\2\2~\34\3\2\2\2\177\u0080\7d")
        buf.write("\2\2\u0080\u0081\7q\2\2\u0081\u0082\7q\2\2\u0082\u0083")
        buf.write("\7n\2\2\u0083\u0084\7g\2\2\u0084\u0085\7c\2\2\u0085\u0086")
        buf.write("\7p\2\2\u0086\36\3\2\2\2\u0087\u0088\7k\2\2\u0088\u0089")
        buf.write("\7p\2\2\u0089\u008a\7v\2\2\u008a \3\2\2\2\u008b\u008c")
        buf.write("\7e\2\2\u008c\u008d\7j\2\2\u008d\u008e\7c\2\2\u008e\u008f")
        buf.write("\7t\2\2\u008f\"\3\2\2\2\u0090\u0091\7?\2\2\u0091$\3\2")
        buf.write("\2\2\u0092\u0093\7p\2\2\u0093\u0094\7g\2\2\u0094\u0095")
        buf.write("\7y\2\2\u0095&\3\2\2\2\u0096\u0097\7-\2\2\u0097(\3\2\2")
        buf.write("\2\u0098\u0099\7/\2\2\u0099*\3\2\2\2\u009a\u009b\7,\2")
        buf.write("\2\u009b,\3\2\2\2\u009c\u009d\7\61\2\2\u009d.\3\2\2\2")
        buf.write("\u009e\u009f\7\'\2\2\u009f\60\3\2\2\2\u00a0\u00a1\7>\2")
        buf.write("\2\u00a1\u00a2\7?\2\2\u00a2\62\3\2\2\2\u00a3\u00a4\7@")
        buf.write("\2\2\u00a4\u00a5\7?\2\2\u00a5\64\3\2\2\2\u00a6\u00a7\7")
        buf.write("@\2\2\u00a7\66\3\2\2\2\u00a8\u00a9\7>\2\2\u00a98\3\2\2")
        buf.write("\2\u00aa\u00ab\7?\2\2\u00ab\u00ac\7?\2\2\u00ac:\3\2\2")
        buf.write("\2\u00ad\u00ae\7#\2\2\u00ae\u00af\7?\2\2\u00af<\3\2\2")
        buf.write("\2\u00b0\u00b1\7(\2\2\u00b1\u00b2\7(\2\2\u00b2>\3\2\2")
        buf.write("\2\u00b3\u00b4\7~\2\2\u00b4\u00b5\7~\2\2\u00b5@\3\2\2")
        buf.write("\2\u00b6\u00ba\5M\'\2\u00b7\u00b9\5O(\2\u00b8\u00b7\3")
        buf.write("\2\2\2\u00b9\u00bc\3\2\2\2\u00ba\u00b8\3\2\2\2\u00ba\u00bb")
        buf.write("\3\2\2\2\u00bbB\3\2\2\2\u00bc\u00ba\3\2\2\2\u00bd\u00be")
        buf.write("\5G$\2\u00beD\3\2\2\2\u00bf\u00c0\7v\2\2\u00c0\u00c1\7")
        buf.write("t\2\2\u00c1\u00c2\7w\2\2\u00c2\u00c9\7g\2\2\u00c3\u00c4")
        buf.write("\7h\2\2\u00c4\u00c5\7c\2\2\u00c5\u00c6\7n\2\2\u00c6\u00c7")
        buf.write("\7u\2\2\u00c7\u00c9\7g\2\2\u00c8\u00bf\3\2\2\2\u00c8\u00c3")
        buf.write("\3\2\2\2\u00c9F\3\2\2\2\u00ca\u00d3\7\62\2\2\u00cb\u00cf")
        buf.write("\5K&\2\u00cc\u00ce\5I%\2\u00cd\u00cc\3\2\2\2\u00ce\u00d1")
        buf.write("\3\2\2\2\u00cf\u00cd\3\2\2\2\u00cf\u00d0\3\2\2\2\u00d0")
        buf.write("\u00d3\3\2\2\2\u00d1\u00cf\3\2\2\2\u00d2\u00ca\3\2\2\2")
        buf.write("\u00d2\u00cb\3\2\2\2\u00d3H\3\2\2\2\u00d4\u00d7\7\62\2")
        buf.write("\2\u00d5\u00d7\5K&\2\u00d6\u00d4\3\2\2\2\u00d6\u00d5\3")
        buf.write("\2\2\2\u00d7J\3\2\2\2\u00d8\u00d9\t\2\2\2\u00d9L\3\2\2")
        buf.write("\2\u00da\u00db\t\3\2\2\u00dbN\3\2\2\2\u00dc\u00dd\t\4")
        buf.write("\2\2\u00ddP\3\2\2\2\u00de\u00e0\t\5\2\2\u00df\u00de\3")
        buf.write("\2\2\2\u00e0\u00e1\3\2\2\2\u00e1\u00df\3\2\2\2\u00e1\u00e2")
        buf.write("\3\2\2\2\u00e2\u00e3\3\2\2\2\u00e3\u00e4\b)\2\2\u00e4")
        buf.write("R\3\2\2\2\u00e5\u00e6\7\61\2\2\u00e6\u00e7\7\61\2\2\u00e7")
        buf.write("\u00eb\3\2\2\2\u00e8\u00ea\n\6\2\2\u00e9\u00e8\3\2\2\2")
        buf.write("\u00ea\u00ed\3\2\2\2\u00eb\u00e9\3\2\2\2\u00eb\u00ec\3")
        buf.write("\2\2\2\u00ec\u00ee\3\2\2\2\u00ed\u00eb\3\2\2\2\u00ee\u00ef")
        buf.write("\b*\2\2\u00efT\3\2\2\2\n\2\u00ba\u00c8\u00cf\u00d2\u00d6")
        buf.write("\u00e1\u00eb\3\b\2\2")
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
    T__27 = 28
    T__28 = 29
    T__29 = 30
    T__30 = 31
    Identifier = 32
    IntegerLiteral = 33
    BooleanLiteral = 34
    WS = 35
    COMMENT = 36

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'void'", "'('", "')'", "','", "'{'", "'}'", "'if'", "'else'", 
            "'while'", "'return'", "';'", "'['", "']'", "'boolean'", "'int'", 
            "'char'", "'='", "'new'", "'+'", "'-'", "'*'", "'/'", "'%'", 
            "'<='", "'>='", "'>'", "'<'", "'=='", "'!='", "'&&'", "'||'" ]

    symbolicNames = [ "<INVALID>",
            "Identifier", "IntegerLiteral", "BooleanLiteral", "WS", "COMMENT" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "T__13", 
                  "T__14", "T__15", "T__16", "T__17", "T__18", "T__19", 
                  "T__20", "T__21", "T__22", "T__23", "T__24", "T__25", 
                  "T__26", "T__27", "T__28", "T__29", "T__30", "Identifier", 
                  "IntegerLiteral", "BooleanLiteral", "Number", "Digit", 
                  "NonZeroDigit", "Letter", "LetterOrDigit", "WS", "COMMENT" ]

    grammarFileName = "Grammar.g4"

    def __init__(self, input=None):
        super().__init__(input)
        self.checkVersion("4.5.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


