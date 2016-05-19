import os
import random
import subprocess
import unittest
from subprocess import Popen, PIPE

import itertools


def abstract_test_with_out(input_file, read_line=None):
    output_filename = "tmp.out"
    cmd = ["python3", "Compiler.py", "-f", "elf64", "-o", output_filename, input_file]
    p = Popen(cmd)
    p.wait()
    p = Popen(["./%s" % output_filename], stdin=PIPE, stdout=PIPE)
    if read_line is not None:
        p.stdin.write(bytes(read_line, "UTF-8"))
    p.stdin.close()
    result = p.stdout.readline().decode("UTF-8")
    p.stdout.close()
    os.remove(output_filename)
    return result


def abstract_test_correct_program(input_file, read_line=None):
    output_filename = "tmp.out"
    cmd = ["python3", "Compiler.py", "-f", "elf64", "-o", output_filename, input_file]
    p = Popen(cmd)
    p.wait()
    p = Popen(["./%s" % output_filename], stdin=PIPE, stdout=PIPE, stderr=PIPE)
    if read_line is not None:
        p.stdin.write(bytes(read_line, "UTF-8"))
    p.stdin.close()
    out_result = p.stdout.readline().decode("UTF-8")
    err_result = p.stderr.readline().decode("UTF-8")
    p.stdout.close()
    p.stderr.close()
    os.remove(output_filename)
    return not is_incorrect_output(out_result) and not is_incorrect_output(err_result)


def abstract_test_incorrect_program(input_file):
    output_filename = "tmp.out"
    cmd = ["python3", "Compiler.py", "-f", "elf64", "-o", output_filename, input_file]
    p = Popen(cmd, stdout=PIPE, stderr=PIPE)
    out_result = p.stdout.readline().decode("UTF-8")
    err_result = p.stderr.readline().decode("UTF-8")
    p.stdout.close()
    p.stderr.close()
    if is_incorrect_output(out_result) or is_incorrect_output(err_result):
        return True
    p.wait()
    try:
        # e.g. Floating point exception (core dumped)
        subprocess.check_call(["./%s" % output_filename])
        return False
    except subprocess.CalledProcessError:
        return True


def is_incorrect_output(result):
    return result.startswith("Syntax error") or result.startswith("Value error")


class CompilerTest(unittest.TestCase):
    def test_power(self):
        n = 3
        k = 4
        result = abstract_test_with_out("tests/power", "%d\n%d\n" % (k, n))
        self.assertEqual(str(n ** k), result)

    def test_a_plus_b(self):
        a = 2
        b = -53
        result = abstract_test_with_out("tests/a_plus_b", "%d\n%d\n" % (a, b))
        self.assertEqual(str(a + b), result)

    def test_global_variable(self):
        result = abstract_test_with_out("tests/global_variable")
        self.assertEqual(str(0), result)

    def test_2_plus_2_is_4(self):
        result = abstract_test_with_out("tests/2_plus_2_is_4")
        self.assertEqual(str(1), result)

    def test_global_2_plus_2_is_4(self):
        result = abstract_test_with_out("tests/global_2_plus_2_is_4")
        self.assertEqual(str(1), result)

    def test_no_main(self):
        result = abstract_test_correct_program("tests/no_main")
        self.assertEqual(True, result)

    def test_incorrect_main(self):
        result = abstract_test_incorrect_program("tests/incorrect_main")
        self.assertEqual(True, result)

    def test_missing_return_statement(self):
        result = abstract_test_incorrect_program("tests/missing_return_statement")
        self.assertEqual(True, result)

    def test_function_incorrect_number_of_arguments(self):
        result = abstract_test_incorrect_program("tests/function_incorrect_number_of_arguments")
        self.assertEqual(True, result)

    def test_function_incorrect_arguments(self):
        result = abstract_test_incorrect_program("tests/function_incorrect_arguments")
        self.assertEqual(True, result)

    def test_expression_incorrect_type(self):
        result = abstract_test_incorrect_program("tests/expression_incorrect_type1")
        result &= abstract_test_incorrect_program("tests/expression_incorrect_type2")
        result &= abstract_test_incorrect_program("tests/expression_incorrect_type3")
        result &= abstract_test_incorrect_program("tests/expression_incorrect_type4")
        self.assertEqual(True, result)

    def test_while_incorrect_condition(self):
        result = abstract_test_incorrect_program("tests/while_incorrect_condition")
        self.assertEqual(True, result)

    def test_if_incorrect_condition(self):
        result = abstract_test_incorrect_program("tests/if_incorrect_condition")
        self.assertEqual(True, result)

    def test_deadcode(self):
        result = abstract_test_incorrect_program("tests/deadcode")
        self.assertEqual(True, result)

    def test_function_not_in_scope(self):
        result = abstract_test_incorrect_program("tests/function_not_in_scope")
        self.assertEqual(True, result)

    def test_variable_not_in_scope(self):
        result = abstract_test_incorrect_program("tests/variable_not_in_scope")
        self.assertEqual(True, result)

    def test_simple_array(self):
        result = abstract_test_with_out("tests/simple_array")
        self.assertEqual("1234", result)

    def test_array_as_function_argument(self):
        result = abstract_test_with_out("tests/array_as_function_argument")
        self.assertEqual("5", result)

    def test_change_array_in_function(self):
        result = abstract_test_with_out("tests/change_array_in_function")
        self.assertEqual("10", result)

    def test_try_to_return_array(self):
        result = abstract_test_incorrect_program("tests/try_to_return_array")
        self.assertEqual(True, result)

    def test_two_dimension_array(self):
        result = abstract_test_with_out("tests/two_dimension_array")
        self.assertEqual("15", result)

    def test_hard_hello(self):
        name = "Ivan"
        age = 23
        result = abstract_test_with_out("tests/hard_hello", "%s\n%d\n" % (name, age))
        self.assertEqual("Hello %s, %d y/o" % (name, age), result)

    def test_palindrome(self):
        string = "123321"
        result = abstract_test_with_out("tests/palindrome", "%s\n" % string)
        self.assertEqual("true", result)

    def test_palindrome2(self):
        string = "123"
        result = abstract_test_with_out("tests/palindrome", "%s\n" % string)
        self.assertEqual("false", result)

    def test_two_bandits(self):
        for _ in itertools.repeat(None, 100):
            a = random.randint(0, 9)
            b = random.randint(0, 9 - a)
            result = abstract_test_with_out("tests/two_bandits", "%d %d\n" % (a, b))
            self.assertEqual("%d %d" % (max(0, b - 1), max(0, a - 1)), result, "Run two_bandits with %d %d" % (a, b))

    def test_about_grisha(self):
        for _ in itertools.repeat(None, 100):
            a = random.randint(0, 11)
            result = abstract_test_with_out("tests/about_grisha", "%d\n" % a)
            self.assertEqual("YES" if (12 - a) * 45 <= 4 * 60 else "NO", result, "Run about_grisha with %d" % a)


if __name__ == '__main__':
    unittest.main()
