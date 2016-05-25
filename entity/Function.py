from Platform import Platform
from entity.NameMangling import unmangling
from entity.Scalar import Scalar, VariableScalar
from entity.Statement import ReturnStatement
from entity.StatementsContainer import StatementsContainer
from entity.Type import Type


def get_function(return_type, name, params=None, function_state=None):
    """
    :type return_type: entity.Type.Type
    :type name: str
    :type params: list
    :type function_state: list
    :rtype: entity.Function.Function
    """
    if name == MainFunction.FUNCTION_NAME:
        return MainFunction(return_type, name, params, function_state)
    elif name == ReadFunction.FUNCTION_NAME or name == WriteFunction.FUNCTION_NAME or name == ArrayCopyFunction.FUNCTION_NAME or name == LengthFunction.FUNCTION_NAME or name == StrcatFunction.FUNCTION_NAME:
        raise NameError("The name of the function \"%s\" is already taken by standard function" % name)
    else:
        return Function(return_type, name, params, function_state)


class Function(StatementsContainer):
    def __init__(self, return_type, name, params=None, function_state=None):
        """
        :type return_type: entity.Type.Type
        :type name: str
        :type params: list
        :type function_state: list
        """
        super(Function, self).__init__()
        self._return_type = return_type
        self._name = name
        self._params = [] if params is None else params
        for param in self._params:
            from entity.Statement import CallPopFunction
            self.add(CallPopFunction(CallPopFunction.FUNCTION_NAME, [param]))
        self.add_all([] if function_state is None else function_state)

    @property
    def name(self):
        return self._name

    @property
    def params(self):
        return self._params

    def name_mangling(self, supported_information, mangled_name):
        prev_name = self._name
        self._name = "_%s" % self._name
        mangled_name[prev_name] = self._name

    def code(self, code_builder, program_state):
        program_state.set_function_name(self._name)
        program_state.add_function(self)
        code_builder.add_label(self.name)
        code_builder.add_instruction("add", "esp", "4")
        for pop_i in range(len(self._params)):
            self[pop_i].code(code_builder, program_state)
        code_builder.add_instruction("sub", "esp", str(4 * (len(self._params) + 1)))
        for statement_i in range(len(self._params), len(self)):
            self[statement_i].code(code_builder, program_state)
        program_state.set_function_name("")

    def value_type(self, program_state=None):
        return self._return_type

    def validate(self, program_state):
        program_state.set_function_name(self._name)
        program_state.add_function(self)
        if self._return_type is None:
            raise SyntaxError("return type of function %s couldn't be void" % self.unmangling())
        if not self.has_return_statement(self):
            raise SyntaxError("function %s: missing return statement" % self.unmangling())
        for pop_i in range(len(self._params)):
            self[pop_i].validate(program_state)
        for statement_i in range(len(self._params), len(self)):
            self[statement_i].validate(program_state)
        program_state.set_function_name("")

    def unmangling(self):
        return unmangling(self._name)

    def constant_folding(self, cf_state):
        """
        Optimizes code using constant folding and constant propagation.
        :type cf_state: util.ConstantFoldingState.ConstantFoldingState
        """
        cf_state.add_function(self.name, self)
        super().constant_folding(cf_state)

    def is_pure_function(self, cf_state):
        """
        Check is it pure function or not.
        :type cf_state: util.ConstantFoldingState.ConstantFoldingState
        :rtype: bool
        """
        return self.__is_pure_function(self, cf_state)

    def __is_pure_function(self, statement_container, cf_state):
        """
        :type statement_container: entity.StatementContainer.StatementContainer
        :type cf_state: util.ConstantFoldingState.ConstantFoldingState
        :rtype: bool
        """
        from entity.Statement import CallPopFunction, CallFunctionStatement, CallReadFunction, CallWriteFunction
        from entity.Expression import AssignmentOperator
        for statement in statement_container:
            if isinstance(statement, (CallReadFunction, CallWriteFunction)):
                return False
            elif isinstance(statement, AssignmentOperator):
                if isinstance(statement.target, VariableScalar) and cf_state.contains_global_variable(
                        statement.target.value):
                    return False
            elif not isinstance(statement, CallPopFunction) and isinstance(statement, CallFunctionStatement):
                if not cf_state.get_function(statement.name).is_pure_function(cf_state):
                    return False
            elif isinstance(statement, StatementsContainer):
                if not self.__is_pure_function(statement, cf_state):
                    return False
        return True

    def fold_function(self):
        """
        Check is function has only one return statement, and returns return value if it constant.
        :rtype: entity.Scalar.Scalar
        """
        results = self.__fold_function(self)
        if len(results) == 1 and isinstance(results[0], Scalar) and not isinstance(results[0], VariableScalar):
            return results[0]

    def __fold_function(self, statement_container):
        """
        :type statement_container: entity.StatementContainer.StatementContainer
        :rtype: list
        """
        results = []
        from entity.Statement import IfStatement
        for statement in statement_container:
            if isinstance(statement, ReturnStatement):
                results.append(statement.expression)
            elif isinstance(statement, StatementsContainer):
                new_result = self.__fold_function(statement)
                if new_result is not None:
                    results.extend(new_result)
                if isinstance(statement, IfStatement) and statement.else_statement is not None:
                    new_result = self.__fold_function(statement)
                if new_result is not None:
                    results.extend(new_result)

        return results

    def __str__(self):
        params = "" if self._params is None else ", ".join(var.name for var in self._params)
        return "fun %s(%s) -> %s\n" % (self._name, str(params), str(self._return_type)) + super().__str__()


