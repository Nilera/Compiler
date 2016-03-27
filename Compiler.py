from antlr4 import *

from GrammarLexer import GrammarLexer
from GrammarParser import GrammarParser
from CodeBuilder import CodeBuilder


def main():
    input_stream = FileStream("input")
    lexer = GrammarLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = GrammarParser(stream)
    parser.program()
    parser.program_states.name_mangling()
    builder = CodeBuilder()
    parser.program_states.windows_code(builder)
    print(str(builder))


main()
