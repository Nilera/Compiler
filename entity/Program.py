from entity.Function import Function
from entity.NameMangling import NameMangling
from entity.StatementsContainer import StatementsContainer


class Program(StatementsContainer):
    def __init__(self):
        super(Program, self).__init__()

    def name_mangling(self, function_name=None, mangled_name=None):
        program_name_mangling = {}
        for function in self:
            if isinstance(function, Function):
                function.name_mangling("", program_name_mangling)
                function_name_mangling = program_name_mangling.copy()
                for state in function:
                    if isinstance(state, NameMangling):
                        state.name_mangling(function.name, function_name_mangling)

    # def get_states_till_to(self, index):
    #     return self._states[0: int(index)]

    # def find_variable(self, name):
    #     for state in self._states:
    #         if isinstance(state, Variable) and state.name == name:
    #             return state
    #     return None

    def windows_code(self):
        raise NotImplementedError
