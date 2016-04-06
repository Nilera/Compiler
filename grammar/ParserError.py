from antlr4.error.ErrorListener import ErrorListener


class ParserError(ErrorListener):
    def __init__(self):
        super(ParserError, self).__init__()

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise SyntaxError("line %d:%d %s" % (line, column, msg))
