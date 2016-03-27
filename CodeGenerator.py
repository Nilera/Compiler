class CodeGenerator(object):
    def windows_code(self, code_builder, function_state):
        raise NotImplementedError

    def linux_code(self, code_builder, function_state):
        return self.windows_code(code_builder, function_state)
