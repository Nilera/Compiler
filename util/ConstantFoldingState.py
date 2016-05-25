from operator import contains


class ConstantFoldingState(object):
    def __init__(self):
        self.__global_variables = set()
        self.__variables = {}
        self.__functions = {}
        self.__constant_functions = []

    def add_global_variable(self, variable_name):
        """
        :type variable_name: str
        """
        self.__global_variables.add(variable_name)

    def contains_global_variable(self, variable_name):
        """
        :type variable_name: str
        :rtype: bool
        """
        return contains(self.__global_variables, variable_name)

    def add_variable(self, variable_name, value):
        """
        :type variable_name: str
        :type value: entity.Scalar.Scalar
        """
        self.__variables[variable_name] = value

    def get_variable(self, variable_name):
        """
        :type variable_name: str
        :rtype: entity.Scalar.Scalar
        """
        return self.__variables[variable_name]

    def contains_variable(self, variable_name):
        """
        :type variable_name: str
        :rtype: bool
        """
        return contains(self.__variables, variable_name)

    def remove_variable(self, variable_name):
        """
        :type variable_name: str
        """
        del self.__variables[variable_name]

    def add_function(self, function_name, function):
        """
        :type function_name: str
        :type function: entity.Function.Function
        """
        self.__functions[function_name] = function

    def get_function(self, function_name):
        """
        :type function_name: str
        :rtype: entity.Function.Function
        """
        return self.__functions[function_name]

    def contains_function(self, function_name):
        """
        :type function_name: str
        :rtype: bool
        """
        return contains(self.__functions, function_name)

    def add_constant_function(self, function):
        """
        :type function: entity.Function.Function
        """
        for fun in self.__constant_functions:
            if fun.name == function.name:
                return
        self.__constant_functions.append(function)

    def get_constant_functions(self):
        """
        :rtype: list
        """
        return self.__constant_functions
