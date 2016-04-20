from entity.CodeGenerator import CodeGenerator
from entity.Function import Function
from entity.NameMangling import NameMangling
from entity.StatementsContainer import StatementsContainer
from entity.Variable import Variable


class Program(StatementsContainer):
    def __init__(self):
        super(Program, self).__init__()

    def name_mangling(self, function_name=None, mangled_name=None):
        program_name_mangling = {}
        for statement in self:
            if isinstance(statement, Function):
                statement.name_mangling("", program_name_mangling)
                function_name_mangling = program_name_mangling.copy()
                for state in statement:
                    if isinstance(state, NameMangling):
                        state.name_mangling(statement.name, function_name_mangling)
            elif isinstance(statement, Variable):
                statement.name_mangling(None, program_name_mangling)

    def code(self, code_builder, program_state):
        for statement in self:
            if isinstance(statement, CodeGenerator):
                statement.code(code_builder, program_state)

    def value_type(self, program_state):
        return None

    def unmangling(self):
        pass
