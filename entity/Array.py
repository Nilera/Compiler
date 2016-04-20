import sys

from entity.CodeGenerator import CodeGenerator
from entity.NameMangling import NameMangling
from entity.Type import Type


class Array(object):
    def __init__(self, value_type, dimension):
        self.__value_type = value_type
        self.__dimension = dimension

    def default_value(self):
        raise NotImplementedError

    def format_string(self):
        if self.__value_type == Type.char and self.__dimension == 1:
            return "string_format", "db", "\"%s\""

    def __sizeof__(self):
        return sys.getsizeof(self.__value_type)

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
        code_builder.add_instruction("test", "eax", "eax")
        code_builder.add_instruction("jz", "_fail_malloc")
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
        if contains(mangled_name, self.__name):
            self.__name = mangled_name[self.__name]

    def code(self, code_builder, program_state):
        return_type = self.value_type(program_state)
        self.__code_get(code_builder, return_type)
        code_builder.add_instruction("mov", "eax", "[%s]" % self.__name)
        code_builder.add_instruction("add", "eax", "ebx")
        if not isinstance(return_type, Array):
            code_builder.add_instruction("mov", "eax", "[eax]")

    def code_setter(self, code_builder, program_state):
        array = self.value_type(program_state)
        self.__code_get(code_builder, array)
        # value in eax
        code_builder.add_instruction("add", "ebx", "[%s]" % self.__name)
        if isinstance(array, Array):
            # TODO: adok
            raise NotImplementedError
        else:
            code_builder.add_instruction("mov", "[ebx]", "eax")

    def __code_get(self, code_builder, array):
        array_length = 1 if isinstance(array, Type) else len(array)
        code_builder.add_instruction("push", "eax")
        code_builder.add_instruction("push", "0")
        for i in range(len(self)):
            code_builder.add_instruction("mov", "eax", str(self[i]))
            for j in range(i + 1, array_length):
                code_builder.add_instruction("mov", "ebx", "[%s_%d]" % (self.__name, j))
                code_builder.add_instruction("cdq")
                code_builder.add_instruction("imul", "ebx")
            # TODO: mov sizeof
            code_builder.add_instruction("mov", "ebx", "4")
            code_builder.add_instruction("cdq")
            code_builder.add_instruction("imul", "ebx")
            code_builder.add_instruction("pop", "ebx")
            code_builder.add_instruction("add", "eax", "ebx")
            code_builder.add_instruction("push", "eax")
        code_builder.add_instruction("pop", "ebx")
        code_builder.add_instruction("pop", "eax")

    def value_type(self, program_state):
        arr_var = program_state.get_variable(self.value)
        arr_var_type = arr_var.value_type()
        if arr_var_type.dimension > len(self.__dimensions_sizes):
            raise SyntaxError("Array required but %s found: %s" % (str(arr_var_type), self.unmangling()))
        elif arr_var_type.dimension == len(self.__dimensions_sizes):
            return arr_var_type.value_type
        else:
            return Array(arr_var_type, len(self.__dimensions_sizes) - arr_var.dimension)

    def unmangling(self):
        return "%s%s" % (
            NameMangling.unmangling(self.value), "[" + "][".join(str(x) for x in self.__dimensions_sizes) + "]")

    def __str__(self):
        return "%s%s" % (self.value, "[" + "][".join(str(x) for x in self.__dimensions_sizes) + "]")
