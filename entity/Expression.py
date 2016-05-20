from operator import contains

from entity.Array import ArrayGetter, ArrayCreator, Array
from entity.CodeElement import CodeElement
from entity.Function import ArrayCopyFunction
from entity.NameMangling import NameMangling
from entity.Scalar import VariableScalar, IntScalar, BoolScalar
from entity.Type import Type


def get_expression(sign, left=None, right=None):
    """
    :type sign: str
    :type left: entity.Scalar.Scalar | entity.Expression.Operator
    :type right: entity.Scalar.Scalar | entity.Expression.Operator
    :rtype: entity.Expression.Operator
    """
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


class Operator(CodeElement):
    def __init__(self):
        super(Operator, self).__init__()

    def name_mangling(self, function_name, mangled_name):
        raise NotImplementedError

    def code(self, code_builder, program_state):
        raise NotImplementedError

    def value_type(self, program_state):
        raise NotImplementedError

    def validate(self, program_state):
        raise NotImplementedError

    def unmangling(self):
        raise NotImplementedError

    def constant_folding(self, constants):
        raise NotImplementedError

    def find_constant(self, constants):
        pass


class AssignmentOperator(Operator):
    def __init__(self, target, expression):
        """
        :type target: entity.Scalar.VariableScalar | entity.Array.ArrayGetter
        :type expression: entity.Scalar.Scalar | entity.Expression.Operator
        """
        super(AssignmentOperator, self).__init__()
        self.__target = target
        self.__expression = expression

    def name_mangling(self, function_name, mangled_name):
        self.__target.name_mangling(function_name, mangled_name)
        self.__expression.name_mangling(function_name, mangled_name)

    def code(self, code_builder, program_state):
        var_name = self.__target.value
        var_type = self.__target.value_type(program_state)

        self.__expression.code(code_builder, program_state)
        if isinstance(self.__target, ArrayGetter):
            self.__target.code_setter(code_builder, program_state)
        elif isinstance(self.__target, VariableScalar) and isinstance(var_type, Array):
            code_builder.add_instruction("mov", "ebx", "[%s]" % var_name)
            arr_copy_function = ArrayCopyFunction(None, ArrayCopyFunction.FUNCTION_NAME, [var_type.value_type])
            arr_copy_function.code(code_builder, program_state)
        else:
            code_builder.add_instruction("mov", "[%s]" % var_name, "eax")

    def value_type(self, program_state):
        raise NotImplementedError

    def validate(self, program_state):
        var_name = self.__target.value
        if not program_state.contains_variable(var_name):
            raise SyntaxError("no variable \"%s\" in scope" % self.__target.unmangling())

        var_type = self.__target.value_type(program_state)
        expr_type = self.__expression.value_type(program_state)
        if var_type != expr_type:
            raise ValueError(
                "%s expression has incorrect type <%s> = <%s>" % (self.unmangling(), var_type, expr_type))
        if isinstance(expr_type, ArrayCreator):
            raise SyntaxError("%s array creator couldn't be use here" % self.unmangling())

        self.__expression.validate(program_state)
        self.__target.validate(program_state)

    def unmangling(self):
        return "%s = %s" % (self.__target.unmangling(), self.__expression.unmangling())

    def constant_folding(self, constants):
        expr = self.__expression.constant_folding(constants)
        if expr is not None:
            self.__expression = expr

    def find_constant(self, constants):
        if isinstance(self.__target, VariableScalar):
            if contains(constants, self.__target.value):
                del constants[self.__target.value]

    def __str__(self):
        return "%s = %s" % (self.__target, self.__expression)


class UnaryOperator(Operator):
    def __init__(self, value):
        """
        :type value: entity.Scalar.Scalar | entity.Expression.Operator
        """
        super(UnaryOperator, self).__init__()
        self._value = value

    def name_mangling(self, function_name, mangled_name):
        self._value.name_mangling(function_name, mangled_name)

    def code(self, code_builder, program_state):
        self._value.code(code_builder, program_state)

    def value_type(self, program_state):
        return Type.int

    def validate(self, program_state):
        if self._value.value_type(program_state) != Type.int:
            raise ValueError("incorrect expression %s, unary operator \'%s\' can be applied only for int" % (
                self.unmangling(), self.__get_sign()))
        self._value.validate(program_state)

    def __get_sign(self):
        """
        :rtype: str
        """
        raise NotImplementedError

    def unmangling(self):
        return "%s%s" % (self.__get_sign(), NameMangling.unmangling(self._value))

    def constant_folding(self, constants):
        """
        :type constants: dict
        :rtype: entity.Scalar.IntScalar
        """
        raise NotImplementedError

    def __str__(self):
        return "%s%s" % (self.__get_sign(), self._value)


class UnaryPlus(UnaryOperator):
    def __init__(self, value):
        super(UnaryPlus, self).__init__(value)

    def __get_sign(self):
        return "+"

    def constant_folding(self, constants):
        return self._value.constant_folding(constants)


