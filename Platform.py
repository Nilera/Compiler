from enum import Enum


class Platform(Enum):
    win32 = 0
    elf32 = 1

    def __str__(self):
        return self.name

    def output_file_extension(self):
        if self == Platform.win32:
            return "exe"
        else:
            return "out"

    @staticmethod
    def by_name(type_name):
        if type_name == Platform.win32.name:
            return Platform.win32
        elif type_name == Platform.elf32.name:
            return Platform.elf32
        else:
            raise AttributeError(
                "platform %s is not supported, user %s or %s instead" % (type_name, Platform.win32, Platform.elf32))
