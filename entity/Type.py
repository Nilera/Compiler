from enum import Enum


class Type(Enum):
    int = 0
    boolean = 1

    def is_correct_value(self, value):
        if self == Type.int:
            return isinstance(value, int)
        else:
            return isinstance(value, bool)

    def __str__(self):
        return self.name

    @staticmethod
    def by_name(type_name):
        if type_name == Type.int.name:
            return Type.int
        elif type_name == Type.boolean.name:
            return Type.boolean
        else:
            raise ValueError("Language is not supported type %s" % type_name)
