from Platform import Platform
from entity.CodeElement import CodeElement
from entity.Function import ArrayCopyFunction
from entity.NameMangling import NameMangling, unmangling
from entity.Type import Type


class Array(object):
    def __init__(self, value_type, dimension):
        """
        :type value_type: entity.Type.Type
        :type dimension: int
        """
        self.__value_type = value_type
        self.__dimension = dimension

    def format_string(self):
        """
        :rtype: str
        """
        if self.__value_type == Type.char and self.__dimension == 1:
            return "string_format", "db", "\"%s\""
        else:
            raise SyntaxError("couldn't write %s" % self)

    def sizeof(self):
        """
        :rtype: int
        """
        return self.__value_type.sizeof()

    def size_type(self):
        """
        :rtype: str
        """
        return "dd"

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


class ArrayCreator(CodeElement):
    def __init__(self, value_type, dimensions_sizes):
        """
        :type value_type: entity.Type.Type
        :type dimensions_sizes: list
        """
        self.__value_type = value_type
        self.__dimensions_sizes = dimensions_sizes

    def __getitem__(self, index):
        """
        :type index: int
        :rtype: entity.Scalar.VariableScalar | entity.Scalar.IntScalar | entity.Expression.Operator
        """
        return self.__dimensions_sizes[index]

    def __len__(self):
        return len(self.__dimensions_sizes)

    def name_mangling(self, function_name, mangled_name):
        for dimension_size in self.__dimensions_sizes:
            if isinstance(dimension_size, NameMangling):
                dimension_size.name_mangling(function_name, mangled_name)

    def code(self, code_builder, program_state):
        """
        :return: eax - pointer to start of array, ecx - length of array
        """
        code_builder.add_extern_malloc()
        code_builder.add_instruction("push", "1")
        for index in range(len(self)):
            dimension = self[index]
            dimension.code(code_builder, program_state)
            code_builder.add_data("%s_%d" % (program_state.array_name, index), "dd", "0")
            code_builder.add_instruction("mov", "[%s_%d]" % (program_state.array_name, index), "eax")
            code_builder.add_instruction("mov", "ebx", "eax")
            code_builder.add_instruction("pop", "eax")
            code_builder.add_instruction("cdq")
            code_builder.add_instruction("imul", "ebx")
            code_builder.add_instruction("push", "eax")
        code_builder.add_instruction("mov", "ebx", "eax")
        if code_builder.platform == Platform.win32:
            code_builder.add_instruction("call", "[__imp__malloc]")
        else:
            code_builder.add_instruction("call", "malloc")
        code_builder.add_instruction("mov", "ecx", "ebx")
        code_builder.add_instruction("add", "esp", "4")

    def value_type(self, program_state):
        return Array(self.__value_type, len(self.__dimensions_sizes))

    def validate(self, program_state):
        for index in range(len(self)):
            dimension = self[index]
            dimension.validate(program_state)

    def unmangling(self):
        return "new %s%s" % (self.__value_type, "[" + "][".join(str(x) for x in self.__dimensions_sizes) + "]")

    def constant_folding(self, cf_state):
        pass

    def __str__(self):
        return self.unmangling()


class ArrayGetter(CodeElement):
    def __init__(self, name, dimensions_sizes):
        """
        :type name: entity.Scalar.VariableScalar
        :type dimensions_sizes: list
        """
        super(ArrayGetter, self).__init__()
        self.__name = name
        self.__dimensions_sizes = dimensions_sizes

    def __getitem__(self, index):
        """
        :type index: int
        :type: int
        """
        return self.__dimensions_sizes[index]

    def __len__(self):
        return len(self.__dimensions_sizes)

    @property
    def value(self):
        return self.__name.value

    def name_mangling(self, function_name, mangled_name):
        self.__name.name_mangling(function_name, mangled_name)
        for dimension_size in self.__dimensions_sizes:
            if isinstance(dimension_size, NameMangling):
                dimension_size.name_mangling(function_name, mangled_name)

    def code(self, code_builder, program_state):
        self.code_getter(code_builder, program_state)

    def code_getter(self, code_builder, program_state):
        return_type = program_state.get_variable(self.value).value_type(program_state)
        self.__code_offset(code_builder, program_state, return_type)
        code_builder.add_instruction("mov", "eax", "[%s]" % self.__name)
        code_builder.add_instruction("add", "eax", "ebx")
        if not isinstance(self.value_type(program_state), Array):
            if self.value_type(program_state) == Type.char:
                code_builder.add_instruction("mov", "ebx", "eax")
                code_builder.add_instruction("xor", "eax", "eax")
                code_builder.add_instruction("mov", "al", "[ebx]")
            else:
                code_builder.add_instruction("mov", "eax", "[eax]")
        self.__code_length(code_builder, program_state, return_type)

    def code_setter(self, code_builder, program_state):
        """
        Sets value from eax to array. If settable value is array then it will be copy to new memory.
        """
        set_value_type = program_state.get_variable(self.value).value_type(program_state)
        self.__code_offset(code_builder, program_state, set_value_type)
        code_builder.add_instruction("add", "ebx", "[%s]" % self.__name)
        if isinstance(self.value_type(program_state), Array):
            arr_copy_function = ArrayCopyFunction(None, ArrayCopyFunction.FUNCTION_NAME, [set_value_type.value_type])
            arr_copy_function.code(code_builder, program_state)
        else:
            if set_value_type.value_type == Type.char:
                code_builder.add_instruction("mov", "[ebx]", "al")
            else:
                code_builder.add_instruction("mov", "[ebx]", "eax")

    def __code_length(self, code_builder, program_state, array):
        """
        Calculates length of array.

        :type array: Array
        :return: ecx length of array
        """
        code_builder.add_instruction("push", "eax")
        code_builder.add_instruction("mov", "eax", "1")
        for i in range(len(self), array.dimension):
            code_builder.add_instruction("mov", "ebx", "[%s_%d]" % (self.__name, i))
            code_builder.add_instruction("cdq")
            code_builder.add_instruction("imul", "ebx")
        code_builder.add_instruction("mov", "ecx", "eax")
        code_builder.add_instruction("pop", "eax")

    def __code_offset(self, code_builder, program_state, array):
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

    def validate(self, program_state):
        for i in range(len(self)):
            self[i].validate(program_state)

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
        return "%s%s" % (unmangling(self.value), "[" + "][".join(str(x) for x in self.__dimensions_sizes) + "]")

    def constant_folding(self, cf_state):
        pass

    def __str__(self):
        return "%s%s" % (self.value, "[" + "][".join(str(x) for x in self.__dimensions_sizes) + "]")
