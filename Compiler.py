from antlr4 import *

from GrammarLexer import GrammarLexer
from GrammarParser import GrammarParser


def main():
    input = FileStream("input")
    lexer = GrammarLexer(input)
    stream = CommonTokenStream(lexer)
    parser = GrammarParser(stream)
    parser.program()
    parser.program_states.name_mangling()
    print(str(parser.program_states))


main()
