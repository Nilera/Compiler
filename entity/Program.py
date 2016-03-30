from entity.CodeGenerator import CodeGenerator
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

    def code(self, code_builder, program_state):
        for statement in self:
            if isinstance(statement, CodeGenerator):
                statement.code(code_builder, program_state)

    def value_type(self, program_state):
        return None

    def unmangling(self):
        pass
