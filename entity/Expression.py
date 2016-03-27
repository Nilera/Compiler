from operator import contains

from entity.CodeGenerator import CodeGenerator
from entity.NameMangling import NameMangling


class Expression(NameMangling, CodeGenerator):
    def __init__(self, value, left=None, right=None):
        self.__value = value
        self.__left = left
        self.__right = right

    # def eval(self, variable_state=None):
    #     if variable_state is None:
    #         variable_state = {}
    #     if self.__right is None:  # leaf of expression tree: variable or pure value (int or bool)
    #         return self.__get_value(variable_state)
    #     elif self.__left is None:  # unary operation
    #         return (-1 if self.__value == '-' else 1) * self.__right.eval(variable_state)
    #     else:  # binary operation
    #         left_val = self.__left.eval(variable_state)
    #         right_val = self.__right.eval(variable_state)
    #         reduced_expression = "%s %s %s" % (str(left_val), self.__value, str(right_val))
    #         return eval(reduced_expression)
    #
    # def __get_value(self, variable_state):
    #     if isinstance(self.__value, (int, bool)) or self.__value not in variable_state:
    #         return self.__value
    #     else:
    #         return variable_state[self.__value]

    def name_mangling(self, function_name, mangled_name):
        if self.__right is None:  # leaf of expression tree: variable or pure value (int or bool)
            self.__value_name_mangling(mangled_name)
        elif self.__left is None:  # unary operation
            self.__value_name_mangling(mangled_name)
        else:  # binary operation
            self.__left.name_mangling(function_name, mangled_name)
            self.__right.name_mangling(function_name, mangled_name)

    def __value_name_mangling(self, mangled_name):
        if not self.__value.isdigit() and contains(mangled_name, self.__value):
            self.__value = mangled_name[self.__value]

    def code(self):
        raise NotImplementedError

    def __str__(self):
        left_str = "" if self.__left is None else self.__left
        right_str = "" if self.__right is None else self.__right
        return ("%s %s %s" % (left_str, self.__value, right_str)).strip()


class AssignmentOperator(NameMangling, CodeGenerator):
    def __init__(self, name, expression):
        self.__name = name
        self.__expression = expression

    def name_mangling(self, function_name, mangled_name):
        self.__name.name_mangling(function_name, mangled_name)
        self.__expression.name_mangling(function_name, mangled_name)

    def code(self):
        raise NotImplementedError

    def __str__(self):
        return "%s = %s" % (self.__name, self.__expression)
