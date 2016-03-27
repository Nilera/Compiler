class FunctionState(object):
    def __init__(self):
        super(FunctionState, self).__init__()
        self.__if_counter = 0
        self.__while_counter = 0
        self.__tmp_variable_counter = 0

    def get_if_number(self):
        self.__if_counter += 1
        return self.__if_counter

    def get_while_number(self):
        self.__while_counter += 1
        return self.__while_counter

    def get_tmp_variable_counter(self):
        self.__tmp_variable_counter += 1
        return self.__tmp_variable_counter
