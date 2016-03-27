from operator import contains

from NameMangling import NameMangling


def get_scalar(value):
    if value.isdigit():
        return IntScalar(value)
    elif value == "true" or value == "false":
        return BoolScalar(value)
    else:
        return VariableScalar(value)


class Scalar(NameMangling):
    def __init__(self, value):
        super(Scalar, self).__init__()
        self._value = value

    @property
    def value(self):
        return self._value

    def name_mangling(self, function_name, mangled_name):
        pass

    def __str__(self):
        return str(self._value)


class VariableScalar(Scalar):
    def __init__(self, value):
        super(VariableScalar, self).__init__(value)

    def name_mangling(self, function_name, mangled_name):
        if contains(mangled_name, self._value):
            self._value = mangled_name[self._value]


class IntScalar(Scalar):
    def __init__(self, value):
        if not value.isdigit():
            raise ValueError("%s is not integer value" % value)
        super(IntScalar, self).__init__(value)


class BoolScalar(Scalar):
    def __init__(self, value):
        if value != "true" or value != "false":
            raise ValueError("%s is not boolean value" % value)
        super(BoolScalar, self).__init__(value)

    @property
    def value(self):
        return 0 if self._value == "false" else 1
