from antlr4 import *

from CodeBuilder import CodeBuilder
from GrammarLexer import GrammarLexer
from GrammarParser import GrammarParser
from ProgramState import ProgramState


def main():
    input_stream = FileStream("input")
    lexer = GrammarLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = GrammarParser(stream)
    parser.program()
    parser.program_states.name_mangling()
    state = ProgramState()
    builder = CodeBuilder(state)
    parser.program_states.windows_code(builder, state)
    print(str(builder))
    # print(str(parser.program_states))


main()
