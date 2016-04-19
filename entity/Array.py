import sys

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
