import itertools
import os
import time
import unittest
from subprocess import Popen, PIPE


def performance_test_run(output_filename, cmd, read_line=None, iter_number=1000):
    p = Popen(cmd)
    p.wait()

    total_time = 0
    for _ in itertools.repeat(None, iter_number):
        start_time = time.time()
        p = Popen(["./%s" % output_filename], stdin=PIPE, stdout=PIPE)
        if read_line is not None:
            p.stdin.write(bytes(read_line, "UTF-8"))
        p.stdin.close()
        p.stdout.close()
        p.wait()
        end_time = time.time()
        total_time += end_time - start_time

    os.remove(output_filename)
    return total_time / iter_number


def performance_test(input_file, read_line=None):
    output_filename = "tmp.out"
    iter_number = 1000

    no_optimization_cmd = ["python3", "Compiler.py", "-f", "elf64", "-o", output_filename, input_file]
    no_optimization_time = performance_test_run(output_filename, no_optimization_cmd, read_line, iter_number)
    print("%s without optimization is %f" % (input_file, no_optimization_time))

    optimization_1_cmd = ["python3", "Compiler.py", "-f", "elf64", "-O", "1", "-o", output_filename, input_file]
    optimization_1_time = performance_test_run(output_filename, optimization_1_cmd, read_line, iter_number)
    print("%s with optimization 1 is %f" % (input_file, optimization_1_time))


class CompilerTest(unittest.TestCase):
    def test_optimization1(self):
        performance_test("tests/optimization1")


if __name__ == '__main__':
    unittest.main()
