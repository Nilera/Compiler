from operator import contains

from entity.Array import Array
from entity.CodeElement import CodeElement
from entity.Expression import Plus
from entity.Function import ReadFunction, WriteFunction, MainFunction, ArrayCopyFunction, LengthFunction, StrcatFunction
from entity.NameMangling import unmangling
from entity.Scalar import VariableScalar, IntScalar
from entity.StatementsContainer import StatementsContainer
from entity.Type import Type
from entity.Variable import Variable


class WhileStatement(StatementsContainer):
    def __init__(self, condition, statements):
        """
        :type condition: entity.Expression.Operator | entity.Scalar.Scalar
        :type statements: list
        """
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
        self.__condition.code(code_builder, program_state)
        code_builder.add_instruction("cmp", "eax", "0")
        code_builder.add_instruction("je", exit_label)
        for statement in self:
            statement.code(code_builder, program_state)
        code_builder.add_instruction("jmp", label)
        code_builder.add_label(exit_label)

    def value_type(self, program_state):
        return None

    def validate(self, program_state):
        super().validate(program_state)
        if self.__condition.value_type(program_state) == Type.boolean:
            self.__condition.validate(program_state)
        else:
            raise SyntaxError("while condition should be boolean value or boolean expression")

    def unmangling(self):
        return ""

    def constant_folding(self, cf_state):
        """
        Optimizes code using constant folding and constant propagation.
        :type cf_state: util.ConstantFoldingState.ConstantFoldingState
        """
        for statement in self:
            if not isinstance(statement, Variable):
                statement.constant_folding(cf_state)
        cond = self.__condition.constant_folding(cf_state)
        if cond is not None:
            self.__condition = cond

    def __str__(self):
        return "while %s \n" % str(self.__condition) + super().__str__()


class IfStatement(StatementsContainer):
    def __init__(self, condition, statements, else_statement=None):
        """
        :type condition: entity.Expression.Operator | entity.Scalar.Scalar
        :type statements: list
        :type else_statement: entity.Statement.ElseStatement
        """
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
        if self.__else_statement is not None:
            self.__else_statement.name_mangling(function_name, mangled_name)

    def code(self, code_builder, program_state):
        label = "%s_if_%d" % (program_state.function_name, program_state.get_if_number())
        exit_label = "%s_exit" % label
        self.__condition.code(code_builder, program_state)
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

    def validate(self, program_state):
        super().validate(program_state)
        if self.__condition.value_type(program_state) == Type.boolean:
            self.__condition.validate(program_state)
        else:
            raise SyntaxError("if condition should be boolean value or boolean expression")

    def unmangling(self):
        return ""

    def constant_folding(self, cf_state):
        """
        Optimizes code using constant folding and constant propagation.
        :type cf_state: util.ConstantFoldingState.ConstantFoldingState
        """
        for statement in self:
            if not isinstance(statement, Variable):
                statement.constant_folding(cf_state)
        cond = self.__condition.constant_folding(cf_state)
        if cond is not None:
            self.__condition = cond
        if self.__else_statement is not None:
            self.__else_statement.constant_folding(cf_state)

    def __str__(self):
        else_statement = "" if self.__else_statement is None else str(self.__else_statement)
        return "if %s \n" % str(self.__condition) + super().__str__() + else_statement


class ElseStatement(StatementsContainer):
    def __init__(self, statements):
        """
        :type statements: list
        """
        super(ElseStatement, self).__init__()
        self.add_all(statements)

    def code(self, code_builder, program_state):
        for statement in self:
            statement.code(code_builder, program_state)

    def value_type(self, program_state):
        return None

    def unmangling(self):
        return ""

    def constant_folding(self, cf_state):
        """
        Optimizes code using constant folding and constant propagation.
        :type cf_state: util.ConstantFoldingState.ConstantFoldingState
        """
        for statement in self:
            if not isinstance(statement, Variable):
                statement.constant_folding(cf_state)

    def __str__(self):
        return "else\n" + "\n".join("\t%d  %s" % (i, str(self[i])) for i in range(len(self)))


class ReturnStatement(CodeElement):
    def __init__(self, expression):
        """
        :type expression: entity.CodeElement.CodeElement
        """
        self.__expression = expression

    def name_mangling(self, function_name, mangled_name):
        self.__expression.name_mangling(function_name, mangled_name)

    def code(self, code_builder, program_state):
        self.__expression.code(code_builder, program_state)
        code_builder.add_instruction("push", "eax")
        code_builder.add_instruction("add", "esp", "4")
        code_builder.add_instruction("ret")

    def value_type(self, program_state):
        return None

    def validate(self, program_state):
        if isinstance(self.__expression.value_type(program_state), Array):
            raise SyntaxError("function couldn't return array")

    def unmangling(self):
        return ""

    def constant_folding(self, cf_state):
        """
        Optimizes code using constant folding and constant propagation.
        :type cf_state: util.ConstantFoldingState.ConstantFoldingState
        """
        res = self.__expression.constant_folding(cf_state)
        if res is not None:
            self.__expression = res

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
    elif function_name == LengthFunction.FUNCTION_NAME:
        return CallLengthFunction(function_name, args)
    elif function_name == StrcatFunction.FUNCTION_NAME:
        return CallStrcatFunction(function_name, args)
    else:
        return CallFunctionStatement(function_name, args)


