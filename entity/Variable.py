from operator import contains

from entity.Array import Array
from entity.CodeElement import CodeElement
from entity.Expression import Operator
from entity.NameMangling import NameMangling, unmangling
from entity.Scalar import VariableScalar, Scalar


class Variable(CodeElement):
    def __init__(self, value_type, name, expression=None):
        """
        :type value_type: entity.Type.Type | entity.Array.Array
        :type name: str
        :type expression: entity.Scalar.Scalar | entity.Expression.Operator | entity.Array.ArrayCreator | entity.Array.ArrayGetter
        """
        self.__value_type = value_type
        self.__name = name
        self.__expression = expression

    @property
    def name(self):
        return self.__name

    @property
    def expression(self):
        return self.__expression

    def name_mangling(self, function_name, mangled_name):
        if isinstance(self.__expression, NameMangling):
            self.__expression.name_mangling(function_name, mangled_name)
        if function_name is not None:
            prev_name = self.__name
            self.__name = "%s_%s" % (function_name, prev_name)
            mangled_name[prev_name] = self.__name

    def code(self, code_builder, program_state):
        """
        :type code_builder: CodeBuilder.CodeBuilder
        :type program_state: ProgramState.ProgramState
        :rtype: None
        """
        program_state.add_variable(self)
        size_type = self.__value_type.size_type()
        if self.expression is None:
            code_builder.add_data(self.name, size_type, "0")
        else:
            if isinstance(self.__value_type, Array):
                code_builder.add_data(self.name, "dd", "0")
                prev_array_name = program_state.array_name
                program_state.set_array_name(self.name)
                self.expression.code(code_builder, program_state)
                program_state.set_array_name(prev_array_name)
                code_builder.add_instruction("mov", "[%s]" % self.name, "eax")
            else:
                # VariableScalar, Operator, CallFunctionStatement, ArrayGetter
                code_builder.add_data(self.name, size_type, "0")
                self.expression.code(code_builder, program_state)
                code_builder.add_instruction("mov", "[%s]" % self.name, "eax")

    def value_type(self, program_state=None):
        return self.__value_type

    def validate(self, program_state):
        program_state.add_variable(self)
        if self.expression is not None:
            expr_type = self.__expression.value_type(program_state)
            if self.__value_type != expr_type:
                raise ValueError(
                    "%s expression has incorrect type <%s> = <%s>" % (self.unmangling(), self.__value_type, expr_type))
            self.expression.validate(program_state)

    def unmangling(self):
        return "%s %s = %s" % (str(self.__value_type), unmangling(self.__name), self.__expression.unmangling())

    def constant_folding(self, constants):
        if isinstance(self.__expression, VariableScalar):
            if contains(constants, self.__expression.value):
                self.__expression = constants[self.__expression.value]
        elif isinstance(self.__expression, Operator):
            res = self.__expression.constant_folding(constants)
            if res is not None:
                self.__expression = res
        elif not isinstance(self.__expression, Scalar):
            return None
        if contains(constants, self.__name):
            constants[self.__name] = self.__expression

    def find_constant(self, constants):
        if isinstance(self.__expression, (Scalar, Operator)):
            constants[self.__name] = self.__expression

    def __str__(self):
        assign = "" if self.__expression is None else " = %s" % str(self.__expression)
        return "%s %s" % (str(self.__value_type), self.__name) + assign
