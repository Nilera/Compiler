from operator import contains

from entity.Array import Array
from entity.CodeGenerator import CodeGenerator
from entity.Expression import BooleanBinaryOperator
from entity.Function import ReadFunction, WriteFunction, MainFunction, ArrayCopyFunction
from entity.NameMangling import NameMangling
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

    def code(self, code_builder, program_state):
        label = "%s_while_%d" % (program_state.function_name, program_state.get_while_number())
        exit_label = "%s_exit" % label
        code_builder.add_label(label)
        if isinstance(self.__condition, BoolScalar):
            code_builder.add_instruction("mov", "eax", self.__condition.value)
        elif isinstance(self.__condition, VariableScalar) \
                and program_state.get_variable(self.__condition.value).type_value == Type.boolean:
            code_builder.add_instruction("mov", "eax", "[%s]" % self.__condition.value)
        elif isinstance(self.__condition, BooleanBinaryOperator):
            self.__condition.code(code_builder, program_state)
        else:
            raise SyntaxError("while condition should be boolean value or boolean expression")
        code_builder.add_instruction("cmp", "eax", "0")
        code_builder.add_instruction("je", exit_label)
        for statement in self:
            statement.code(code_builder, program_state)
        code_builder.add_instruction("jmp", label)
        code_builder.add_label(exit_label)

    def value_type(self, program_state):
        return None

    def unmangling(self):
        return ""

    def __str__(self):
        return "while %s \n" % str(self.__condition) + super().__str__()


class IfStatement(StatementsContainer):
    def __init__(self, condition, statements, else_statement=None):
        super(IfStatement, self).__init__()
        self.__condition = condition
        self.add_all(statements)
        self.__else_statement = else_statement

    @property
    def else_statement(self):
        return self.__else_statement

    def name_mangling(self, function_name, mangled_name):
        self.__condition.name_mangling(function_name, mangled_name)
        super().name_mangling(function_name, mangled_name)

    def code(self, code_builder, program_state):
        label = "%s_if_%d" % (program_state.function_name, program_state.get_if_number())
        exit_label = "%s_exit" % label
        if isinstance(self.__condition, BoolScalar):
            code_builder.add_instruction("mov", "eax", self.__condition.value)
        elif isinstance(self.__condition, VariableScalar) \
                and program_state.get_variable(self.__condition.value).value_type() == Type.boolean:
            code_builder.add_instruction("mov", "eax", "[%s]" % self.__condition.value)
        elif isinstance(self.__condition, BooleanBinaryOperator):
            self.__condition.code(code_builder, program_state)
        else:
            raise SyntaxError("while condition should be boolean value or boolean expression")
        code_builder.add_instruction("cmp", "eax", "1")
        code_builder.add_instruction("je", label)
        if self.__else_statement is not None:
            self.__else_statement.code(code_builder, program_state)
        code_builder.add_instruction("jmp", exit_label)
        code_builder.add_label(label)
        for statement in self:
            statement.code(code_builder, program_state)
        code_builder.add_label(exit_label)

    def value_type(self, program_state):
        return None

    def unmangling(self):
        return ""

    def __str__(self):
        else_statement = "" if self.__else_statement is None else str(self.__else_statement)
        return "if %s \n" % str(self.__condition) + super().__str__() + else_statement


class ElseStatement(StatementsContainer):
    def __init__(self, statements):
        super(ElseStatement, self).__init__()
        self.add_all(statements)

    def code(self, code_builder, program_state):
        for statement in self:
            statement.code(code_builder, program_state)

    def value_type(self, program_state):
        return None

    def unmangling(self):
        return ""

    def __str__(self):
        return "else\n" + "\n".join("\t%d  %s" % (i, str(self[i])) for i in range(len(self)))


class ReturnStatement(NameMangling, CodeGenerator):
    def __init__(self, expression):
        self.__expression = expression

    def name_mangling(self, function_name, mangled_name):
        self.__expression.name_mangling(function_name, mangled_name)

    def code(self, code_builder, program_state):
        if isinstance(self.__expression.value_type(program_state), Array):
            raise SyntaxError("function couldn't return array")
        self.__expression.code(code_builder, program_state)
        code_builder.add_instruction("push", "eax")

    def value_type(self, program_state):
        return None

    def unmangling(self):
        return ""

    def __str__(self):
        return "return %s" % str(self.__expression)


def get_call_function_statement(function_name, args=None):
    if function_name == MainFunction.FUNCTION_NAME:
        raise SyntaxError("call main function is forbidden")
    elif function_name == ReadFunction.FUNCTION_NAME:
        return CallReadFunction(function_name, args)
    elif function_name == WriteFunction.FUNCTION_NAME:
        return CallWriteFunction(function_name, args)
    elif function_name == ArrayCopyFunction.FUNCTION_NAME:
        return CallArrayCopyFunction(function_name, args)
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
            self._args[i].name_mangling(function_name, mangled_name)

    def code(self, code_builder, program_state):
        self._code_validation(program_state)
        for arg in reversed(self._args):
            arg.code(code_builder, program_state)
            code_builder.add_instruction("push", "eax")
        code_builder.add_instruction("call", self._function_name)
        code_builder.add_instruction("sub", "esp", "8")
        code_builder.add_instruction("pop", "eax")
        code_builder.add_instruction("add", "esp", str(4 * (len(self._args) + 1)))

    def _code_validation(self, program_state):
        if not program_state.contains_function(self._function_name):
            raise SyntaxError("no function \"%s\" in scope" % NameMangling.unmangling(self._function_name))
        params = program_state.get_function(self._function_name).params
        if len(params) != len(self._args) or not self.__is_valid_params(params, program_state):
            raise SyntaxError(
                "function %s cannot be applied to given types\nrequired: %s\nfound: %s" % (
                    self._function_name,
                    "no arguments" if len(params) == 0 else ", ".join(str(x.value_type(program_state)) for x in params),
                    "no arguments" if len(params) == 0 else ", ".join(
                        str(x.value_type(program_state)) for x in self._args)))

    def __is_valid_params(self, params, program_state):
        for i in range(len(params)):
            arg1 = params[i].value_type(program_state)
            arg2 = self._args[i].value_type(program_state)
            if arg1 != arg2:
                return False
        return True

    def value_type(self, program_state):
        if not program_state.contains_function(self._function_name):
            raise ValueError("no function \"%s\" in scope" % self.unmangling())
        return program_state.get_function(self._function_name).value_type()

    def unmangling(self):
        args = "" if self._args is None else ", ".join(arg.unmangling() for arg in self._args)
        return "%s(%s)" % (NameMangling.unmangling(self._function_name), args)

    def __str__(self):
        args = "" if self._args is None else ", ".join(str(arg) for arg in self._args)
        return "%s(%s)" % (self._function_name, args)


