from entity.Returnable import Returnable


class CodeGenerator(Returnable):
    def windows_code(self, code_builder, program_state):
        raise NotImplementedError

    def linux_code(self, code_builder, program_state):
        return self.windows_code(code_builder, program_state)

    def value_type(self, program_state):
        raise NotImplementedError
