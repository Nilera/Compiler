from entity.Returnable import Returnable


class CodeGenerator(Returnable):
    def code(self, code_builder, program_state):
        """
        :type code_builder: CodeBuilder.CodeBuilder
        :type program_state: ProgramState.ProgramState
        :rtype: None
        """
        raise NotImplementedError

    def value_type(self, program_state):
        """
        :type program_state: ProgramState.ProgramState
        :rtype: entity.Type.Type | entity.Array.Array
        """
        raise NotImplementedError
