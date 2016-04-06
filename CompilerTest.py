import os
import unittest

from subprocess import Popen, PIPE


def abstract_test_with_out(input_file, read_line=None):
    output_filename = "tmp.out"
    power_cmd = ["python3", "Compiler.py", "-f", "elf64", "-o", output_filename, input_file]
    p = Popen(power_cmd)
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
    power_cmd = ["python3", "Compiler.py", "-f", "elf64", "-o", output_filename, input_file]
    p = Popen(power_cmd)
    p.wait()
    p = Popen(["./%s" % output_filename], stdin=PIPE, stdout=PIPE)
    if read_line is not None:
        p.stdin.write(bytes(read_line, "UTF-8"))
    p.stdin.close()
    result = p.stdout.readline().decode("UTF-8")
    p.stdout.close()
    if result.startswith("Syntax error") or result.startswith("Value error"):
        return False
    os.remove(output_filename)
    return True


def abstract_test_incorrect_program(input_file):
    output_filename = "tmp.out"
    power_cmd = ["python3", "Compiler.py", "-f", "elf64", "-o", output_filename, input_file]
    p = Popen(power_cmd, stderr=PIPE)
    result = p.stderr.readline().decode("UTF-8")
    p.stderr.close()
    return result.startswith("Syntax error") or result.startswith("Value error")


class CompilerTest(unittest.TestCase):
    def test_power(self):
        n = 3
        k = 4
        result = abstract_test_with_out("tests/power", "%d\n%d\n" % (k, n))
        self.assertEqual(result, str(n ** k))

    def test_a_plus_b(self):
        a = 2
        b = -53
        result = abstract_test_with_out("tests/a_plus_b", "%d\n%d\n" % (a, b))
        self.assertEqual(result, str(a + b))

    def test_global_variable(self):
        result = abstract_test_with_out("tests/global_variable")
        self.assertEqual(result, str(0))

    def test_2_plus_2_is_4(self):
        result = abstract_test_with_out("tests/2_plus_2_is_4")
        self.assertEqual(result, str(1))

    def test_no_main(self):
        result = abstract_test_correct_program("tests/no_main")
        self.assertEqual(result, True)

    def test_incorrect_main(self):
        result = abstract_test_incorrect_program("tests/incorrect_main")
        self.assertEqual(result, True)

    def test_missing_return_statement(self):
        result = abstract_test_incorrect_program("tests/missing_return_statement")
        self.assertEqual(result, True)

    def test_function_incorrect_number_of_arguments(self):
        result = abstract_test_incorrect_program("tests/function_incorrect_number_of_arguments")
        self.assertEqual(result, True)

    def test_function_incorrect_arguments(self):
        result = abstract_test_incorrect_program("tests/function_incorrect_arguments")
        self.assertEqual(result, True)

    def test_expression_incorrect_type(self):
        result = abstract_test_incorrect_program("tests/expression_incorrect_type1")
        result &= abstract_test_incorrect_program("tests/expression_incorrect_type2")
        result &= abstract_test_incorrect_program("tests/expression_incorrect_type3")
        result &= abstract_test_incorrect_program("tests/expression_incorrect_type4")
        self.assertEqual(result, True)

    def test_while_incorrect_condition(self):
        result = abstract_test_incorrect_program("tests/while_incorrect_condition")
        self.assertEqual(result, True)

    def test_if_incorrect_condition(self):
        result = abstract_test_incorrect_program("tests/if_incorrect_condition")
        self.assertEqual(result, True)

    def test_deadcode(self):
        result = abstract_test_incorrect_program("tests/deadcode")
        self.assertEqual(result, True)

    def test_function_not_in_scope(self):
        result = abstract_test_incorrect_program("tests/function_not_in_scope")
        self.assertEqual(result, True)

    def test_variable_not_in_scope(self):
        result = abstract_test_incorrect_program("tests/variable_not_in_scope")
        self.assertEqual(result, True)


if __name__ == '__main__':
    unittest.main()
