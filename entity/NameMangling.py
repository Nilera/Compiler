def unmangling(mangled_name):
    """
    :type mangled_name: str
    :rtype: str
    """
    try:
        underscore_index = mangled_name.rindex("_")
        return mangled_name[underscore_index + 1:]
    except ValueError:
        return mangled_name


class NameMangling(object):
    def name_mangling(self, function_name, mangled_name):
        """
        :type function_name: str
        :type mangled_name: dict
        :rtype: None
        """
        raise NotImplementedError

    def unmangling(self):
        """
        :rtype: str
        """
        raise NotImplementedError
