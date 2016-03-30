class NameMangling(object):
    def name_mangling(self, function_name, mangled_name):
        raise NotImplementedError

    def unmangling(self):
        raise NotImplementedError

    @staticmethod
    def unmangling(mangled_name):
        try:
            underscore_index = mangled_name.rindex("_")
            return mangled_name[underscore_index + 1:]
        except ValueError:
            return mangled_name
