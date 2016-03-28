from entity.Function import MainFunction


class CodeBuilder(object):
    def __init__(self, program_state):
        super(CodeBuilder, self).__init__()
        self.__externs = set()
        self.__global_variables_initialization = []
        self.__global_functions = []
        self.__text_section_instruction = []
        self.__data_section_instruction = set()
        self.__program_state = program_state

    def add_extern(self, name):
        self.__externs.add("extern %s" % name)

    def add_global_variable_instruction(self, instr, op1=None, op2=None, op3=None, op4=None):
        self.__add_instruction(instr, op1, op2, op3, op4, self.__text_section_instruction)

    def add_global_function(self, function):
        self.__global_functions.append(function)

    def add_label(self, label):
        self.__text_section_instruction.append("%s:" % label)

    def add_instruction(self, instr, op1=None, op2=None, op3=None, op4=None):
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
            function.windows_code(self, self.__program_state)

        externs = "\n".join(x for x in self.__externs)
        text = "section .text\n" + \
               "global _main\n\n" + \
               MainFunction.GLOBAL_VARIABLES_FUNCTION + ":\n" + \
               "\n".join(x for x in self.__global_variables_initialization) + \
               "\tret\n" + \
               "\n".join(x for x in self.__text_section_instruction)
        data = "section .data\n" + \
               "\n".join(x for x in self.__data_section_instruction) + \
               "\n\tend"
        return "%s\n%s\n\n%s" % (externs, text, data)
