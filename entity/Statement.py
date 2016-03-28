from operator import contains

from CodeGenerator import CodeGenerator
from NameMangling import NameMangling
from entity.Expression import Operator, BooleanBinaryOperator
from entity.Function import ReadFunction, WriteFunction
from entity.Scalar import VariableScalar, BoolScalar
from entity.StatementsContainer import StatementsContainer
from entity.Type import Type


class WhileStatement(StatementsContainer):
    def __init__(self, condition, statements):
        super(WhileStatement, self).__init__()
        self.__condition = condition
        self.add_all(statements)

    def name_mangling(self, function_name, mangled_name):
        self.__condition.name_mangling(function_name, mangled_name)
        super().name_mangling(function_name, mangled_name)

    def windows_code(self, code_builder, program_state):
        label = "%s_while_%d" % (program_state.function_name, program_state.get_while_number())
        exit_label = "%s_exit" % label
        code_builder.add_label(label)
        if isinstance(self.__condition, BoolScalar):
            code_builder.add_instruction("mov", "eax", self.__condition.value)
        elif isinstance(self.__condition, VariableScalar) \
                and program_state.get_variable(self.__condition.value).type_value == Type.boolean:
            code_builder.add_instruction("mov", "eax", "[%s]" % self.__condition.value)
        elif isinstance(self.__condition, BooleanBinaryOperator):
            self.__condition.windows_code(code_builder, program_state)
        else:
            raise SyntaxError("while condition should be boolean value or boolean expression")
        code_builder.add_instruction("cmp", "eax", "0")
        code_builder.add_instruction("je", exit_label)
        for statement in self:
            statement.windows_code(code_builder, program_state)
        code_builder.add_instruction("jmp", label)
        code_builder.add_label(exit_label)

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
        label = "%s_if_%d" % (program_state.function_name, program_state.get_if_number())
        exit_label = "%s_exit" % label
        if isinstance(self.__condition, BoolScalar):
            code_builder.add_instruction("mov", "eax", self.__condition.value)
        elif isinstance(self.__condition, VariableScalar) \
                and program_state.get_variable(self.__condition.value).type_value == Type.boolean:
            code_builder.add_instruction("mov", "eax", "[%s]" % self.__condition.value)
        elif isinstance(self.__condition, BooleanBinaryOperator):
            self.__condition.windows_code(code_builder, program_state)
        else:
            raise SyntaxError("while condition should be boolean value or boolean expression")
        code_builder.add_instruction("cmp", "eax", "1")
        code_builder.add_instruction("je", label)
        if self.__else_statement is not None:
            self.__else_statement.windows_code(code_builder, program_state)
        code_builder.add_instruction("jmp", exit_label)
        code_builder.add_label(label)
        for statement in self:
            statement.windows_code(code_builder, program_state)
        code_builder.add_label(exit_label)

    def __str__(self):
        else_statement = "" if self.__else_statement is None else str(self.__else_statement)
        return "if %s \n" % str(self.__condition) + super().__str__() + else_statement


class ElseStatement(StatementsContainer):
    def __init__(self, statements):
        super(ElseStatement, self).__init__()
        self.add_all(statements)

    def windows_code(self, code_builder, program_state):
        for statement in self:
            statement.windows_code(code_builder, program_state)

    def __str__(self):
        return "else\n" + "\n".join("\t%d  %s" % (i, str(self[i])) for i in range(len(self)))


class ReturnStatement(NameMangling, CodeGenerator):
    def __init__(self, expression):
        self.__expression = expression

    def name_mangling(self, function_name, mangled_name):
        self.__expression.name_mangling(function_name, mangled_name)

    def windows_code(self, code_builder, program_state, is_main=False):
        if is_main:
            code_builder.add_extern("__imp__ExitProcess@4")
        if isinstance(self.__expression, Operator):
            self.__expression.windows_code(code_builder, program_state)
            code_builder.add_instruction("push", "eax")
        elif isinstance(self.__expression, VariableScalar):
            code_builder.add_instruction("mov", "eax", "[%s]" % self.__expression.value)
            code_builder.add_instruction("push", "eax")
        else:
            code_builder.add_instruction("push", self.__expression.value)
        if is_main:
            code_builder.add_instruction("call", "[__imp__ExitProcess@4]")

    def __str__(self):
        return "return %s" % str(self.__expression)


def get_call_function_statement(function_name, args=None):
    if function_name == ReadFunction.FUNCTION_NAME:
        return CallReadFunction(function_name, args)
    elif function_name == WriteFunction.FUNCTION_NAME:
        return CallWriteFunction(function_name, args)
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
        for arg in reversed(self._args):
            code_builder.add_instruction("mov", "eax", "[%s]" % arg.value)
            code_builder.add_instruction("push", "eax")
        code_builder.add_instruction("add", "esp", str(4 * (len(self._args) + 1)))
        code_builder.add_instruction("call", self._function_name)
        code_builder.add_instruction("sub", "esp", "8")
        code_builder.add_instruction("pop", "eax")
        code_builder.add_instruction("add", "esp", "4")

    def __str__(self):
        args = "" if self._args is None else ", ".join(str(arg) for arg in self._args)
        return "%s(%s)" % (self._function_name, args)

    @staticmethod
    def _convert_args(program_state, raw_args):
        args = []
        for var_scalar in raw_args:
            args.append(program_state.get_variable(var_scalar.value))
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
