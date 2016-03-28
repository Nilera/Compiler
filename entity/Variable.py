from CodeGenerator import CodeGenerator
from NameMangling import NameMangling
from entity.Scalar import IntScalar, BoolScalar


class Variable(NameMangling, CodeGenerator):
    def __init__(self, value_type, name, expression=None):
        self.__value_type = value_type
        self.__name = name
        self.__expression = expression

    @property
    def value_type(self):
        return self.__value_type

    @property
    def name(self):
        return self.__name

    @property
    def expression(self):
        return self.__expression

    def name_mangling(self, function_name, mangled_name):
        prev_name = self.__name
        self.__name = "%s_%s" % (function_name, prev_name)
        if isinstance(self.__expression, NameMangling):
            self.__expression.name_mangling(function_name, mangled_name)
        mangled_name[prev_name] = self.__name

    def windows_code(self, code_builder, program_state):
        program_state.add_variable(self)
        if self.expression is None:
            code_builder.add_data(self.name, "dw", self.value_type.default_value())
        elif isinstance(self.expression, (IntScalar, BoolScalar)):
            code_builder.add_data(self.name, "dw", self.expression.value)
        else:
            if program_state.is_global_statement():
                pass
            else:
                pass

    def __str__(self):
        assign = "" if self.__expression is None else " = %s" % str(self.__expression)
        return "%s %s" % (str(self.__value_type), self.__name) + assign
