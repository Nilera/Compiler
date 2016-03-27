from entity.CodeGenerator import CodeGenerator
from entity.NameMangling import NameMangling


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

    def windows_code(self):
        raise NotImplementedError

    # def eval_expression(self, variable_state=None):
    #     value = self.__expression.eval(variable_state)
    #     if self.__value_type.is_correct_value(value):
    #         return value
    #     else:
    #         type_name = str(self.__value_type)
    #         raise ValueError("Variable %s is not type %s" % (self.__name, type_name))

    def __str__(self):
        assign = "" if self.__expression is None else " = %s" % str(self.__expression)
        return "%s %s" % (str(self.__value_type), self.__name) + assign
