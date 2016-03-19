from antlr4 import *

from GrammarLexer import GrammarLexer
from GrammarParser import GrammarParser


def main():
    input = FileStream("input")
    lexer = GrammarLexer(input)
    stream = CommonTokenStream(lexer)
    parser = GrammarParser(stream)
    tree = parser.prog()
    print(tree.toStringTree())


main()
