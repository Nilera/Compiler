import hashlib
from operator import contains

from entity.Array import Array
from entity.CodeElement import CodeElement
from entity.NameMangling import unmangling
from entity.Type import Type


def get_scalar(value):
    """
    :type value: str
    :rtype: str | int
    """
    if value.isdigit():
        return IntScalar(value)
    elif value == "true" or value == "false":
        return BoolScalar(value)
    elif value.startswith("\'"):
        return CharScalar(value)
    elif value.startswith("\""):
        return StringScalar(value)
    else:
        return VariableScalar(value)


class Scalar(CodeElement):
    def __init__(self, value):
        super(Scalar, self).__init__()
        self._value = value

    @property
    def value(self):
        """
        :rtype: int | str
        """
        return self._value

    def name_mangling(self, function_name, mangled_name):
        pass

    def code(self, code_builder, program_state):
        code_builder.add_instruction("mov", "eax", self.value)

    def value_type(self, program_state):
        raise NotImplementedError

    def validate(self, program_state):
        pass

    def unmangling(self):
        return self._value

    def constant_folding(self, constants):
        return self

    def find_constant(self, constants):
        pass

    def __str__(self):
        return str(self._value)


class VariableScalar(Scalar):
    def __init__(self, value):
        """
        :type value: str
        """
        super(VariableScalar, self).__init__(value)

    def name_mangling(self, function_name, mangled_name):
        if contains(mangled_name, self._value):
            self._value = mangled_name[self._value]

    def code(self, code_builder, program_state):
        code_builder.add_instruction("mov", "eax", "[%s]" % self._value)

    def value_type(self, program_state):
        if not program_state.contains_variable(self._value):
            raise ValueError("no variable \"%s\" in scope" % self.unmangling())
        return program_state.get_variable(self._value).value_type()

    def unmangling(self):
        return unmangling(self._value)

    def constant_folding(self, constants):
        if contains(constants, self._value):
            return constants[self._value]


class IntScalar(Scalar):
    def __init__(self, value):
        super(IntScalar, self).__init__(int(value))

    def value_type(self, program_state=None):
        return Type.int


class BoolScalar(Scalar):
    def __init__(self, value):
        super(BoolScalar, self).__init__(0 if value == "false" else 1)

    def value_type(self, program_state=None):
        return Type.boolean


class CharScalar(Scalar):
    def __init__(self, value):
        super(CharScalar, self).__init__(ord(value[1]))

    def code(self, code_builder, program_state):
        code_builder.add_instruction("xor", "eax", "eax")
        code_builder.add_instruction("mov", "al", self.value)

    def value_type(self, program_state=None):
        return Type.char


class StringScalar(Scalar):
    def __init__(self, value):
        super(StringScalar, self).__init__(value)

    def code(self, code_builder, program_state):
        str_hash = "s_%s" % hashlib.md5(self.value.encode("UTF-8")).hexdigest()
        code_builder.add_data(str_hash, "db", self._value)
        code_builder.add_instruction("mov", "eax", str_hash)
        code_builder.add_instruction("mov", "ecx", len(self.value) + 1)

    def value_type(self, program_state=None):
        return Array(Type.char, 1)

    @property
    def value(self):
        """
        :rtype: str
        """
        return self._value[1:len(self._value) - 1]
