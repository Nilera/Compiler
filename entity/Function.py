from Platform import Platform
from entity.NameMangling import NameMangling
from entity.StatementsContainer import StatementsContainer


def get_function(return_type, name, params=None, function_state=None):
    if name == MainFunction.FUNCTION_NAME:
        return MainFunction(return_type, name, params, function_state)
    elif name == ReadFunction.FUNCTION_NAME or name == WriteFunction.FUNCTION_NAME or ArrayCopyFunction.FUNCTION_NAME:
        raise NameError("The name of the function \"%s\" is already taken by standard function" % name)
    else:
        return Function(return_type, name, params, function_state)


class Function(StatementsContainer):
    def __init__(self, return_type, name, params=None, function_state=None):
        super(Function, self).__init__()
        self._validate(return_type, name, params, function_state)
        self._return_type = return_type
        self._name = name
        self._params = [] if params is None else params
        for param in self._params:
            from entity.Statement import CallPopFunction
            self.add(CallPopFunction(CallPopFunction.FUNCTION_NAME, [param]))
        self.add_all([] if function_state is None else function_state)

    def _validate(self, return_type, name, params=None, function_state=None):
        if return_type is None:
            raise SyntaxError("return type of function %s couldn't be void" % NameMangling.unmangling(name))
        if not self.has_return_statement(function_state):
            raise SyntaxError("function %s: missing return statement" % NameMangling.unmangling(name))

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
        code_builder.add_instruction("add", "esp", "4")
        code_builder.add_instruction("ret")
        program_state.set_function_name("")

    def value_type(self, program_state=None):
        return self._return_type

    def unmangling(self):
        return NameMangling.unmangling(self._name)

    def __str__(self):
        params = "" if self._params is None else ", ".join(var.name for var in self._params)
        return "fun %s(%s) -> %s\n" % (self._name, str(params), str(self._return_type)) + super().__str__()


class MainFunction(Function):
    FUNCTION_NAME = "main"

    def __init__(self, return_type, name, params=None, function_state=None):
        super(MainFunction, self).__init__(return_type, name, params, function_state)

    def _validate(self, return_type, name, params=None, function_state=None):
        if return_type is not None:
            raise SyntaxError(
                "function main must return a value of type void, please define the main function as:\nvoid main()")
        if params is not None:
            raise SyntaxError("function main not found, please define the main function as:\n void main()")
        has_return_statement = self.has_return_statement(function_state)
        if has_return_statement is None or has_return_statement:
            raise SyntaxError("function %s shouldn't have return statement" % name)

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


class ReadFunction(Function):
    FUNCTION_NAME = "read"

    def __init__(self, return_type, name, params, function_state=None):
        super(ReadFunction, self).__init__(return_type, name, params, function_state)
        self.__global_function_number = None

    def _validate(self, return_type, name, params=None, function_state=None):
        pass

    def code(self, code_builder, program_state):
        program_state.set_function_name(self._name)
        format_string = self._params[0].value_type(program_state).format_string()
        code_builder.add_extern_scanf()
        code_builder.add_label(self.get_label(program_state))
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
        if self.__global_function_number is None:
            self.__global_function_number = program_state.get_global_function_number()
        return "__%s_%d" % (self._name, self.__global_function_number)

    def value_type(self, program_state=None):
        return None


class WriteFunction(Function):
    FUNCTION_NAME = "write"

    def __init__(self, return_type, name, params, function_state=None):
        super(WriteFunction, self).__init__(return_type, name, params, function_state)
        self.__global_function_number = None

    def _validate(self, return_type, name, params=None, function_state=None):
        pass

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
        if self.__global_function_number is None:
            self.__global_function_number = program_state.get_global_function_number()
        return "__%s_%d" % (self._name, self.__global_function_number)

    def value_type(self, program_state=None):
        return None


class ArrayCopyFunction(Function):
    FUNCTION_NAME = "arr_copy"

    def __init__(self, return_type, name, params, function_state=None):
        super(ArrayCopyFunction, self).__init__(return_type, name, params, function_state)

    def _validate(self, return_type, name, params=None, function_state=None):
        pass

    def code(self, code_builder, program_state):
        label = "copy_loop_%d" % program_state.get_while_number()
        code_builder.add_label(label)
        code_builder.add_instruction("mov", "edx", "[eax]")
        code_builder.add_instruction("mov", "[ebx]", "edx")
        code_builder.add_instruction("add", "eax", 4)
        code_builder.add_instruction("add", "ebx", 4)
        code_builder.add_instruction("loop", label)

    def value_type(self, program_state=None):
        return None
