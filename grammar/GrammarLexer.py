# Generated from D:/Python/Compiler/grammar\Grammar.g4 by ANTLR 4.5.1
from antlr4 import *
from io import StringIO


from entity.Program import Program
from entity.Variable import Variable
from entity.Function import *
from entity.Expression import *
from entity.Type import Type
from entity.Array import *
from entity.Scalar import *
from entity.Statement import *


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\2(")
        buf.write("\u011a\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\4\3")
        buf.write("\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\b\3\t\3\t\3\t\3\t")
        buf.write("\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17\3\17\3")
        buf.write("\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\22\3\22\3\23\3\23\3\23\3\23\3\24\3\24")
        buf.write("\3\25\3\25\3\26\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3\31")
        buf.write("\3\32\3\32\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\35\3\36")
        buf.write("\3\36\3\36\3\37\3\37\3\37\3 \3 \3 \3!\3!\7!\u00c5\n!\f")
        buf.write("!\16!\u00c8\13!\3\"\3\"\3#\3#\3#\3#\3#\3#\3#\3#\3#\5#")
        buf.write("\u00d5\n#\3$\3$\3$\3$\3$\3$\3$\3$\5$\u00df\n$\3%\3%\3")
        buf.write("&\3&\5&\u00e5\n&\3&\3&\3\'\6\'\u00ea\n\'\r\'\16\'\u00eb")
        buf.write("\3(\3(\5(\u00f0\n(\3)\3)\3)\3*\3*\3*\7*\u00f8\n*\f*\16")
        buf.write("*\u00fb\13*\5*\u00fd\n*\3+\3+\5+\u0101\n+\3,\3,\3-\3-")
        buf.write("\3.\3.\3/\6/\u010a\n/\r/\16/\u010b\3/\3/\3\60\3\60\3\60")
        buf.write("\3\60\7\60\u0114\n\60\f\60\16\60\u0117\13\60\3\60\3\60")
        buf.write("\2\2\61\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f")
        buf.write("\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27")
        buf.write("-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%")
        buf.write("I\2K&M\2O\2Q\2S\2U\2W\2Y\2[\2]\'_(\3\2\n\4\2))^^\4\2$")
        buf.write("$^^\n\2$$))^^ddhhppttvv\3\2\63;\4\2C\\c|\6\2\62;C\\aa")
        buf.write("c|\5\2\13\f\16\17\"\"\4\2\f\f\17\17\u011b\2\3\3\2\2\2")
        buf.write("\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r")
        buf.write("\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3")
        buf.write("\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2")
        buf.write("\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'")
        buf.write("\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2")
        buf.write("\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29")
        buf.write("\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2")
        buf.write("C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2K\3\2\2\2\2]\3\2\2\2")
        buf.write("\2_\3\2\2\2\3a\3\2\2\2\5f\3\2\2\2\7h\3\2\2\2\tj\3\2\2")
        buf.write("\2\13l\3\2\2\2\rn\3\2\2\2\17p\3\2\2\2\21s\3\2\2\2\23x")
        buf.write("\3\2\2\2\25~\3\2\2\2\27\u0085\3\2\2\2\31\u0087\3\2\2\2")
        buf.write("\33\u0089\3\2\2\2\35\u008b\3\2\2\2\37\u0093\3\2\2\2!\u0097")
        buf.write("\3\2\2\2#\u009c\3\2\2\2%\u009e\3\2\2\2\'\u00a2\3\2\2\2")
        buf.write(")\u00a4\3\2\2\2+\u00a6\3\2\2\2-\u00a8\3\2\2\2/\u00aa\3")
        buf.write("\2\2\2\61\u00ac\3\2\2\2\63\u00af\3\2\2\2\65\u00b2\3\2")
        buf.write("\2\2\67\u00b4\3\2\2\29\u00b6\3\2\2\2;\u00b9\3\2\2\2=\u00bc")
        buf.write("\3\2\2\2?\u00bf\3\2\2\2A\u00c2\3\2\2\2C\u00c9\3\2\2\2")
        buf.write("E\u00d4\3\2\2\2G\u00de\3\2\2\2I\u00e0\3\2\2\2K\u00e2\3")
        buf.write("\2\2\2M\u00e9\3\2\2\2O\u00ef\3\2\2\2Q\u00f1\3\2\2\2S\u00fc")
        buf.write("\3\2\2\2U\u0100\3\2\2\2W\u0102\3\2\2\2Y\u0104\3\2\2\2")
        buf.write("[\u0106\3\2\2\2]\u0109\3\2\2\2_\u010f\3\2\2\2ab\7x\2\2")
        buf.write("bc\7q\2\2cd\7k\2\2de\7f\2\2e\4\3\2\2\2fg\7*\2\2g\6\3\2")
        buf.write("\2\2hi\7+\2\2i\b\3\2\2\2jk\7.\2\2k\n\3\2\2\2lm\7}\2\2")
        buf.write("m\f\3\2\2\2no\7\177\2\2o\16\3\2\2\2pq\7k\2\2qr\7h\2\2")
        buf.write("r\20\3\2\2\2st\7g\2\2tu\7n\2\2uv\7u\2\2vw\7g\2\2w\22\3")
        buf.write("\2\2\2xy\7y\2\2yz\7j\2\2z{\7k\2\2{|\7n\2\2|}\7g\2\2}\24")
        buf.write("\3\2\2\2~\177\7t\2\2\177\u0080\7g\2\2\u0080\u0081\7v\2")
        buf.write("\2\u0081\u0082\7w\2\2\u0082\u0083\7t\2\2\u0083\u0084\7")
        buf.write("p\2\2\u0084\26\3\2\2\2\u0085\u0086\7=\2\2\u0086\30\3\2")
        buf.write("\2\2\u0087\u0088\7]\2\2\u0088\32\3\2\2\2\u0089\u008a\7")
        buf.write("_\2\2\u008a\34\3\2\2\2\u008b\u008c\7d\2\2\u008c\u008d")
        buf.write("\7q\2\2\u008d\u008e\7q\2\2\u008e\u008f\7n\2\2\u008f\u0090")
        buf.write("\7g\2\2\u0090\u0091\7c\2\2\u0091\u0092\7p\2\2\u0092\36")
        buf.write("\3\2\2\2\u0093\u0094\7k\2\2\u0094\u0095\7p\2\2\u0095\u0096")
        buf.write("\7v\2\2\u0096 \3\2\2\2\u0097\u0098\7e\2\2\u0098\u0099")
        buf.write("\7j\2\2\u0099\u009a\7c\2\2\u009a\u009b\7t\2\2\u009b\"")
        buf.write("\3\2\2\2\u009c\u009d\7?\2\2\u009d$\3\2\2\2\u009e\u009f")
        buf.write("\7p\2\2\u009f\u00a0\7g\2\2\u00a0\u00a1\7y\2\2\u00a1&\3")
        buf.write("\2\2\2\u00a2\u00a3\7-\2\2\u00a3(\3\2\2\2\u00a4\u00a5\7")
        buf.write("/\2\2\u00a5*\3\2\2\2\u00a6\u00a7\7,\2\2\u00a7,\3\2\2\2")
        buf.write("\u00a8\u00a9\7\61\2\2\u00a9.\3\2\2\2\u00aa\u00ab\7\'\2")
        buf.write("\2\u00ab\60\3\2\2\2\u00ac\u00ad\7>\2\2\u00ad\u00ae\7?")
        buf.write("\2\2\u00ae\62\3\2\2\2\u00af\u00b0\7@\2\2\u00b0\u00b1\7")
        buf.write("?\2\2\u00b1\64\3\2\2\2\u00b2\u00b3\7@\2\2\u00b3\66\3\2")
        buf.write("\2\2\u00b4\u00b5\7>\2\2\u00b58\3\2\2\2\u00b6\u00b7\7?")
        buf.write("\2\2\u00b7\u00b8\7?\2\2\u00b8:\3\2\2\2\u00b9\u00ba\7#")
        buf.write("\2\2\u00ba\u00bb\7?\2\2\u00bb<\3\2\2\2\u00bc\u00bd\7(")
        buf.write("\2\2\u00bd\u00be\7(\2\2\u00be>\3\2\2\2\u00bf\u00c0\7~")
        buf.write("\2\2\u00c0\u00c1\7~\2\2\u00c1@\3\2\2\2\u00c2\u00c6\5Y")
        buf.write("-\2\u00c3\u00c5\5[.\2\u00c4\u00c3\3\2\2\2\u00c5\u00c8")
        buf.write("\3\2\2\2\u00c6\u00c4\3\2\2\2\u00c6\u00c7\3\2\2\2\u00c7")
        buf.write("B\3\2\2\2\u00c8\u00c6\3\2\2\2\u00c9\u00ca\5S*\2\u00ca")
        buf.write("D\3\2\2\2\u00cb\u00cc\7v\2\2\u00cc\u00cd\7t\2\2\u00cd")
        buf.write("\u00ce\7w\2\2\u00ce\u00d5\7g\2\2\u00cf\u00d0\7h\2\2\u00d0")
        buf.write("\u00d1\7c\2\2\u00d1\u00d2\7n\2\2\u00d2\u00d3\7u\2\2\u00d3")
        buf.write("\u00d5\7g\2\2\u00d4\u00cb\3\2\2\2\u00d4\u00cf\3\2\2\2")
        buf.write("\u00d5F\3\2\2\2\u00d6\u00d7\7)\2\2\u00d7\u00d8\5I%\2\u00d8")
        buf.write("\u00d9\7)\2\2\u00d9\u00df\3\2\2\2\u00da\u00db\7)\2\2\u00db")
        buf.write("\u00dc\5Q)\2\u00dc\u00dd\7)\2\2\u00dd\u00df\3\2\2\2\u00de")
        buf.write("\u00d6\3\2\2\2\u00de\u00da\3\2\2\2\u00dfH\3\2\2\2\u00e0")
        buf.write("\u00e1\n\2\2\2\u00e1J\3\2\2\2\u00e2\u00e4\7$\2\2\u00e3")
        buf.write("\u00e5\5M\'\2\u00e4\u00e3\3\2\2\2\u00e4\u00e5\3\2\2\2")
        buf.write("\u00e5\u00e6\3\2\2\2\u00e6\u00e7\7$\2\2\u00e7L\3\2\2\2")
        buf.write("\u00e8\u00ea\5O(\2\u00e9\u00e8\3\2\2\2\u00ea\u00eb\3\2")
        buf.write("\2\2\u00eb\u00e9\3\2\2\2\u00eb\u00ec\3\2\2\2\u00ecN\3")
        buf.write("\2\2\2\u00ed\u00f0\n\3\2\2\u00ee\u00f0\5Q)\2\u00ef\u00ed")
        buf.write("\3\2\2\2\u00ef\u00ee\3\2\2\2\u00f0P\3\2\2\2\u00f1\u00f2")
        buf.write("\7^\2\2\u00f2\u00f3\t\4\2\2\u00f3R\3\2\2\2\u00f4\u00fd")
        buf.write("\7\62\2\2\u00f5\u00f9\5W,\2\u00f6\u00f8\5U+\2\u00f7\u00f6")
        buf.write("\3\2\2\2\u00f8\u00fb\3\2\2\2\u00f9\u00f7\3\2\2\2\u00f9")
        buf.write("\u00fa\3\2\2\2\u00fa\u00fd\3\2\2\2\u00fb\u00f9\3\2\2\2")
        buf.write("\u00fc\u00f4\3\2\2\2\u00fc\u00f5\3\2\2\2\u00fdT\3\2\2")
        buf.write("\2\u00fe\u0101\7\62\2\2\u00ff\u0101\5W,\2\u0100\u00fe")
        buf.write("\3\2\2\2\u0100\u00ff\3\2\2\2\u0101V\3\2\2\2\u0102\u0103")
        buf.write("\t\5\2\2\u0103X\3\2\2\2\u0104\u0105\t\6\2\2\u0105Z\3\2")
        buf.write("\2\2\u0106\u0107\t\7\2\2\u0107\\\3\2\2\2\u0108\u010a\t")
        buf.write("\b\2\2\u0109\u0108\3\2\2\2\u010a\u010b\3\2\2\2\u010b\u0109")
        buf.write("\3\2\2\2\u010b\u010c\3\2\2\2\u010c\u010d\3\2\2\2\u010d")
        buf.write("\u010e\b/\2\2\u010e^\3\2\2\2\u010f\u0110\7\61\2\2\u0110")
        buf.write("\u0111\7\61\2\2\u0111\u0115\3\2\2\2\u0112\u0114\n\t\2")
        buf.write("\2\u0113\u0112\3\2\2\2\u0114\u0117\3\2\2\2\u0115\u0113")
        buf.write("\3\2\2\2\u0115\u0116\3\2\2\2\u0116\u0118\3\2\2\2\u0117")
        buf.write("\u0115\3\2\2\2\u0118\u0119\b\60\2\2\u0119`\3\2\2\2\16")
        buf.write("\2\u00c6\u00d4\u00de\u00e4\u00eb\u00ef\u00f9\u00fc\u0100")
        buf.write("\u010b\u0115\3\b\2\2")
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
    CharacterLiteral = 35
    StringLiteral = 36
    WS = 37
    COMMENT = 38

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'void'", "'('", "')'", "','", "'{'", "'}'", "'if'", "'else'", 
            "'while'", "'return'", "';'", "'['", "']'", "'boolean'", "'int'", 
            "'char'", "'='", "'new'", "'+'", "'-'", "'*'", "'/'", "'%'", 
            "'<='", "'>='", "'>'", "'<'", "'=='", "'!='", "'&&'", "'||'" ]

    symbolicNames = [ "<INVALID>",
            "Identifier", "IntegerLiteral", "BooleanLiteral", "CharacterLiteral", 
            "StringLiteral", "WS", "COMMENT" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "T__13", 
                  "T__14", "T__15", "T__16", "T__17", "T__18", "T__19", 
                  "T__20", "T__21", "T__22", "T__23", "T__24", "T__25", 
                  "T__26", "T__27", "T__28", "T__29", "T__30", "Identifier", 
                  "IntegerLiteral", "BooleanLiteral", "CharacterLiteral", 
                  "SingleCharacter", "StringLiteral", "StringCharacters", 
                  "StringCharacter", "EscapeSequence", "Number", "Digit", 
                  "NonZeroDigit", "Letter", "LetterOrDigit", "WS", "COMMENT" ]

    grammarFileName = "Grammar.g4"

    def __init__(self, input=None):
        super().__init__(input)
        self.checkVersion("4.5.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


