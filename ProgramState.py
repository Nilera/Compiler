from operator import contains


class ProgramState(object):
    def __init__(self, function_name=""):
        super(ProgramState, self).__init__()
        self.__function_name = function_name
        self.__variables_dict = {}
        self.__function_dict = {}
        self.__if_counter = 0
        self.__while_counter = 0

    def is_global_statement(self):
        return self.__function_name == ""

    @property
    def function_name(self):
        return self.__function_name

    def set_function_name(self, function_name):
        self.__function_name = function_name

    def add_variable(self, variable):
        self.__variables_dict[variable.name] = variable

    def get_variable(self, variable_name):
        return self.__variables_dict[variable_name]

    def contains_variable(self, variable_name):
        return contains(self.__variables_dict, variable_name)

    def add_function(self, function):
        self.__function_dict[function.name] = function

    def get_function(self, function_name):
        return self.__function_dict[function_name]

    def contains_function(self, function_name):
        return contains(self.__function_dict, function_name)

    def get_if_number(self):
        self.__if_counter += 1
        return self.__if_counter

    def get_while_number(self):
        self.__while_counter += 1
        return self.__while_counter
