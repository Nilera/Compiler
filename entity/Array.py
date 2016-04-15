class Array(object):
    def __init__(self, value_type, dimension):
        self.__value_type = value_type
        self.__dimension = dimension

    @property
    def value_type(self):
        return self.__value_type

    @property
    def dimension(self):
        return self.__dimension

    def __eq__(self, other):
        return isinstance(other,
                          Array) and self.__value_type == other.value_type and self.__dimension == other.dimension

    def __str__(self):
        return "%s%s" % (self.__value_type, "[]" * self.__dimension)
