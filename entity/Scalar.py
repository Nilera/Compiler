from operator import contains

from entity.CodeGenerator import CodeGenerator
from entity.NameMangling import NameMangling
from entity.Returnable import Returnable
from entity.Type import Type


def get_scalar(value):
    if value.isdigit():
        return IntScalar(value)
    elif value == "true" or value == "false":
        return BoolScalar(value)
    else:
        return VariableScalar(value)


class Scalar(NameMangling, CodeGenerator, Returnable):
    def __init__(self, value):
        super(Scalar, self).__init__()
        self._value = value

    @property
    def value(self):
        return self._value

    def name_mangling(self, function_name, mangled_name):
        pass

    def windows_code(self, code_builder, program_state):
        code_builder.add_instruction("mov", "eax", self.value)

    def value_type(self, program_state):
        raise NotImplementedError

    def __str__(self):
        return str(self._value)


class VariableScalar(Scalar):
    def __init__(self, value):
        super(VariableScalar, self).__init__(value)

    def name_mangling(self, function_name, mangled_name):
        if contains(mangled_name, self._value):
            self._value = mangled_name[self._value]

    def windows_code(self, code_builder, program_state):
        code_builder.add_instruction("mov", "eax", "[%s]" % self._value)

    def value_type(self, program_state):
        if not program_state.contains_variable(self._value):
            raise ValueError("no variable \"%s\" in scope" % self.__unmangling())
        return program_state.get_variable(self._value).value_type()

    def __unmangling(self):
        try:
            underscore_index = self._value.rindex("_")
            return self._value[underscore_index + 1:]
        except ValueError:
            return self._value


class IntScalar(Scalar):
    def __init__(self, value):
        if not value.isdigit():
            raise ValueError("%s is not integer value" % value)
        super(IntScalar, self).__init__(value)

    def value_type(self, program_state):
        return Type.int


class BoolScalar(Scalar):
    def __init__(self, value):
        if value != "true" or value != "false":
            raise ValueError("%s is not boolean value" % value)
        super(BoolScalar, self).__init__(value)

    def value_type(self, program_state):
        return Type.boolean

    @property
    def value(self):
        return 0 if self._value == "false" else 1
