from operator import contains

from entity.CodeGenerator import CodeGenerator
from entity.NameMangling import NameMangling


def get_scalar(value):
    if value.isdigit():
        return IntScalar(value)
    elif value == "true" or value == "false":
        return BoolScalar(value)
    else:
        return VariableScalar(value)


class Scalar(NameMangling, CodeGenerator):
    def __init__(self, value):
        super(Scalar, self).__init__()
        self._value = value

    @property
    def value(self):
        return self._value

    def name_mangling(self, function_name, mangled_name):
        pass

    def windows_code(self):
        raise NotImplementedError

    def __str__(self):
        return str(self._value)


class VariableScalar(Scalar):
    def __init__(self, value):
        super(VariableScalar, self).__init__(value)

    def name_mangling(self, function_name, mangled_name):
        if contains(mangled_name, self._value):
            self._value = mangled_name[self._value]

    def windows_code(self):
        raise NotImplementedError


class IntScalar(Scalar):
    def __init__(self, value):
        if not value.isdigit():
            raise ValueError("%s is not integer value" % value)
        super(IntScalar, self).__init__(value)

    def windows_code(self):
        raise NotImplementedError


class BoolScalar(Scalar):
    def __init__(self, value):
        if value != "true" or value != "false":
            raise ValueError("%s is not boolean value" % value)
        super(BoolScalar, self).__init__(value)

    def windows_code(self):
        raise NotImplementedError
        # self.__value = 1 if self.__value == "true" else 0
