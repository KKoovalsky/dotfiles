import re
import cpp_file_navigator
import vim


class ExtendedSignature:

    def __init__(self,
                 return_type,
                 signature_with_param_names_and_no_return_type):
        self.return_type = return_type
        s = signature_with_param_names_and_no_return_type
        self.signature_with_param_names_and_no_return_type = s

    def __repr__(self):
        return '{} {}'.format(
            self.return_type,
            self.signature_with_param_names_and_no_return_type)


def create_snippet_with_method_definition_for_method_under_cursor():
    current_line = vim.current.line
    current_line_number = vim.current.range.start + 1
    current_file = vim.current.buffer.name
    extended_signature = _get_extended_signature_from_line(current_line)
    class_name = cpp_file_navigator.find_class_name_of_method_at_line(
        current_file, current_line_number)
    method_definition = _make_line_with_method_definition(
        class_name, extended_signature)
    return '\n{}\n{{\n    $0\n}}'.format(method_definition)


def _get_extended_signature_from_line(line):
    regex = r'(\w+) (\w+)\((.*)\)'
    match = re.search(regex, line)
    return_type = match.group(1)
    function_name = match.group(2)
    params = match.group(3)
    return ExtendedSignature(
        return_type, '{}({})'.format(function_name, params))


def _make_line_with_method_definition(class_name, extended_signature):
    return '{} {}::{}'.format(
        extended_signature.return_type,
        class_name,
        extended_signature.signature_with_param_names_and_no_return_type)
