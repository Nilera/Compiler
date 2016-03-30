from entity.Returnable import Returnable


class CodeGenerator(Returnable):
    def code(self, code_builder, program_state):
        raise NotImplementedError

    def value_type(self, program_state):
        raise NotImplementedError
