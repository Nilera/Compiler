from entity.NameMangling import NameMangling
from entity.StatementsContainer import StatementsContainer


def get_function(return_type, name, params=None, function_state=None):
    if name == MainFunction.FUNCTION_NAME:
        return MainFunction(return_type, name, params, function_state)
    elif name == ReadFunction.FUNCTION_NAME or name == WriteFunction.FUNCTION_NAME:
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
            raise SyntaxError("return type of function %s couldn't be void" % name)
        try:
            from entity.Statement import ReturnStatement
            statements = [] if function_state is None else function_state
            next(x for x in statements if isinstance(x, ReturnStatement))
        except StopIteration:
            raise SyntaxError("function %s has no return statement" % name)

    @property
    def name(self):
        return self._name

    def name_mangling(self, supported_information, mangled_name):
        prev_name = self._name
        self._name = "_%s" % self._name
        mangled_name[prev_name] = self._name

    def windows_code(self, code_builder, program_state):
        program_state.set_function_name(self._name)
        program_state.add_function(self)
        code_builder.add_label(self.name)
        code_builder.add_instruction("add", "esp", "4")
        for pop_i in range(len(self._params)):
            self[pop_i].windows_code(code_builder, program_state)
        code_builder.add_instruction("sub", "esp", str(4 * (len(self._params) + 1)))
        for statement_i in range(len(self._params), len(self)):
            self[statement_i].windows_code(code_builder, program_state)
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
        try:
            from entity.Statement import ReturnStatement
            statements = [] if function_state is None else function_state
            next(x for x in statements if isinstance(x, ReturnStatement))
            raise SyntaxError("function %s shouldn't have return statement" % name)
        except StopIteration:
            pass

    def windows_code(self, code_builder, program_state):
        program_state.set_function_name(self._name)
        code_builder.add_label(self.name)
        for statement in self:
            statement.windows_code(code_builder, program_state)
        program_state.set_function_name("")

    def value_type(self, program_state=None):
        return None


class ReadFunction(Function):
    FUNCTION_NAME = "read"

    def __init__(self, return_type, name, params, function_state=None):
        super(ReadFunction, self).__init__(return_type, name, params, function_state)

    def _validate(self, return_type, name, params=None, function_state=None):
        pass

    def windows_code(self, code_builder, program_state):
        program_state.set_function_name(self._name)
        format_string = self._params[0].value_type(program_state).format_string()
        code_builder.add_extern("__imp__scanf")
        code_builder.add_label(self.get_label())
        code_builder.add_instruction("push", self._params[0].value)
        code_builder.add_instruction("push", format_string[0])
        code_builder.add_instruction("call", "[__imp__scanf]")
        code_builder.add_instruction("add", "esp", "8")
        code_builder.add_instruction("ret")
        code_builder.add_data(format_string[0], format_string[1], format_string[2])
        program_state.set_function_name("")

    def get_label(self):
        return "__%s_%s" % (self._name, str(self._params[0]))

    def value_type(self, program_state=None):
        return None


class WriteFunction(Function):
    FUNCTION_NAME = "write"

    def __init__(self, return_type, name, params, function_state=None):
        super(WriteFunction, self).__init__(return_type, name, params, function_state)

    def _validate(self, return_type, name, params=None, function_state=None):
        pass

    def windows_code(self, code_builder, program_state):
        program_state.set_function_name(self._name)
        format_string = self._params[0].value_type(program_state).format_string()
        code_builder.add_extern("__imp__printf")
        code_builder.add_label(self.get_label())
        self._params[0].windows_code(code_builder, program_state)
        code_builder.add_instruction("push", "eax")
        code_builder.add_instruction("push", format_string[0])
        code_builder.add_instruction("call", "[__imp__printf]")
        code_builder.add_instruction("add", "esp", "8")
        code_builder.add_instruction("ret")
        code_builder.add_data(format_string[0], format_string[1], format_string[2])
        program_state.set_function_name("")

    def get_label(self):
        return "__%s_%s" % (self._name, str(self._params[0]))

    def value_type(self, program_state=None):
        return None
