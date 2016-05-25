class Optimizable(object):
    def constant_folding(self, cf_state):
        """
        Optimizes code using constant folding and constant propagation.
        :type cf_state: util.ConstantFoldingState.ConstantFoldingState
        """
        raise NotImplementedError
