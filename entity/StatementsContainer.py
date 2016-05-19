from entity.CodeGenerator import CodeGenerator
from entity.NameMangling import NameMangling


class StatementsContainer(NameMangling, CodeGenerator):
    def __init__(self):
        super(StatementsContainer, self).__init__()
        self._statements = []

    def __getitem__(self, index):
        return self._statements[index]

    def __len__(self):
        return len(self._statements)

    def add(self, statement):
        self._statements.append(statement)

    def add_all(self, statements):
        self._statements.extend(statements)

    def name_mangling(self, function_name, mangled_name):
        for statement in self:
            statement.name_mangling(function_name, mangled_name)

    def code(self, code_generator, program_state):
        raise NotImplementedError

    def value_type(self, program_state):
        raise NotImplementedError

    def unmangling(self):
        return NotImplementedError

    # True - has return statement, False - otherwise and None if it is incorrect StatementContainer
    def has_return_statement(self, statements):
        from entity.Statement import ReturnStatement
        from entity.Statement import IfStatement
        result = False
        for index in range(len(statements)):
            statement = statements[index]
            if isinstance(statement, ReturnStatement):
                return self.__has_return_statement_return(index, statements)
            elif isinstance(statement, IfStatement):
                result = self.__has_return_statement_if(statement)
            elif isinstance(statement, StatementsContainer):
                res = statement.has_return_statement(statement)
                result = None if res is None or res else False
        return result

    def __has_return_statement_return(self, index, statements):
        if index + 1 != len(statements):
            raise SyntaxError("program contains unreachable statements")
        return True

    def __has_return_statement_if(self, if_statement):
        if_node = if_statement
        else_node = if_statement.else_statement
        if_res = if_node.has_return_statement(if_node)
        if else_node is None:
            return None if if_res is None or if_res else False
        else:
            else_res = else_node.has_return_statement(else_node)
            if if_res and else_res:
                return True
            elif not if_res and not else_res:
                return False
            else:
                return None

    def __str__(self):
        return "\n".join("%d  %s" % (i, str(self[i])) for i in range(len(self)))
