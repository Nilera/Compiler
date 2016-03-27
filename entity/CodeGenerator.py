class CodeGenerator(object):
    def windows_code(self):
        raise NotImplementedError

    def linux_code(self):
        return self.windows_code()
