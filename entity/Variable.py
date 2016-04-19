from Platform import Platform
from entity.CodeGenerator import CodeGenerator
from entity.Expression import Operator, ArrayCreator, ArrayGetter
from entity.NameMangling import NameMangling
from entity.Scalar import IntScalar, BoolScalar, VariableScalar
from entity.Statement import CallFunctionStatement


class Variable(NameMangling, CodeGenerator):
    def __init__(self, value_type, name, expression=None):
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
        prev_name = self.__name
        self.__name = "%s_%s" % (function_name, prev_name)
        if isinstance(self.__expression, NameMangling):
            self.__expression.name_mangling(function_name, mangled_name)
        mangled_name[prev_name] = self.__name

    def code(self, code_builder, program_state):
        program_state.add_variable(self)
        size_type = self.__value_type.size_type()
        default_value = self.__value_type.default_value()
        if self.expression is None:
            code_builder.add_data(self.__name, size_type, default_value)
        else:
            expr_type = self.expression.value_type(program_state)
            if self.__value_type != expr_type:
                raise ValueError(
                    "%s expression has incorrect type <%s> = <%s>" % (self.unmangling(), self.__value_type, expr_type))
            if isinstance(self.expression, ArrayCreator):
                pass
            elif isinstance(self.expression, ArrayGetter):
                pass
            elif isinstance(self.expression, (IntScalar, BoolScalar)):
                code_builder.add_data(self.name, size_type, self.expression.value)
            else:



            if isinstance(self.expression, (IntScalar, BoolScalar)):
                code_builder.add_data(self.name, size_type, self.expression.value)
            elif isinstance(self.expression, ArrayCreator):
                if code_builder.platform == Platform.win32:
                    code_builder.add_extern("__imp__malloc")
                else:
                    code_builder.add_extern("malloc")
                code_builder.add_data(self.name, size_type, "0")
                program_state.set_array_name(self.name)
                self.expression.code(code_builder, program_state)
                program_state.set_array_name("")
                code_builder.add_instruction("mov", "[%s]" % self.name, "eax")
            elif isinstance(self.expression, VariableScalar):
                code_builder.add_data(self.name, size_type, default_value)
                code_builder.add_instruction("mov", "eax", "[%s]" % self.expression.value)
                code_builder.add_instruction("mov", "[%s]" % self.name, "eax")
            elif isinstance(self.expression, ArrayGetter):
                code_builder.add_data(self.name, "dw", "0")
                program_state.set_array_name(self.name)
                self.expression.code_generator(code_builder, program_state)
                program_state.set_array_name("")
                code_builder.add_instruction("mov", "[%s]" % self.name, "eax")
            elif isinstance(self.expression, Operator):
                code_builder.add_data(self.name, size_type, default_value)
                self.expression.code(code_builder, program_state)
                code_builder.add_instruction("mov", "[%s]" % self.name, "eax")
            elif isinstance(self.expression, CallFunctionStatement):
                code_builder.add_data(self.name, size_type, default_value)
                self.expression.code(code_builder, program_state)
                code_builder.add_instruction("mov", "[%s]" % self.name, "eax")

    def value_type(self, program_state=None):
        return self.__value_type

    def unmangling(self):
        return "%s %s = %s" % (
            str(self.__value_type), NameMangling.unmangling(self.__name), self.__expression.unmangling())

    def __str__(self):
        assign = "" if self.__expression is None else " = %s" % str(self.__expression)
        return "%s %s" % (str(self.__value_type), self.__name) + assign