class CallFunctionStatement(CodeElement):
    def __init__(self, function_name, args=None):
        """
        :type function_name: str
        :type args: list
        """
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
        for arg in reversed(self._args):
            arg.code(code_builder, program_state)
            code_builder.add_instruction("push", "eax")
        code_builder.add_instruction("call", self._function_name)
        code_builder.add_instruction("sub", "esp", "8")
        code_builder.add_instruction("pop", "eax")
        code_builder.add_instruction("add", "esp", str(4 * (len(self._args) + 1)))

    def value_type(self, program_state):
        if not program_state.contains_function(self._function_name):
            raise ValueError("no function \"%s\" in scope" % self.unmangling())
        return program_state.get_function(self._function_name).value_type()

    def validate(self, program_state):
        """
        :type program_state: ProgramState.ProgramState
        :rtype: bool
        """
        if not program_state.contains_function(self._function_name):
            raise SyntaxError("no function \"%s\" in scope" % unmangling(self._function_name))
        params = program_state.get_function(self._function_name).params
        if len(params) != len(self._args) or not self.__is_valid_params(params, program_state):
            raise SyntaxError(
                "function %s cannot be applied to given types\nrequired: %s\nfound: %s" % (
                    self._function_name,
                    "no arguments" if len(params) == 0 else ", ".join(str(x.value_type(program_state)) for x in params),
                    "no arguments" if len(params) == 0 else ", ".join(
                        str(x.value_type(program_state)) for x in self._args)))
        for arg in reversed(self._args):
            arg.validate(program_state)

    def __is_valid_params(self, params, program_state):
        """
        :type params: list
        :type program_state: ProgramState.ProgramState
        :rtype: bool
        """
        for i in range(len(params)):
            arg1 = params[i].value_type(program_state)
            arg2 = self._args[i].value_type(program_state)
            if arg1 != arg2:
                return False
        return True

    def unmangling(self):
        args = "" if self._args is None else ", ".join(arg.unmangling() for arg in self._args)
        return "%s(%s)" % (unmangling(self._function_name), args)

    def constant_folding(self, cf_state):
        """
        Optimizes code using constant folding and constant propagation.
        :type cf_state: util.ConstantFoldingState.ConstantFoldingState
        """
        # TODO: try to make constant function
        for i in range(len(self._args)):
            arg = self._args[i].constant_folding(cf_state)
            if arg is not None:
                self._args[i] = arg

    def __str__(self):
        args = "" if self._args is None else ", ".join(str(arg) for arg in self._args)
        return "%s(%s)" % (self._function_name, args)


class CallReadFunction(CallFunctionStatement):
    def __init__(self, function_name, args):
        super(CallReadFunction, self).__init__(function_name, args)

    def code(self, code_builder, program_state):
        arr_param = self._args[0].value_type(program_state)
        if not isinstance(self._args[0], VariableScalar) and not (
                    isinstance(arr_param, Array) and arr_param.value_type == Type.char):
            raise SyntaxError("function 'read' cannot be applied to given arguments")
        read_fun = ReadFunction(None, self._function_name, self._args)
        code_builder.add_instruction("call", read_fun.get_label(program_state))
        code_builder.add_global_function(read_fun)

    def value_type(self, program_state):
        return None

    def validate(self, program_state):
        if len(self._args) != 1:
            raise SyntaxError(
                "actual and formal argument lists of function read is differ in length\nrequired: 1\nfound: %d" % len(
                    self._args))

    def constant_folding(self, cf_state):
        """
        Optimizes code using constant folding and constant propagation.
        :type cf_state: util.ConstantFoldingState.ConstantFoldingState
        """
        var_name = self._args[0].value
        if cf_state.contains_variable(var_name):
            cf_state.remove_variable(var_name)


