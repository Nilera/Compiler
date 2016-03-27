from operator import contains

from entity.CodeGenerator import CodeGenerator
from entity.NameMangling import NameMangling
from entity.StatementsContainer import StatementsContainer


class WhileStatement(StatementsContainer):
    def __init__(self, condition, statements):
        super(WhileStatement, self).__init__()
        self.__condition = condition
        self.add_all(statements)

    def name_mangling(self, function_name, mangled_name):
        self.__condition.name_mangling(function_name, mangled_name)
        super().name_mangling(function_name, mangled_name)

    def code(self):
        raise NotImplementedError

    def __str__(self):
        return "while %s \n" % str(self.__condition) + super().__str__()


class IfStatement(StatementsContainer):
    def __init__(self, condition, statements, else_statement=None):
        super(IfStatement, self).__init__()
        self.__condition = condition
        self.add_all(statements)
        self.__else_statement = else_statement

    def name_mangling(self, function_name, mangled_name):
        self.__condition.name_mangling(function_name, mangled_name)
        super().name_mangling(function_name, mangled_name)

    def code(self):
        raise NotImplementedError

    def __str__(self):
        else_statement = "" if self.__else_statement is None else str(self.__else_statement)
        return "if %s \n" % str(self.__condition) + super().__str__() + else_statement


class ElseStatement(StatementsContainer):
    def __init__(self, statements):
        super(ElseStatement, self).__init__()
        self.add_all(statements)

    def code(self):
        raise NotImplementedError

    def __str__(self):
        return "else\n" + "\n".join("\t%d  %s" % (i, str(self[i])) for i in range(len(self)))


class ReturnStatement(NameMangling, CodeGenerator):
    def __init__(self, expression):
        self.__expression = expression

    def name_mangling(self, function_name, mangled_name):
        self.__expression.name_mangling(function_name, mangled_name)

    def code(self):
        raise NotImplementedError

    def __str__(self):
        return "return %s" % str(self.__expression)


class CallFunctionStatement(NameMangling, CodeGenerator):
    def __init__(self, function_name, args=None):
        self.__function_name = function_name
        args = [] if args is None else args
        self.__args = args

    def name_mangling(self, function_name, mangled_name):
        if contains(mangled_name, self.__function_name):
            self.__function_name = mangled_name[self.__function_name]
        for i in range(len(self.__args)):
            if contains(mangled_name, self.__args[i]):
                self.__args[i] = mangled_name[self.__args[i]]

    def code(self):
        raise NotImplementedError

    def __str__(self):
        args = "" if self.__args is None else ", ".join(str(arg) for arg in self.__args)
        return "%s(%s)" % (self.__function_name, args)