class MainFunction(Function):
    FUNCTION_NAME = "main"

    def __init__(self, return_type, name, params=None, function_state=None):
        super(MainFunction, self).__init__(return_type, name, params, function_state)

    def code(self, code_builder, program_state):
        program_state.set_function_name(self._name)
        if code_builder.platform == Platform.win32:
            code_builder.add_label("_%s" % self.FUNCTION_NAME)
        else:
            code_builder.add_label(self.FUNCTION_NAME)
        for statement in self:
            statement.code(code_builder, program_state)
        if code_builder.platform == Platform.win32:
            code_builder.add_extern_exit()
            code_builder.add_instruction("push", "0")
            code_builder.add_instruction("call", "[__imp__ExitProcess@4]")
        else:
            code_builder.add_instruction("ret")
        program_state.set_function_name("")

    def value_type(self, program_state=None):
        return None

    def validate(self, program_state):
        program_state.set_function_name(self._name)
        if self._return_type is not None:
            raise SyntaxError(
                "function main must return a value of type void, please define the main function as:\nvoid main()")
        if self._params is not None and len(self._params) != 0:
            raise SyntaxError("function main not found, please define the main function as:\n void main()")
        has_return_statement = self.has_return_statement(self)
        if has_return_statement is None or has_return_statement:
            raise SyntaxError("function %s shouldn't have return statement" % self.name)
        for statement in self:
            statement.validate(program_state)
        program_state.set_function_name("")


class ReadFunction(Function):
    FUNCTION_NAME = "read"

    def __init__(self, return_type, name, params, function_state=None):
        super(ReadFunction, self).__init__(return_type, name, params, function_state)
        self.__global_function_number = None

    def code(self, code_builder, program_state):
        program_state.set_function_name(self._name)
        format_string = self._params[0].value_type(program_state).format_string()
        code_builder.add_extern_scanf()
        code_builder.add_label(self.get_label(program_state))
        from entity.Array import ArrayGetter
        from entity.Array import Array
        if isinstance(self._params[0].value_type(program_state), (Array, ArrayGetter)):
            self._params[0].code(code_builder, program_state)
            code_builder.add_instruction("push", "eax")
        else:
            code_builder.add_instruction("push", self._params[0].value)
        code_builder.add_instruction("push", format_string[0])
        if code_builder.platform == Platform.win32:
            code_builder.add_instruction("call", "[__imp__scanf]")
        else:
            code_builder.add_instruction("call", "scanf")
        code_builder.add_instruction("add", "esp", "8")
        code_builder.add_instruction("ret")
        code_builder.add_data(format_string[0], format_string[1], format_string[2])
        program_state.set_function_name("")

    def get_label(self, program_state):
        """
        :param program_state: ProgramState.ProgramState
        :rtype: str
        """
        if self.__global_function_number is None:
            self.__global_function_number = program_state.get_global_function_number()
        return "__%s_%d" % (self._name, self.__global_function_number)

    def value_type(self, program_state=None):
        return None

    def validate(self, program_state):
        program_state.set_function_name(self._name)
        from entity.Array import ArrayGetter
        from entity.Array import Array
        if isinstance(self._params[0].value_type(program_state), (Array, ArrayGetter)):
            self._params[0].validate(program_state)
        program_state.set_function_name("")


