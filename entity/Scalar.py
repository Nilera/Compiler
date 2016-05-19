import hashlib
from operator import contains

from entity.Array import Array
from entity.CodeGenerator import CodeGenerator
from entity.NameMangling import NameMangling, unmangling
from entity.Returnable import Returnable
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


class Scalar(NameMangling, CodeGenerator, Returnable):
    def __init__(self, value):
        """
        :type value: str
        """
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

    def unmangling(self):
        return self._value

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


class IntScalar(Scalar):
    def __init__(self, value):
        if not value.isdigit():
            raise ValueError("%s is not integer value" % value)
        super(IntScalar, self).__init__(value)

    def value_type(self, program_state):
        return Type.int


class BoolScalar(Scalar):
    def __init__(self, value):
        if value != "true" and value != "false":
            raise ValueError("%s is not boolean value" % value)
        super(BoolScalar, self).__init__(value)

    def value_type(self, program_state):
        return Type.boolean

    @property
    def value(self):
        """
        :rtype: int
        """
        return 0 if self._value == "false" else 1


class CharScalar(Scalar):
    def __init__(self, value):
        if not value.startswith("\'"):
            raise ValueError("%s is not char value" % value)
        super(CharScalar, self).__init__(value)

    def code(self, code_builder, program_state):
        code_builder.add_instruction("xor", "eax", "eax")
        code_builder.add_instruction("mov", "al", self.value)

    def value_type(self, program_state):
        return Type.char

    @property
    def value(self):
        """
        :rtype: int
        """
        return ord(self._value[1])


class StringScalar(Scalar):
    def __init__(self, value):
        if not value.startswith("\""):
            raise ValueError("%s is not string value" % value)
        super(StringScalar, self).__init__(value)

    def code(self, code_builder, program_state):
        str_hash = "s_%s" % hashlib.md5(self.value.encode("UTF-8")).hexdigest()
        code_builder.add_data(str_hash, "db", self._value)
        code_builder.add_instruction("mov", "eax", str_hash)
        code_builder.add_instruction("mov", "ecx", len(self.value) + 1)

    def value_type(self, program_state):
        return Array(Type.char, 1)

    @property
    def value(self):
        """
        :rtype: str
        """
        return self._value[1:len(self._value) - 1]
