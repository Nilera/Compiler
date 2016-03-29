from entity.StatementsContainer import StatementsContainer


def get_function(return_type, name, params=None, function_state=None):
    if name == MainFunction.FUNCTION_NAME:
        return MainFunction(return_type, name, params, function_state)
    elif name == ReadFunction.FUNCTION_NAME:
        raise NameError("The name of the function \"%s\" is already taken" % name)
    elif name == WriteFunction.FUNCTION_NAME:
        raise NameError("The name of the function \"%s\" is already taken" % name)
    else:
        return Function(return_type, name, params, function_state)


class Function(StatementsContainer):
    def __init__(self, return_type, name, params=None, function_state=None):
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

    def __str__(self):
        params = "" if self._params is None else ", ".join(var.name for var in self._params)
        return "fun %s(%s) -> %s\n" % (self._name, str(params), str(self._return_type)) + super().__str__()


class MainFunction(Function):
    FUNCTION_NAME = "main"

    def __init__(self, return_type, name, params=None, function_state=None):
        super(MainFunction, self).__init__(return_type, name, params, function_state)

    def windows_code(self, code_builder, program_state):
        program_state.set_function_name(self._name)
        code_builder.add_label(self.name)
        for statement in self:
            from entity.Statement import ReturnStatement
            if isinstance(statement, ReturnStatement):
                statement.windows_code(code_builder, program_state, True)
            else:
                statement.windows_code(code_builder, program_state)
        program_state.set_function_name("")

    def value_type(self, program_state=None):
        return None


class ReadFunction(Function):
    FUNCTION_NAME = "read"

    def __init__(self, return_type, name, params, function_state=None):
        super(ReadFunction, self).__init__(return_type, name, params, function_state)

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
