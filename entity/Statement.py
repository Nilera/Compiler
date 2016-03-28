from operator import contains

from CodeGenerator import CodeGenerator
from NameMangling import NameMangling
from entity.Function import ReadFunction, WriteFunction
from entity.Scalar import VariableScalar
from entity.StatementsContainer import StatementsContainer


class WhileStatement(StatementsContainer):
    def __init__(self, condition, statements):
        super(WhileStatement, self).__init__()
        self.__condition = condition
        self.add_all(statements)

    def name_mangling(self, function_name, mangled_name):
        self.__condition.name_mangling(function_name, mangled_name)
        super().name_mangling(function_name, mangled_name)

    def windows_code(self, code_builder, program_state):
        pass

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

    def windows_code(self, code_builder, program_state):
        raise NotImplementedError

    def __str__(self):
        else_statement = "" if self.__else_statement is None else str(self.__else_statement)
        return "if %s \n" % str(self.__condition) + super().__str__() + else_statement


class ElseStatement(StatementsContainer):
    def __init__(self, statements):
        super(ElseStatement, self).__init__()
        self.add_all(statements)

    def windows_code(self, code_builder, program_state):
        raise NotImplementedError

    def __str__(self):
        return "else\n" + "\n".join("\t%d  %s" % (i, str(self[i])) for i in range(len(self)))


class ReturnStatement(NameMangling, CodeGenerator):
    def __init__(self, expression):
        self.__expression = expression

    def name_mangling(self, function_name, mangled_name):
        self.__expression.name_mangling(function_name, mangled_name)

    def windows_code(self, code_builder, program_state):
        pass

    def __str__(self):
        return "return %s" % str(self.__expression)


def get_call_function_statement(function_name, args=None):
    if function_name == ReadFunction.FUNCTION_NAME:
        return CallReadFunction(function_name, args)
    elif function_name == WriteFunction.FUNCTION_NAME:
        return CallWriteFunction(function_name, args)
    elif function_name == CallPopFunction.FUNCTION_NAME:
        return CallPopFunction(function_name, args)
    else:
        return CallFunctionStatement(function_name, args)


class CallFunctionStatement(NameMangling, CodeGenerator):
    def __init__(self, function_name, args=None):
        super(CallFunctionStatement, self).__init__()
        self._function_name = function_name
        args = [] if args is None else args
        self._args = args

    def name_mangling(self, function_name, mangled_name):
        if contains(mangled_name, self._function_name):
            self._function_name = mangled_name[self._function_name]
        for i in range(len(self._args)):
            if isinstance(self._args[i], VariableScalar) and contains(mangled_name, self._args[i].value):
                self._args[i].name_mangling(function_name, mangled_name)

    def windows_code(self, code_builder, program_state):
        pass

    def __str__(self):
        args = "" if self._args is None else ", ".join(str(arg) for arg in self._args)
        return "%s(%s)" % (self._function_name, args)

    @staticmethod
    def _convert_args(program_state, raw_args):
        args = []
        for var_scalar in raw_args:
            var_name = var_scalar.value
            variable = program_state.get_variable(var_name)
            args.append(CallPopFunction(CallPopFunction.FUNCTION_NAME, variable))
        return args


class CallReadFunction(CallFunctionStatement):
    def __init__(self, function_name, args):
        super(CallReadFunction, self).__init__(function_name, args)

    def windows_code(self, code_builder, program_state):
        read_fun = ReadFunction(None, self._function_name,
                                CallFunctionStatement._convert_args(program_state, self._args))
        code_builder.add_instruction("call", read_fun.get_label())
        code_builder.add_global_function(read_fun)


class CallWriteFunction(CallFunctionStatement):
    def __init__(self, function_name, args):
        super(CallWriteFunction, self).__init__(function_name, args)

    def windows_code(self, code_builder, program_state):
        write_fun = WriteFunction(None, self._function_name,
                                  CallFunctionStatement._convert_args(program_state, self._args))
        code_builder.add_instruction("call", write_fun.get_label())
        code_builder.add_global_function(write_fun)

    @staticmethod
    def __convert_args(program_state, raw_args):
        args = []
        for var_scalar in raw_args:
            args.append(program_state.get_variable(var_scalar.value))
        return args


class CallPopFunction(CallFunctionStatement):
    FUNCTION_NAME = "__pop"

    def __init__(self, function_name, args):
        super(CallPopFunction, self).__init__(function_name, args)

    @property
    def variable(self):
        return self._args

    def name_mangling(self, function_name, mangled_name):
        self._args.name_mangling(function_name, mangled_name)

    def windows_code(self, code_builder, program_state):
        code_builder.add_instruction("pop", "[%s]" % self._args.name)

    def __str__(self):
        return "%s(%s)" % (self._function_name, self._args)