class CallReadFunction(CallFunctionStatement):
    def __init__(self, function_name, args):
        super(CallReadFunction, self).__init__(function_name, args)

    def value_type(self, program_state):
        return None

    def code(self, code_builder, program_state):
        if len(self._args) != 1:
            raise SyntaxError(
                "actual and formal argument lists of function read is differ in length\nrequired: 1\nfound: %d" % len(
                    self._args))
        # TODO: add string
        if not isinstance(self._args[0], VariableScalar):
            raise SyntaxError("function read cannot be applied to given arguments\nrequired: variable name")
        read_fun = ReadFunction(None, self._function_name, self._args)
        code_builder.add_instruction("call", read_fun.get_label(program_state))
        code_builder.add_global_function(read_fun)


class CallWriteFunction(CallFunctionStatement):
    def __init__(self, function_name, args):
        super(CallWriteFunction, self).__init__(function_name, args)

    def code(self, code_builder, program_state):
        if len(self._args) != 1:
            raise SyntaxError(
                "actual and formal argument lists of function write is differ in length\nrequired: 1\nfound: %d" % len(
                    self._args))
        # TODO: add string
        if not isinstance(self._args[0].value_type(program_state), (Type, Array)):
            raise SyntaxError(
                "function write cannot be applied to given arguments\nrequired: int, boolean, char or char[]")
        write_fun = WriteFunction(None, self._function_name, self._args)
        code_builder.add_instruction("call", write_fun.get_label(program_state))
        code_builder.add_global_function(write_fun)

    def value_type(self, program_state):
        return None


class CallPopFunction(CallFunctionStatement):
    FUNCTION_NAME = "__pop"

    def __init__(self, function_name, args=None):
        super(CallPopFunction, self).__init__(function_name, args)

    def name_mangling(self, function_name, mangled_name):
        self._args[0].name_mangling(function_name, mangled_name)

    def code(self, code_builder, program_state):
        self._args[0].code(code_builder, program_state)
        code_builder.add_instruction("pop", "eax")
        code_builder.add_instruction("mov", "[%s]" % self._args[0].name, "eax")

    def value_type(self, program_state):
        return None


class CallArrayCopyFunction(CallFunctionStatement):
    def __init__(self, function_name, args):
        super(CallArrayCopyFunction, self).__init__(function_name, args)

    def code(self, code_builder, program_state):
        self._code_validation(program_state)
        src = self._args[0].value_type(program_state)
        dist = self._args[2].value_type(program_state)

        self._args[1].code(code_builder, program_state)
        code_builder.add_instruction("mov", "ebx", str(src.sizeof()))
        code_builder.add_instruction("cdq")
        code_builder.add_instruction("imul", "ebx")
        code_builder.add_instruction("mov", "esi", "eax")
        self._args[0].code(code_builder, program_state)
        code_builder.add_instruction("add", "esi", "eax")

        self._args[3].code(code_builder, program_state)
        code_builder.add_instruction("mov", "ebx", str(dist.sizeof()))
        code_builder.add_instruction("cdq")
        code_builder.add_instruction("imul", "ebx")
        code_builder.add_instruction("mov", "edi", "eax")
        self._args[2].code(code_builder, program_state)
        code_builder.add_instruction("add", "edi", "eax")

        self._args[4].code(code_builder, program_state)
        code_builder.add_instruction("mov", "ecx", "eax")
        code_builder.add_instruction("mov", "eax", "edi")
        code_builder.add_instruction("mov", "ebx", "esi")

        arr_copy_function = ArrayCopyFunction(None, self._function_name, self._args)
        arr_copy_function.code(code_builder, program_state)

    def _code_validation(self, program_state):
        if len(self._args) != 5:
            raise SyntaxError(
                "actual and formal argument lists of function %s is differ in length\nrequired: 5\nfound: %d" % (len(
                    self._args), ArrayCopyFunction.FUNCTION_NAME))
        src = self._args[0].value_type(program_state)
        dist = self._args[2].value_type(program_state)
        if not isinstance(src, Array) or src.dimension != 1 or \
                not self._args[1].value_type(program_state) == Type.int or \
                not isinstance(dist, Array) or dist.dimension != 1 or \
                not self._args[3].value_type(program_state) == Type.int or \
                not self._args[4].value_type(program_state) == Type.int:
            raise SyntaxError(
                "function write cannot be applied to given arguments\nrequired: array[] int array[] int int")
        if src.value_type != dist.value_type:
            raise SyntaxError("%s src and dist array type is different" % str(self))

    def value_type(self, program_state):
        return None
