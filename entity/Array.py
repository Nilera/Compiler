from operator import contains

from Platform import Platform
from entity.CodeGenerator import CodeGenerator
from entity.NameMangling import NameMangling
from entity.Type import Type


class Array(object):
    def __init__(self, value_type, dimension):
        self.__value_type = value_type
        self.__dimension = dimension

    def default_value(self):
        return 0

    def format_string(self):
        if self.__value_type == Type.char and self.__dimension == 1:
            return "string_format", "db", "\"%s\""

    def sizeof(self):
        return self.__value_type.sizeof()

    def size_type(self):
        return self.__value_type.size_type()

    def __str__(self):
        return "%s%s" % (self.__value_type, "[]" * self.__dimension)

    @property
    def value_type(self):
        return self.__value_type

    @property
    def dimension(self):
        return self.__dimension

    def __eq__(self, other):
        return isinstance(other,
                          Array) and self.__value_type == other.value_type and self.__dimension == other.dimension


class ArrayCreator(NameMangling, CodeGenerator):
    def __init__(self, value_type, dimensions_sizes):
        self.__value_type = value_type
        self.__dimensions_sizes = dimensions_sizes

    def __getitem__(self, index):
        return self.__dimensions_sizes[index]

    def __len__(self):
        return len(self.__dimensions_sizes)

    def name_mangling(self, function_name, mangled_name):
        pass

    def code(self, code_builder, program_state):
        if code_builder.platform == Platform.win32:
            code_builder.add_extern("__imp__malloc")
        else:
            code_builder.add_extern("malloc")
        code_builder.add_instruction("push", "1")
        for index in range(len(self)):
            dimension = self[index]
            dimension.code(code_builder, program_state)
            code_builder.add_data("%s_%d" % (program_state.array_name, index), "dd", "0")
            code_builder.add_instruction("mov", "ebx", "eax")
            code_builder.add_instruction("pop", "eax")
            code_builder.add_instruction("cdq")
            code_builder.add_instruction("imul", "ebx")
            code_builder.add_instruction("push", "eax")
            code_builder.add_instruction("mov", "[%s_%d]" % (program_state.array_name, index), "eax")
        if code_builder.platform == Platform.win32:
            code_builder.add_instruction("call", "[__imp__malloc]")
        else:
            code_builder.add_instruction("call", "malloc")
        # code_builder.add_instruction("test", "eax", "eax")
        # code_builder.add_instruction("jz", "_fail_malloc")
        # TODO: add malloc fail
        code_builder.add_instruction("add", "esp", "4")

    def value_type(self, program_state):
        return Array(self.__value_type, len(self.__dimensions_sizes))

    def unmangling(self):
        return "new %s%s" % (self.__value_type, "[" + "][".join(str(x) for x in self.__dimensions_sizes) + "]")

    def __str__(self):
        return self.unmangling()


class ArrayGetter(NameMangling, CodeGenerator):
    def __init__(self, name, dimensions_sizes):
        super(ArrayGetter, self).__init__()
        self.__name = name
        self.__dimensions_sizes = dimensions_sizes

    def __getitem__(self, index):
        return self.__dimensions_sizes[index]

    def __len__(self):
        return len(self.__dimensions_sizes)

    @property
    def value(self):
        return self.__name.value

    def name_mangling(self, function_name, mangled_name):
        self.__name.name_mangling(function_name, mangled_name)

    def code(self, code_builder, program_state):
        self.__code_get(code_builder, program_state, program_state.get_variable(self.value).value_type(program_state))
        code_builder.add_instruction("mov", "eax", "[%s]" % self.__name)
        code_builder.add_instruction("add", "eax", "ebx")
        if not isinstance(self.value_type(program_state), Array):
            code_builder.add_instruction("mov", "eax", "[eax]")

    def code_setter(self, code_builder, program_state):
        """
        Sets value from eax to array. If settable value is array then it will be copy to new memory.
        """
        self.__code_get(code_builder, program_state, program_state.get_variable(self.value).value_type(program_state))
        code_builder.add_instruction("add", "ebx", "[%s]" % self.__name)
        if isinstance(self.value_type(program_state), Array):
            raise NotImplementedError
        else:
            code_builder.add_instruction("mov", "[ebx]", "eax")

    def __code_get(self, code_builder, program_state, array):
        """
        Calculates index offset to get data from array.

        :type array: Array
        :return: ebx offset
        """
        type_size = array.sizeof()
        code_builder.add_instruction("push", "eax")
        code_builder.add_instruction("push", "0")
        for i in range(len(self)):
            self[i].code(code_builder, program_state)
            for j in range(i + 1, array.dimension):
                code_builder.add_instruction("mov", "ebx", "[%s_%d]" % (self.__name, j))
                code_builder.add_instruction("cdq")
                code_builder.add_instruction("imul", "ebx")
            code_builder.add_instruction("pop", "ebx")
            code_builder.add_instruction("add", "eax", "ebx")
            code_builder.add_instruction("push", "eax")
        code_builder.add_instruction("pop", "eax")
        code_builder.add_instruction("mov", "ebx", str(type_size))
        code_builder.add_instruction("cdq")
        code_builder.add_instruction("imul", "ebx")
        code_builder.add_instruction("mov", "ebx", "eax")
        code_builder.add_instruction("pop", "eax")

    def value_type(self, program_state):
        arr_var = program_state.get_variable(self.value)
        arr_var_type = arr_var.value_type()
        if arr_var_type.dimension < len(self.__dimensions_sizes):
            raise SyntaxError("Array required but %s found: %s" % (str(arr_var_type), self.unmangling()))
        elif arr_var_type.dimension == len(self.__dimensions_sizes):
            return arr_var_type.value_type
        else:
            return Array(arr_var_type.value_type, arr_var_type.dimension - len(self))

    def unmangling(self):
        return "%s%s" % (
            NameMangling.unmangling(self.value), "[" + "][".join(str(x) for x in self.__dimensions_sizes) + "]")

    def __str__(self):
        return "%s%s" % (self.value, "[" + "][".join(str(x) for x in self.__dimensions_sizes) + "]")
