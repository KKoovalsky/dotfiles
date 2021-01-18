import re
import os


def is_header_file(path):
    return path.endswith('.h') or path.endswith('.hpp') or path.endswith('hxx')


def to_include_guard(filename):
    return re.sub(r'[^A-Za-z0-9]+', '_', filename).upper()


def get_class_name_from_few_previous_lines(vim_buffer, current_line_num):
    for i in range(0, 10):
        line = vim_buffer[current_line_num - i]
        match = re.match('(class|struct) (\\w+)', line)
        if match:
            return match.group(2)
    return ''


def test_file_name_to_pretty_pascal_case(filename):
    pretty_name = test_file_name_to_pretty(filename)
    return snake_case_to_pascal_case(pretty_name)


def snake_case_to_pascal_case(s):
    return s.replace("_", " ").title().replace(" ", "")


def test_file_name_to_pretty(filename):
    no_ext = os.path.splitext(filename)[0]
    no_test_str = no_ext.replace('test', '')
    no_leading_and_trailing_underscores = no_test_str.rstrip('_').lstrip('_')
    return no_leading_and_trailing_underscores

