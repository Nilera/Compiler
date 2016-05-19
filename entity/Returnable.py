class Returnable(object):
    def value_type(self, program_state):
        """
        :type program_state: ProgramState.ProgramState
        :rtype: entity.Type.Type | entity.Array.Array
        """
        raise NotImplementedError
