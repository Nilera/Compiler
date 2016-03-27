from antlr4 import *

from GrammarLexer import GrammarLexer
from GrammarParser import GrammarParser


def main():
    input_stream = FileStream("input")
    lexer = GrammarLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = GrammarParser(stream)
    parser.program()
    parser.program_states.name_mangling()
    print(str(parser.program_states))


main()
