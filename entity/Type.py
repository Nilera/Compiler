from enum import Enum


class Type(Enum):
    int = 0
    boolean = 1
    char = 2

    def format_string(self):
        if self == Type.int or self == Type.boolean:
            return "int_format", "db", "\"%d\""
        elif self == Type.char:
            return "char_format", "db", "\"%c\""

    def sizeof(self):
        if self == Type.int or self == Type.boolean:
            return 4
        elif self == Type.char:
            return 1

    def size_type(self):
        if self == Type.int or self == Type.boolean:
            return "dd"
        elif self == Type.char:
            return "dd"

    def __str__(self):
        return self.name

    @staticmethod
    def by_name(type_name):
        if type_name == Type.int.name:
            return Type.int
        elif type_name == Type.boolean.name:
            return Type.boolean
        elif type_name == Type.char.name:
            return Type.char
        else:
            raise ValueError("language is not supported type %s" % type_name)
