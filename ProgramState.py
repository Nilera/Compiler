class ProgramState(object):
    def __init__(self, function_name=None):
        super(ProgramState, self).__init__()
        self.__function_name = function_name
        self.__variables_dict = {}
        self.__if_counter = 0
        self.__while_counter = 0
        self.__tmp_variable_counter = 0

    def is_global_statement(self):
        return self.__function_name is None

    def add_variable(self, variable):
        self.__variables_dict[variable.name] = variable

    def get_variable(self, variable_name):
        return self.__variables_dict[variable_name]

    def get_if_number(self):
        self.__if_counter += 1
        return self.__if_counter

    def get_while_number(self):
        self.__while_counter += 1
        return self.__while_counter

    def get_tmp_variable_counter(self):
        self.__tmp_variable_counter += 1
        return self.__tmp_variable_counter
