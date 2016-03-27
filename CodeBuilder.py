class CodeBuilder(object):
    def __init__(self):
        super(CodeBuilder, self).__init__()
        self.__externs = []
        self.__text_section_instruction = []
        self.__data_section_instruction = []

    def add_extern(self, name):
        self.__externs.append(name)

    def add_label(self, label):
        self.__text_section_instruction.append("%s:" % label)

    def add_instruction(self, instr, op1=None, op2=None, op3=None, op4=None):
        op1 = "" if op1 is None else " " + str(op1)
        op2 = "" if op2 is None else ", " + str(op2)
        op3 = "" if op3 is None else ", " + str(op3)
        op4 = "" if op4 is None else ", " + str(op4)
        self.__text_section_instruction.append("\t%s%s%s%s%s" % (instr, op1, op2, op3, op4))

    def add_data(self, name, value_type, value):
        self.__data_section_instruction.append("\t%s %s %s, 0" % (name, value_type, value))

    def __str__(self):
        externs = "\nextern ".join(x for x in self.__externs)
        text = "section .text\n" + \
               "global _main\n\n" + \
               "\n".join(x for x in self.__text_section_instruction)
        data = "section .data\n" + \
               "\n".join(x for x in self.__data_section_instruction) + \
               "\n\tend"
        return "%s\n%s\n%s" % (externs, text, data)
