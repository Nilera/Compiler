from entity.StatementsContainer import StatementsContainer


class Function(StatementsContainer):
    def __init__(self, return_type, name, params=None, function_state=None):
        super(Function, self).__init__()
        self.__return_type = return_type
        self.__name = name
        self.__params = params

        # add argument of function as local variables
        if params is not None:
            self.add_all(params)
        if function_state is None:
            function_state = []
        self.add_all(function_state)

    @property
    def name(self):
        return self.__name

    def name_mangling(self, supported_information, mangled_name):
        prev_name = self.__name
        self.__name = "_%s" % self.__name
        mangled_name[prev_name] = self.__name

    def windows_code(self, code_builder, function_state):
        pass

    def __str__(self):
        params = "" if self.__params is None else ", ".join(var.name for var in self.__params)
        return "fun %s(%s) -> %s\n" % (self.__name, str(params), str(self.__return_type)) + super().__str__()
