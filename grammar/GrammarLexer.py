# Generated from D:/Python/Compiler/grammar\Grammar.g4 by ANTLR 4.5.1
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
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\2%")
        buf.write("\u00e9\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\3\2\3\2\3\2\3\2\3\2\3\3\3\3")
        buf.write("\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\b\3\t\3\t\3")
        buf.write("\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17\3")
        buf.write("\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\21")
        buf.write("\3\21\3\22\3\22\3\22\3\22\3\23\3\23\3\24\3\24\3\25\3\25")
        buf.write("\3\26\3\26\3\27\3\27\3\30\3\30\3\30\3\31\3\31\3\31\3\32")
        buf.write("\3\32\3\33\3\33\3\34\3\34\3\34\3\35\3\35\3\35\3\36\3\36")
        buf.write("\3\36\3\37\3\37\3\37\3 \3 \7 \u00b2\n \f \16 \u00b5\13")
        buf.write(" \3!\3!\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\5\"\u00c2")
        buf.write("\n\"\3#\3#\3#\7#\u00c7\n#\f#\16#\u00ca\13#\5#\u00cc\n")
        buf.write("#\3$\3$\5$\u00d0\n$\3%\3%\3&\3&\3\'\3\'\3(\6(\u00d9\n")
        buf.write("(\r(\16(\u00da\3(\3(\3)\3)\3)\3)\7)\u00e3\n)\f)\16)\u00e6")
        buf.write("\13)\3)\3)\2\2*\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23")
        buf.write("\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25")
        buf.write(")\26+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A")
        buf.write("\"C#E\2G\2I\2K\2M\2O$Q%\3\2\7\3\2\63;\4\2C\\c|\6\2\62")
        buf.write(";C\\aac|\5\2\13\f\16\17\"\"\4\2\f\f\17\17\u00ea\2\3\3")
        buf.write("\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2")
        buf.write("\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2")
        buf.write("\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2")
        buf.write("\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2")
        buf.write("\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3")
        buf.write("\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2")
        buf.write("\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3")
        buf.write("\2\2\2\2C\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\3S\3\2\2\2\5X")
        buf.write("\3\2\2\2\7Z\3\2\2\2\t\\\3\2\2\2\13^\3\2\2\2\r`\3\2\2\2")
        buf.write("\17b\3\2\2\2\21e\3\2\2\2\23j\3\2\2\2\25p\3\2\2\2\27w\3")
        buf.write("\2\2\2\31y\3\2\2\2\33{\3\2\2\2\35}\3\2\2\2\37\u0085\3")
        buf.write("\2\2\2!\u0089\3\2\2\2#\u008b\3\2\2\2%\u008f\3\2\2\2\'")
        buf.write("\u0091\3\2\2\2)\u0093\3\2\2\2+\u0095\3\2\2\2-\u0097\3")
        buf.write("\2\2\2/\u0099\3\2\2\2\61\u009c\3\2\2\2\63\u009f\3\2\2")
        buf.write("\2\65\u00a1\3\2\2\2\67\u00a3\3\2\2\29\u00a6\3\2\2\2;\u00a9")
        buf.write("\3\2\2\2=\u00ac\3\2\2\2?\u00af\3\2\2\2A\u00b6\3\2\2\2")
        buf.write("C\u00c1\3\2\2\2E\u00cb\3\2\2\2G\u00cf\3\2\2\2I\u00d1\3")
        buf.write("\2\2\2K\u00d3\3\2\2\2M\u00d5\3\2\2\2O\u00d8\3\2\2\2Q\u00de")
        buf.write("\3\2\2\2ST\7x\2\2TU\7q\2\2UV\7k\2\2VW\7f\2\2W\4\3\2\2")
        buf.write("\2XY\7*\2\2Y\6\3\2\2\2Z[\7+\2\2[\b\3\2\2\2\\]\7.\2\2]")
        buf.write("\n\3\2\2\2^_\7}\2\2_\f\3\2\2\2`a\7\177\2\2a\16\3\2\2\2")
        buf.write("bc\7k\2\2cd\7h\2\2d\20\3\2\2\2ef\7g\2\2fg\7n\2\2gh\7u")
        buf.write("\2\2hi\7g\2\2i\22\3\2\2\2jk\7y\2\2kl\7j\2\2lm\7k\2\2m")
        buf.write("n\7n\2\2no\7g\2\2o\24\3\2\2\2pq\7t\2\2qr\7g\2\2rs\7v\2")
        buf.write("\2st\7w\2\2tu\7t\2\2uv\7p\2\2v\26\3\2\2\2wx\7=\2\2x\30")
        buf.write("\3\2\2\2yz\7]\2\2z\32\3\2\2\2{|\7_\2\2|\34\3\2\2\2}~\7")
        buf.write("d\2\2~\177\7q\2\2\177\u0080\7q\2\2\u0080\u0081\7n\2\2")
        buf.write("\u0081\u0082\7g\2\2\u0082\u0083\7c\2\2\u0083\u0084\7p")
        buf.write("\2\2\u0084\36\3\2\2\2\u0085\u0086\7k\2\2\u0086\u0087\7")
        buf.write("p\2\2\u0087\u0088\7v\2\2\u0088 \3\2\2\2\u0089\u008a\7")
        buf.write("?\2\2\u008a\"\3\2\2\2\u008b\u008c\7p\2\2\u008c\u008d\7")
        buf.write("g\2\2\u008d\u008e\7y\2\2\u008e$\3\2\2\2\u008f\u0090\7")
        buf.write("-\2\2\u0090&\3\2\2\2\u0091\u0092\7/\2\2\u0092(\3\2\2\2")
        buf.write("\u0093\u0094\7,\2\2\u0094*\3\2\2\2\u0095\u0096\7\61\2")
        buf.write("\2\u0096,\3\2\2\2\u0097\u0098\7\'\2\2\u0098.\3\2\2\2\u0099")
        buf.write("\u009a\7>\2\2\u009a\u009b\7?\2\2\u009b\60\3\2\2\2\u009c")
        buf.write("\u009d\7@\2\2\u009d\u009e\7?\2\2\u009e\62\3\2\2\2\u009f")
        buf.write("\u00a0\7@\2\2\u00a0\64\3\2\2\2\u00a1\u00a2\7>\2\2\u00a2")
        buf.write("\66\3\2\2\2\u00a3\u00a4\7?\2\2\u00a4\u00a5\7?\2\2\u00a5")
        buf.write("8\3\2\2\2\u00a6\u00a7\7#\2\2\u00a7\u00a8\7?\2\2\u00a8")
        buf.write(":\3\2\2\2\u00a9\u00aa\7(\2\2\u00aa\u00ab\7(\2\2\u00ab")
        buf.write("<\3\2\2\2\u00ac\u00ad\7~\2\2\u00ad\u00ae\7~\2\2\u00ae")
        buf.write(">\3\2\2\2\u00af\u00b3\5K&\2\u00b0\u00b2\5M\'\2\u00b1\u00b0")
        buf.write("\3\2\2\2\u00b2\u00b5\3\2\2\2\u00b3\u00b1\3\2\2\2\u00b3")
        buf.write("\u00b4\3\2\2\2\u00b4@\3\2\2\2\u00b5\u00b3\3\2\2\2\u00b6")
        buf.write("\u00b7\5E#\2\u00b7B\3\2\2\2\u00b8\u00b9\7v\2\2\u00b9\u00ba")
        buf.write("\7t\2\2\u00ba\u00bb\7w\2\2\u00bb\u00c2\7g\2\2\u00bc\u00bd")
        buf.write("\7h\2\2\u00bd\u00be\7c\2\2\u00be\u00bf\7n\2\2\u00bf\u00c0")
        buf.write("\7u\2\2\u00c0\u00c2\7g\2\2\u00c1\u00b8\3\2\2\2\u00c1\u00bc")
        buf.write("\3\2\2\2\u00c2D\3\2\2\2\u00c3\u00cc\7\62\2\2\u00c4\u00c8")
        buf.write("\5I%\2\u00c5\u00c7\5G$\2\u00c6\u00c5\3\2\2\2\u00c7\u00ca")
        buf.write("\3\2\2\2\u00c8\u00c6\3\2\2\2\u00c8\u00c9\3\2\2\2\u00c9")
        buf.write("\u00cc\3\2\2\2\u00ca\u00c8\3\2\2\2\u00cb\u00c3\3\2\2\2")
        buf.write("\u00cb\u00c4\3\2\2\2\u00ccF\3\2\2\2\u00cd\u00d0\7\62\2")
        buf.write("\2\u00ce\u00d0\5I%\2\u00cf\u00cd\3\2\2\2\u00cf\u00ce\3")
        buf.write("\2\2\2\u00d0H\3\2\2\2\u00d1\u00d2\t\2\2\2\u00d2J\3\2\2")
        buf.write("\2\u00d3\u00d4\t\3\2\2\u00d4L\3\2\2\2\u00d5\u00d6\t\4")
        buf.write("\2\2\u00d6N\3\2\2\2\u00d7\u00d9\t\5\2\2\u00d8\u00d7\3")
        buf.write("\2\2\2\u00d9\u00da\3\2\2\2\u00da\u00d8\3\2\2\2\u00da\u00db")
        buf.write("\3\2\2\2\u00db\u00dc\3\2\2\2\u00dc\u00dd\b(\2\2\u00dd")
        buf.write("P\3\2\2\2\u00de\u00df\7\61\2\2\u00df\u00e0\7\61\2\2\u00e0")
        buf.write("\u00e4\3\2\2\2\u00e1\u00e3\n\6\2\2\u00e2\u00e1\3\2\2\2")
        buf.write("\u00e3\u00e6\3\2\2\2\u00e4\u00e2\3\2\2\2\u00e4\u00e5\3")
        buf.write("\2\2\2\u00e5\u00e7\3\2\2\2\u00e6\u00e4\3\2\2\2\u00e7\u00e8")
        buf.write("\b)\2\2\u00e8R\3\2\2\2\n\2\u00b3\u00c1\u00c8\u00cb\u00cf")
        buf.write("\u00da\u00e4\3\b\2\2")
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
    Identifier = 31
    IntegerLiteral = 32
    BooleanLiteral = 33
    WS = 34
    COMMENT = 35

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'void'", "'('", "')'", "','", "'{'", "'}'", "'if'", "'else'", 
            "'while'", "'return'", "';'", "'['", "']'", "'boolean'", "'int'", 
            "'='", "'new'", "'+'", "'-'", "'*'", "'/'", "'%'", "'<='", "'>='", 
            "'>'", "'<'", "'=='", "'!='", "'&&'", "'||'" ]

    symbolicNames = [ "<INVALID>",
            "Identifier", "IntegerLiteral", "BooleanLiteral", "WS", "COMMENT" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "T__13", 
                  "T__14", "T__15", "T__16", "T__17", "T__18", "T__19", 
                  "T__20", "T__21", "T__22", "T__23", "T__24", "T__25", 
                  "T__26", "T__27", "T__28", "T__29", "Identifier", "IntegerLiteral", 
                  "BooleanLiteral", "Number", "Digit", "NonZeroDigit", "Letter", 
                  "LetterOrDigit", "WS", "COMMENT" ]

    grammarFileName = "Grammar.g4"

    def __init__(self, input=None):
        super().__init__(input)
        self.checkVersion("4.5.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