class UnaryMinus(UnaryOperator):
    def __init__(self, value):
        super(UnaryMinus, self).__init__(value)

    def code(self, code_builder, program_state):
        super().code(code_builder, program_state)
        code_builder.add_instruction("neg", "eax")

    def __get_sign(self):
        return "-"

    def constant_folding(self, constants):
        res = self._value.constant_folding(constants)
        if res is not None:
            return IntScalar(-res.value)


class BinaryOperator(Operator):
    def __init__(self, left, right):
        """
        :type left: entity.Scalar.Scalar | entity.Expression.Operator
        :type right: entity.Scalar.Scalar | entity.Expression.Operator
        """
        super(BinaryOperator, self).__init__()
        self._left = left
        self._right = right

    def name_mangling(self, function_name, mangled_name):
        self._left.name_mangling(function_name, mangled_name)
        self._right.name_mangling(function_name, mangled_name)

    def code(self, code_builder, program_state):
        self._left.code(code_builder, program_state)
        code_builder.add_instruction("push", "eax")
        self._right.code(code_builder, program_state)
        code_builder.add_instruction("mov", "ebx", "eax")
        code_builder.add_instruction("pop", "eax")
        self.code_operator(code_builder, program_state)

    def code_operator(self, code_builder, program_state):
        raise NotImplementedError

    def value_type(self, program_state):
        return Type.int

    def validate(self, program_state):
        left_type = self._left.value_type(program_state)
        right_type = self._right.value_type(program_state)
        if left_type != right_type:
            raise ValueError("%s: operator %s cannot be applied for <%s>, <%s>" % (
                self.unmangling(), self._get_sign(), left_type, right_type))
        self._left.validate(program_state)
        self._right.validate(program_state)

    def _get_sign(self):
        """
        :rtype: str
        """
        raise NotImplementedError

    def unmangling(self):
        return "%s %s %s" % (self._left.unmangling(), self._get_sign(), self._right.unmangling())

    def constant_folding(self, constants):
        """
        :type constants: dict
        :rtype: entity.Scalar.IntScalar | entity.Scalar.CharScalar
        """
        raise NotImplementedError

    def __str__(self):
        return "%s %s %s" % (self._left, self._get_sign(), self._right)


class BooleanBinaryOperator(BinaryOperator):
    def __init__(self, left, right):
        super(BooleanBinaryOperator, self).__init__(left, right)

    def code_operator(self, code_builder, program_state):
        label = "%s_bool_op_%d_skip" % (program_state.function_name, program_state.get_if_number())
        code_builder.add_instruction("cmp", "eax", "ebx")
        code_builder.add_instruction("mov", "eax", "1")
        code_builder.add_instruction(self._get_instruction(), label)
        code_builder.add_instruction("xor", "eax", "eax")
        code_builder.add_label(label)

    def _get_instruction(self):
        raise NotImplementedError

    def value_type(self, program_state):
        return Type.boolean

    def _get_sign(self):
        raise NotImplementedError

    def constant_folding(self, constants):
        """
        :type constants: dict
        :rtype: entity.Scalar.BoolScalar
        """
        raise NotImplementedError


class Plus(BinaryOperator):
    def __init__(self, left, right):
        super(Plus, self).__init__(left, right)

    def code_operator(self, code_builder, program_state):
        code_builder.add_instruction("add", "eax", "ebx")

    def _get_sign(self):
        return "+"

    def constant_folding(self, constants):
        left = self._left.constant_folding(constants)
        right = self._right.constant_folding(constants)
        if left is not None and right is not None:
            return IntScalar(left.value + right.value)


class Minus(BinaryOperator):
    def __init__(self, left, right):
        super(Minus, self).__init__(left, right)

    def code_operator(self, code_builder, program_state):
        code_builder.add_instruction("sub", "eax", "ebx")

    def _get_sign(self):
        return "-"

    def constant_folding(self, constants):
        left = self._left.constant_folding(constants)
        right = self._right.constant_folding(constants)
        if left is not None and right is not None:
            return IntScalar(left.value - right.value)


class Multiply(BinaryOperator):
    def __init__(self, left, right):
        super(Multiply, self).__init__(left, right)

    def code_operator(self, code_builder, program_state):
        code_builder.add_instruction("cdq")
        code_builder.add_instruction("imul", "ebx")

    def _get_sign(self):
        return "*"

    def constant_folding(self, constants):
        left = self._left.constant_folding(constants)
        right = self._right.constant_folding(constants)
        if left is not None and right is not None:
            return IntScalar(left.value * right.value)


class Divide(BinaryOperator):
    def __init__(self, left, right):
        super(Divide, self).__init__(left, right)

    def code_operator(self, code_builder, program_state):
        code_builder.add_instruction("cdq")
        code_builder.add_instruction("idiv", "ebx")

    def _get_sign(self):
        return "/"

    def constant_folding(self, constants):
        left = self._left.constant_folding(constants)
        right = self._right.constant_folding(constants)
        if left is not None and right is not None:
            return IntScalar(left.value / right.value)


