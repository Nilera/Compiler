from entity.CodeGenerator import CodeGenerator
from entity.NameMangling import NameMangling
from entity.Optimizable import Optimizable


class CodeElement(NameMangling, CodeGenerator, Optimizable):
    def name_mangling(self, function_name, mangled_name):
        raise NotImplementedError

    def unmangling(self):
        raise NotImplementedError

    def code(self, code_builder, program_state):
        raise NotImplementedError

    def value_type(self, program_state):
        raise NotImplementedError

    def constant_folding(self, cf_state):
        """
        Optimizes code using constant folding and constant propagation.
        :type cf_state: util.ConstantFoldingState.ConstantFoldingState
        """
        raise NotImplementedError
