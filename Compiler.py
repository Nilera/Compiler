#!/usr/bin/python

import getopt
import os
import sys
from subprocess import Popen

from antlr4 import CommonTokenStream

from Platform import Platform
from grammar.GrammarLexer import GrammarLexer, FileStream
from grammar.GrammarParser import GrammarParser
from grammar.ParserError import ParserError
from util.CodeBuilder import CodeBuilder
from util.ConstantFoldingState import ConstantFoldingState
from util.ProgramState import ProgramState


def main(argv):
    help_string = "Compiler.py -f <win32 | elf32 | elf64> -O <0 | 1 | 2> -o <output file> input_file"

    platform = Platform.elf32
    input_file = ''
    output_file = ''
    optimization = 0

    asm_file = ''
    obj_file = ''

    try:
        opts, args = getopt.getopt(argv, "hf:o:O:")
        for opt, arg in opts:
            if opt == '-h':
                print(help_string)
                sys.exit()
            elif opt == "-f":
                platform = Platform.by_name(arg)
            elif opt == "-o":
                output_file = arg
            elif opt == "-O":
                optimization = int(arg)

        input_file = args[0]
        asm_file = os.path.splitext(input_file)[0] + ".asm"
        obj_file = os.path.splitext(input_file)[0] + (".obj" if platform == Platform.win32 else ".o")
        if output_file == '':
            output_file = os.path.splitext(input_file)[0] + "." + platform.output_file_extension()
    except getopt.GetoptError:
        print(help_string)
        sys.exit(2)

    try:
        run_compile(platform, input_file, asm_file, optimization)
        link_executable_file(platform, asm_file, obj_file, output_file)
    except SyntaxError as e:
        print("Syntax error:", e.msg, file=sys.stderr)
    except ValueError as e:
        print("Value error:", e, file=sys.stderr)
    except NameError as e:
        print("Name error:", e, file=sys.stderr)


def link_executable_file(platform, asm_file, obj_file, output_file):
    if platform == Platform.win32:
        print("unfortunately couldn't make executable file for %s platform" % platform)
    else:
        yasm_cmd = ["yasm", "-f", Platform.elf32.name, "-o", obj_file, asm_file]
        p = Popen(yasm_cmd)
        p.wait()
        os.remove(asm_file)
        if platform == Platform.elf32:
            gcc_cmd = ["gcc", "-O0", "-o", output_file, obj_file]
        else:
            gcc_cmd = ["gcc", "-m32", "-O0", "-o", output_file, obj_file]
        p = Popen(gcc_cmd)
        p.wait()
        os.remove(obj_file)


def run_compile(platform, input_file, asm_file, optimization):
    input_stream = FileStream(input_file)

    lexer = GrammarLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = GrammarParser(stream)
    parser.addErrorListener(ParserError())
    parser.program()

    parser.program_states.name_mangling()
    parser.program_states.validate(ProgramState())

    state = ProgramState()
    builder = CodeBuilder(state, platform)
    if optimization != 0:
        if optimization >= 1:
            parser.program_states.program_constant_folding(ConstantFoldingState(), builder)
        if optimization >= 2:
            pass
    parser.program_states.code(builder, state)

    output_file = open(asm_file, 'w')
    print(str(builder), file=output_file)
    output_file.close()


if __name__ == "__main__":
    main(sys.argv[1:])