class Modulo(BinaryOperator):
    def __init__(self, left, right):
        super(Modulo, self).__init__(left, right)

    def code_operator(self, code_builder, program_state):
        code_builder.add_instruction("cdq")
        code_builder.add_instruction("idiv", "ebx")
        code_builder.add_instruction("mov", "eax", "edx")

    def _get_sign(self):
        return "%"

    def constant_folding(self, constants):
        left = self._left.constant_folding(constants)
        right = self._right.constant_folding(constants)
        if left is not None and right is not None:
            return IntScalar(left.value % right.value)


class Greater(BooleanBinaryOperator):
    def __init__(self, left, right):
        super(Greater, self).__init__(left, right)

    def _get_instruction(self):
        return "jg"

    def _get_sign(self):
        return ">"

    def constant_folding(self, constants):
        left = self._left.constant_folding(constants)
        right = self._right.constant_folding(constants)
        if left is not None and right is not None:
            return BoolScalar(left.value > right.value)


class Less(BooleanBinaryOperator):
    def __init__(self, left, right):
        super(Less, self).__init__(left, right)

    def _get_instruction(self):
        return "jl"

    def _get_sign(self):
        return "<"

    def constant_folding(self, constants):
        left = self._left.constant_folding(constants)
        right = self._right.constant_folding(constants)
        if left is not None and right is not None:
            return BoolScalar(left.value < right.value)


class Equal(BooleanBinaryOperator):
    def __init__(self, left, right):
        super(Equal, self).__init__(left, right)

    def _get_instruction(self):
        return "je"

    def _get_sign(self):
        return "=="

    def constant_folding(self, constants):
        left = self._left.constant_folding(constants)
        right = self._right.constant_folding(constants)
        if left is not None and right is not None:
            return BoolScalar(left.value == right.value)


class GreaterOrEqual(BooleanBinaryOperator):
    def __init__(self, left, right):
        super(GreaterOrEqual, self).__init__(left, right)

    def _get_instruction(self):
        return "jge"

    def _get_sign(self):
        return ">="

    def constant_folding(self, constants):
        left = self._left.constant_folding(constants)
        right = self._right.constant_folding(constants)
        if left is not None and right is not None:
            return BoolScalar(left.value >= right.value)


class LessOrEqual(BooleanBinaryOperator):
    def __init__(self, left, right):
        super(LessOrEqual, self).__init__(left, right)

    def _get_instruction(self):
        return "jle"

    def _get_sign(self):
        return "<="

    def constant_folding(self, constants):
        left = self._left.constant_folding(constants)
        right = self._right.constant_folding(constants)
        if left is not None and right is not None:
            return BoolScalar(left.value <= right.value)


class NotEqual(BooleanBinaryOperator):
    def __init__(self, left, right):
        super(NotEqual, self).__init__(left, right)

    def _get_instruction(self):
        return "jne"

    def _get_sign(self):
        return "!="

    def constant_folding(self, constants):
        left = self._left.constant_folding(constants)
        right = self._right.constant_folding(constants)
        if left is not None and right is not None:
            return BoolScalar(left.value != right.value)


class Or(BooleanBinaryOperator):
    def __init__(self, left, right):
        super(Or, self).__init__(left, right)

    def code_operator(self, code_builder, program_state):
        code_builder.add_instruction("or", "eax", "ebx")

    def _get_instruction(self):
        raise NotImplementedError

    def _get_sign(self):
        return "||"

    def validate(self, program_state):
        super().validate(program_state)
        left_type = self._left.value_type(program_state)
        right_type = self._right.value_type(program_state)
        if left_type != Type.boolean or right_type != Type.boolean:
            raise ValueError("%s: operator %s cannot be applied for <%s>, <%s>" % (
                self.unmangling(), self._get_sign(), left_type, right_type))

    def constant_folding(self, constants):
        left = self._left.constant_folding(constants)
        right = self._right.constant_folding(constants)
        if left is not None and right is not None:
            left_val = False if left.value == 0 else True
            right_val = False if right.value == 0 else True
            return BoolScalar(left_val or right_val)


class And(BooleanBinaryOperator):
    def __init__(self, left, right):
        super(And, self).__init__(left, right)

    def code_operator(self, code_builder, program_state):
        code_builder.add_instruction("and", "eax", "ebx")

    def _get_instruction(self):
        raise NotImplementedError

    def _get_sign(self):
        return "&&"

    def validate(self, program_state):
        super().validate(program_state)
        left_type = self._left.value_type(program_state)
        right_type = self._right.value_type(program_state)
        if left_type != Type.boolean or right_type != Type.boolean:
            raise ValueError("%s: operator %s cannot be applied for <%s>, <%s>" % (
                self.unmangling(), self._get_sign(), left_type, right_type))

    def constant_folding(self, constants):
        left = self._left.constant_folding(constants)
        right = self._right.constant_folding(constants)
        if left is not None and right is not None:
            left_val = False if left.value == 0 else True
            right_val = False if right.value == 0 else True
            return BoolScalar(left_val and right_val)