class CallWriteFunction(CallFunctionStatement):
    def __init__(self, function_name, args):
        super(CallWriteFunction, self).__init__(function_name, args)

    def code(self, code_builder, program_state):
        write_fun = WriteFunction(None, self._function_name, self._args)
        code_builder.add_instruction("call", write_fun.get_label(program_state))
        code_builder.add_global_function(write_fun)

    def value_type(self, program_state):
        return None

    def validate(self, program_state):
        if len(self._args) != 1:
            raise SyntaxError(
                "actual and formal argument lists of function write is differ in length\nrequired: 1\nfound: %d" % len(
                    self._args))
        if not isinstance(self._args[0].value_type(program_state), (Type, Array)):
            raise SyntaxError(
                "function 'write' cannot be applied to given arguments\nrequired: int, boolean, char or char[]")

    def constant_folding(self, cf_state):
        """
        Optimizes code using constant folding and constant propagation.
        :type cf_state: util.ConstantFoldingState.ConstantFoldingState
        """
        for i in range(len(self._args)):
            arg = self._args[i].constant_folding(cf_state)
            if arg is not None:
                self._args[i] = arg


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

    def validate(self, program_state):
        self._args[0].validate(program_state)

    def constant_folding(self, cf_state):
        """
        Optimizes code using constant folding and constant propagation.
        :type cf_state: util.ConstantFoldingState.ConstantFoldingState
        """
        return None


class CallArrayCopyFunction(CallFunctionStatement):
    def __init__(self, function_name, args):
        super(CallArrayCopyFunction, self).__init__(function_name, args)

    def code(self, code_builder, program_state):
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
        code_builder.add_instruction("mov", "eax", "esi")
        code_builder.add_instruction("mov", "ebx", "edi")

        arr_copy_function = ArrayCopyFunction(None, self._function_name, [src.value_type])
        arr_copy_function.code(code_builder, program_state)

    def validate(self, program_state):
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
                "function 'arraycopy' cannot be applied to given arguments\nrequired: array[] int array[] int int")
        if src.value_type != dist.value_type:
            raise SyntaxError("%s src and dist array type is different" % str(self))
        for arg in reversed(self._args):
            arg.validate(program_state)

    def value_type(self, program_state):
        return None

    def constant_folding(self, cf_state):
        """
        Optimizes code using constant folding and constant propagation.
        :type cf_state: util.ConstantFoldingState.ConstantFoldingState
        """
        return None


class CallStrcatFunction(CallFunctionStatement):
    def __init__(self, function_name, args):
        super(CallStrcatFunction, self).__init__(function_name, args)

    def code(self, code_builder, program_state):
        dist = self._args[0]
        src = self._args[1]
        dist_length = LengthFunction(Type.int, LengthFunction.FUNCTION_NAME, [dist])
        src_length = LengthFunction(Type.int, LengthFunction.FUNCTION_NAME, [src])
        call_arraycopy = CallArrayCopyFunction(self._function_name,
                                               [src, IntScalar("0"), dist, dist_length,
                                                Plus(src_length, IntScalar("1"))])
        call_arraycopy.code(code_builder, program_state)

    def validate(self, program_state):
        if len(self._args) != 2:
            raise SyntaxError(
                "actual and formal argument lists of function %s is differ in length\nrequired: 2\nfound: %d" % (len(
                    self._args), ArrayCopyFunction.FUNCTION_NAME))
        dist = self._args[0].value_type(program_state)
        src = self._args[1].value_type(program_state)
        if not isinstance(src, Array) or src.dimension != 1 or src.value_type != Type.char or \
                not isinstance(dist, Array) or dist.dimension != 1 or dist.value_type != Type.char:
            raise SyntaxError(
                "function 'strcat' cannot be applied to given arguments\nrequired: char[] char[]")
        for arg in reversed(self._args):
            arg.validate(program_state)

    def value_type(self, program_state):
        return None

    def constant_folding(self, cf_state):
        """
        Optimizes code using constant folding and constant propagation.
        :type cf_state: util.ConstantFoldingState.ConstantFoldingState
        """
        return None


class CallLengthFunction(CallFunctionStatement):
    def __init__(self, function_name, args):
        super(CallLengthFunction, self).__init__(function_name, args)

    def code(self, code_builder, program_state):
        length_function = LengthFunction(Type.int, self._function_name, self._args)
        length_function.code(code_builder, program_state)

    def validate(self, program_state):
        if len(self._args) != 1:
            raise SyntaxError(
                "actual and formal argument lists of function %s is differ in length\nrequired: 1\nfound: %d" % (len(
                    self._args), ArrayCopyFunction.FUNCTION_NAME))
        if not isinstance(self._args[0].value_type(program_state), Array):
            raise SyntaxError(
                "function 'length' cannot be applied to given arguments\nrequired: array[]")
        for arg in reversed(self._args):
            arg.validate(program_state)

    def value_type(self, program_state):
        return Type.int

    def constant_folding(self, cf_state):
        """
        Optimizes code using constant folding and constant propagation.
        :type cf_state: util.ConstantFoldingState.ConstantFoldingState
        """
        return None
