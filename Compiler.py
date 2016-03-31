#!/usr/bin/python

import getopt
import os
import sys
from subprocess import Popen

from antlr4 import CommonTokenStream

from CodeBuilder import CodeBuilder
from GrammarLexer import GrammarLexer, FileStream
from GrammarParser import GrammarParser
from ParserError import ParserError
from Platform import Platform
from ProgramState import ProgramState


def main(argv):
    help_string = "Compiler.py -f <elf32 | win32> -o <output file>"

    platform = Platform.elf32
    input_file = ''
    output_file = ''

    asm_file = ''
    obj_file = ''

    try:
        opts, args = getopt.getopt(argv, "hf:o:")
        for opt, arg in opts:
            if opt == '-h':
                print(help_string)
                sys.exit()
            elif opt in ("-f", "--format"):
                platform = Platform.by_name(arg)
            elif opt in ("-o", "--ofile"):
                output_file = arg
        input_file = args[0]
        asm_file = os.path.splitext(input_file)[0] + ".asm"
        obj_file = os.path.splitext(input_file)[0] + (".obj" if platform == Platform.win32 else ".o")
        if output_file == '':
            output_file = os.path.splitext(input_file)[0] + "." + platform.output_file_extension()
    except getopt.GetoptError:
        print(help_string)
        sys.exit(2)

    try:
        run_compile(platform, input_file, asm_file)
        link_executable_file(platform, asm_file, obj_file, output_file)
    except SyntaxError as e:
        print("Syntax error:", e.msg, file=sys.stderr)
    except ValueError as e:
        print("Value error:", e, file=sys.stderr)


def link_executable_file(platform, asm_file, obj_file, output_file):
    if platform == Platform.win32:
        print("unfortunately couldn't make executable file for %s platform" % platform)
    else:
        yasm_cmd = ["yasm", "-f", platform.name, "-o", obj_file, asm_file]
        p = Popen(yasm_cmd)
        p.wait()
        os.remove(asm_file)
        gcc_cmd = ["gcc", "-o", output_file, obj_file]
        p = Popen(gcc_cmd)
        p.wait()
        os.remove(obj_file)


def run_compile(platform, input_file, asm_file):
    input_stream = FileStream(input_file)

    lexer = GrammarLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = GrammarParser(stream)
    parser.addErrorListener(ParserError())
    parser.program()

    parser.program_states.name_mangling()
    state = ProgramState()
    builder = CodeBuilder(state, platform)
    parser.program_states.code(builder, state)

    output_file = open(asm_file, 'w')
    print(str(builder), file=output_file)
    output_file.close()


if __name__ == "__main__":
    main(sys.argv[1:])
