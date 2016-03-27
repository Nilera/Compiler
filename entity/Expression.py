from entity.CodeGenerator import CodeGenerator
from entity.NameMangling import NameMangling


def get_expression(sign, left=None, right=None):
    if left is None:
        return UnaryPlus(right) if sign == "+" else UnaryMinus(right)
    else:
        if sign == "+":
            return Plus(left, right)
        if sign == "-":
            return Minus(left, right)
        if sign == "*":
            return Multiply(left, right)
        if sign == "/":
            return Divide(left, right)
        if sign == "%":
            return Modulo(left, right)
        if sign == ">":
            return Greater(left, right)
        if sign == "<":
            return Less(left, right)
        if sign == "==":
            return Equal(left, right)
        if sign == "!=":
            return NotEqual(left, right)
        if sign == ">=":
            return GreaterOrEqual(left, right)
        if sign == "<=":
            return LessOrEqual(left, right)
        if sign == "&&":
            return And(left, right)
        if sign == "||":
            return Or(left, right)


class Operator(NameMangling, CodeGenerator):
    def __init__(self):
        super(Operator, self).__init__()

    def name_mangling(self, function_name, mangled_name):
        raise NotImplementedError

    def windows_code(self):
        raise NotImplementedError


class AssignmentOperator(Operator):
    def __init__(self, name, expression):
        super(AssignmentOperator, self).__init__()
        self.__name = name
        self.__expression = expression

    def name_mangling(self, function_name, mangled_name):
        self.__name.name_mangling(function_name, mangled_name)
        self.__expression.name_mangling(function_name, mangled_name)

    def windows_code(self):
        raise NotImplementedError

    def __str__(self):
        return "%s = %s" % (self.__name, self.__expression)


class UnaryOperator(Operator):
    def __init__(self, value):
        super(UnaryOperator, self).__init__()
        self._value = value

    def name_mangling(self, function_name, mangled_name):
        self._value.name_mangling(function_name, mangled_name)

    def windows_code(self):
        raise NotImplementedError

    def __get_sign(self):
        raise NotImplementedError

    def __str__(self):
        return "%s%s" % (self.__get_sign(), self._value)


class UnaryPlus(UnaryOperator):
    def __init__(self, value):
        super(UnaryPlus, self).__init__(value)

    def windows_code(self):
        raise NotImplementedError

    def __get_sign(self):
        return "+"


class UnaryMinus(UnaryOperator):
    def __init__(self, value):
        super(UnaryMinus, self).__init__(value)

    def windows_code(self):
        raise NotImplementedError

    def __get_sign(self):
        return "-"


class BinaryOperator(Operator):
    def __init__(self, left, right):
        super(BinaryOperator, self).__init__()
        self._left = left
        self._right = right

    def name_mangling(self, function_name, mangled_name):
        self._left.name_mangling(function_name, mangled_name)
        self._right.name_mangling(function_name, mangled_name)

    def windows_code(self):
        raise NotImplementedError

    def _get_sign(self):
        raise NotImplementedError

    def __str__(self):
        return "%s %s %s" % (self._left, self._get_sign(), self._right)


class Plus(BinaryOperator):
    def __init__(self, left, right):
        super(Plus, self).__init__(left, right)

    def windows_code(self):
        raise NotImplementedError

    def _get_sign(self):
        return "+"


class Minus(BinaryOperator):
    def __init__(self, left, right):
        super(Minus, self).__init__(left, right)

    def windows_code(self):
        raise NotImplementedError

    def _get_sign(self):
        return "-"


class Multiply(BinaryOperator):
    def __init__(self, left, right):
        super(Multiply, self).__init__(left, right)

    def windows_code(self):
        raise NotImplementedError

    def _get_sign(self):
        return "*"


class Divide(BinaryOperator):
    def __init__(self, left, right):
        super(Divide, self).__init__(left, right)

    def windows_code(self):
        raise NotImplementedError

    def _get_sign(self):
        return "/"


class Modulo(BinaryOperator):
    def __init__(self, left, right):
        super(Modulo, self).__init__(left, right)

    def windows_code(self):
        raise NotImplementedError

    def _get_sign(self):
        return "%"


class Greater(BinaryOperator):
    def __init__(self, left, right):
        super(Greater, self).__init__(left, right)

    def windows_code(self):
        raise NotImplementedError

    def _get_sign(self):
        return ">"


class Less(BinaryOperator):
    def __init__(self, left, right):
        super(Less, self).__init__(left, right)

    def windows_code(self):
        raise NotImplementedError

    def _get_sign(self):
        return "<"


class Equal(BinaryOperator):
    def __init__(self, left, right):
        super(Equal, self).__init__(left, right)

    def windows_code(self):
        raise NotImplementedError

    def _get_sign(self):
        return "=="


class GreaterOrEqual(BinaryOperator):
    def __init__(self, left, right):
        super(GreaterOrEqual, self).__init__(left, right)

    def windows_code(self):
        raise NotImplementedError

    def _get_sign(self):
        return ">="


class LessOrEqual(BinaryOperator):
    def __init__(self, left, right):
        super(LessOrEqual, self).__init__(left, right)

    def windows_code(self):
        raise NotImplementedError

    def _get_sign(self):
        return "<="


class NotEqual(BinaryOperator):
    def __init__(self, left, right):
        super(NotEqual, self).__init__(left, right)

    def windows_code(self):
        raise NotImplementedError

    def _get_sign(self):
        return "!="


class Or(BinaryOperator):
    def __init__(self, left, right):
        super(Or, self).__init__(left, right)

    def windows_code(self):
        raise NotImplementedError

    def _get_sign(self):
        return "||"


class And(BinaryOperator):
    def __init__(self, left, right):
        super(And, self).__init__(left, right)

    def windows_code(self):
        raise NotImplementedError

    def _get_sign(self):
        return "&&"
