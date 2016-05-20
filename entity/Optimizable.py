class Optimizable(object):
    def constant_folding(self, constants):
        """
        Optimizes code using constant folding and constant propagation.
        :type constants: dict
        :rtype: None
        """
        raise NotImplementedError

    def find_constant(self, constants):
        """
        Finds all constant in code and stores it ``constants`` dictionary.
        :type constants: dict
        :rtype: None
        """
        raise NotImplementedError