class WriteFunction(Function):
    FUNCTION_NAME = "write"

    def __init__(self, return_type, name, params, function_state=None):
        super(WriteFunction, self).__init__(return_type, name, params, function_state)
        self.__global_function_number = None

    def code(self, code_builder, program_state):
        program_state.set_function_name(self._name)
        format_string = self._params[0].value_type(program_state).format_string()
        code_builder.add_extern_printf()
        code_builder.add_label(self.get_label(program_state))
        self._params[0].code(code_builder, program_state)
        code_builder.add_instruction("push", "eax")
        code_builder.add_instruction("push", format_string[0])
        if code_builder.platform == Platform.win32:
            code_builder.add_instruction("call", "[__imp__printf]")
        else:
            code_builder.add_instruction("call", "printf")
        code_builder.add_instruction("add", "esp", "8")
        code_builder.add_instruction("ret")
        code_builder.add_data(format_string[0], format_string[1], format_string[2])
        program_state.set_function_name("")

    def get_label(self, program_state):
        """
        :param program_state: ProgramState.ProgramState
        :rtype: str
        """
        if self.__global_function_number is None:
            self.__global_function_number = program_state.get_global_function_number()
        return "__%s_%d" % (self._name, self.__global_function_number)

    def value_type(self, program_state=None):
        return None

    def validate(self, program_state):
        program_state.set_function_name(self._name)
        self._params[0].validate(program_state)
        program_state.set_function_name("")


class ArrayCopyFunction(Function):
    FUNCTION_NAME = "arraycopy"

    def __init__(self, return_type, name, params, function_state=None):
        super(ArrayCopyFunction, self).__init__(return_type, name, params, function_state)

    def code(self, code_builder, program_state):
        src_value_type = self._params[0]
        label = "copy_loop_%d" % program_state.get_while_number()
        code_builder.add_label(label)
        if src_value_type == Type.char:
            code_builder.add_instruction("mov", "dl", "[eax]")
            code_builder.add_instruction("mov", "[ebx]", "dl")
        else:
            code_builder.add_instruction("mov", "edx", "[eax]")
            code_builder.add_instruction("mov", "[ebx]", "edx")
        code_builder.add_instruction("add", "eax", src_value_type.sizeof())
        code_builder.add_instruction("add", "ebx", src_value_type.sizeof())
        code_builder.add_instruction("loop", label)

    def value_type(self, program_state=None):
        return None

    def validate(self, program_state):
        pass


class StrcatFunction(Function):
    """
    Copy of arraycopy function for string only.
    """
    FUNCTION_NAME = "strcat"

    def __init__(self, return_type, name, params, function_state=None):
        super(StrcatFunction, self).__init__(return_type, name, params, function_state)

    def code(self, code_builder, program_state):
        pass

    def value_type(self, program_state=None):
        return None

    def validate(self, program_state):
        pass


class LengthFunction(Function):
    FUNCTION_NAME = "length"

    def __init__(self, return_type, name, params, function_state=None):
        super(LengthFunction, self).__init__(return_type, name, params, function_state)

    def code(self, code_builder, program_state):
        src = self._params[0].value_type(program_state)
        self._params[0].code(code_builder, program_state)
        if src.value_type == Type.char:
            code_builder.add_instruction("xor", "ecx", "ecx")
            label = "__length_%d" % program_state.get_if_number()
            label_exit = "%s_exit" % label
            code_builder.add_label(label)
            code_builder.add_instruction("mov", "bl", "[eax]")
            code_builder.add_instruction("cmp", "bl", 0)
            code_builder.add_instruction("jz", label_exit)
            code_builder.add_instruction("inc", "eax")
            code_builder.add_instruction("inc", "ecx")
            code_builder.add_instruction("jmp", label)
            code_builder.add_label(label_exit)
        code_builder.add_instruction("mov", "eax", "ecx")

    def value_type(self, program_state=None):
        return Type.int

    def validate(self, program_state):
        self._params[0].validate(program_state)
