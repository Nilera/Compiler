from Platform import Platform
from entity.Function import MainFunction


class CodeBuilder(object):
    def __init__(self, program_state, platform):
        super(CodeBuilder, self).__init__()
        self.__externs = set()
        self.__global_variables_initialization = []
        self.__global_functions = []
        self.__main_function_instruction = []
        self.__text_section_instruction = []
        self.__data_section_instruction = set()
        self.__program_state = program_state
        self.__platform = platform

    @property
    def platform(self):
        return self.__platform

    def add_extern_malloc(self):
        if self.platform == Platform.win32:
            self.__add_extern("__imp__malloc")
        else:
            self.__add_extern("malloc")

    def add_extern_exit(self):
        if self.platform == Platform.win32:
            self.__add_extern("__imp__ExitProcess@4")

    def add_extern_scanf(self):
        if self.platform == Platform.win32:
            self.__add_extern("__imp__scanf")
        else:
            self.__add_extern("scanf")

    def add_extern_printf(self):
        if self.platform == Platform.win32:
            self.__add_extern("__imp__printf")
        else:
            self.__add_extern("printf")

    def __add_extern(self, name):
        self.__externs.add("extern %s" % name)

    def add_global_function(self, function):
        self.__global_functions.append(function)

    def add_label(self, label):
        if self.__program_state.function_name == "_%s" % MainFunction.FUNCTION_NAME:
            self.__main_function_instruction.append("%s:" % label)
        else:
            self.__text_section_instruction.append("%s:" % label)

    def add_instruction(self, instr, op1=None, op2=None, op3=None, op4=None):
        if self.__program_state.function_name == "_%s" % MainFunction.FUNCTION_NAME:
            self.__add_instruction(instr, op1, op2, op3, op4, self.__main_function_instruction)
        elif self.__program_state.is_global_statement():
            self.__add_instruction(instr, op1, op2, op3, op4, self.__global_variables_initialization)
        else:
            self.__add_instruction(instr, op1, op2, op3, op4, self.__text_section_instruction)

    @staticmethod
    def __add_instruction(instr, op1, op2, op3, op4, instruction_list):
        op1 = "" if op1 is None else " " + str(op1)
        op2 = "" if op2 is None else ", " + str(op2)
        op3 = "" if op3 is None else ", " + str(op3)
        op4 = "" if op4 is None else ", " + str(op4)
        instruction_list.append("\t%s%s%s%s%s" % (instr, op1, op2, op3, op4))

    def add_data(self, name, value_type, value):
        self.__data_section_instruction.add("\t%s %s %s, 0" % (name, value_type, value))

    def __str__(self):
        for function in self.__global_functions:
            function.code(self, self.__program_state)
        global_main = "_%s" % MainFunction.FUNCTION_NAME if self.__platform == Platform.win32 else MainFunction.FUNCTION_NAME

        if len(self.__main_function_instruction) == 0:
            main_function = MainFunction(None, MainFunction.FUNCTION_NAME, None, [])
            main_function.name_mangling(None, {})
            main_function.code(self, self.__program_state)

        main_function_str = self.__main_function_instruction[0] + "\n" + "\n".join(
            x for x in self.__global_variables_initialization) + "\n" + "\n".join(
            self.__main_function_instruction[i] for i in range(1, len(
                self.__main_function_instruction)))

        externs = "\n".join(x for x in self.__externs)
        text = "section .text\n" + \
               "global %s\n\n" % global_main + \
               main_function_str + "\n" + \
               "\n".join(x for x in self.__text_section_instruction)
        data = "section .data\n" + \
               "\n".join(x for x in self.__data_section_instruction) + \
               "\n\tend"
        return "%s\n\n%s\n\n%s" % (externs, text, data)
