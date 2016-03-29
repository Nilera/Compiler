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

    def windows_code(self, code_generator, program_state):
        raise NotImplementedError

    def value_type(self, program_state):
        raise NotImplementedError

    def __str__(self):
        return "\n".join("%d  %s" % (i, str(self[i])) for i in range(len(self)))
