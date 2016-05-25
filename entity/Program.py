from entity.Expression import AssignmentOperator
from entity.Function import Function
from entity.NameMangling import NameMangling
from entity.Statement import CallReadFunction
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
            statement.code(code_builder, program_state)

    def value_type(self, program_state):
        return None

    def unmangling(self):
        pass

    def constant_folding(self, cf_state):
        """
        Optimizes code using constant folding and constant propagation.
        :type cf_state: util.ConstantFoldingState.ConstantFoldingState
        """
        for statement in self:
            if isinstance(statement, Variable):
                statement.constant_folding(cf_state)
            elif isinstance(statement, Function):
                self.__global_variable_check(cf_state, statement)
        for statement in self:
            if isinstance(statement, Function):
                statement.constant_folding(cf_state)
        for function in cf_state.get_constant_functions():
            self._statements.insert(0, function)

    def __global_variable_check(self, cf_state, statement_container):
        """
        Finds global variable using in function and if assignment operator is used in relation to it, it will remove
        from the list of constants.
        :type cf_state: util.ConstantFoldingState.ConstantFoldingState
        :type statement_container: entity.StatementContainer
        """
        for statement in statement_container:
            if isinstance(statement, StatementsContainer):
                self.__global_variable_check(cf_state, statement)
            elif isinstance(statement, (AssignmentOperator, CallReadFunction)):
                statement.constant_folding(cf_state)
