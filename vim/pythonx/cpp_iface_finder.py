import subprocess
import re
import os
import vim


class VimBufferMatchError(Exception):
    pass


def get_git_not_ignored_and_untracked_files():
    tracked_content_cmd = subprocess.run(
        ['git', 'ls-files'], stdout=subprocess.PIPE)
    untracked_content_cmd = subprocess.run(
        ['git', 'ls-files', '--others', '--exclude-standard'],
        stdout=subprocess.PIPE)
    result = tracked_content_cmd.stdout.splitlines() + \
        untracked_content_cmd.stdout.splitlines()
    result = [e.decode('utf-8') for e in result]
    return set(filter(None, result))


def contains_abstract_class(filename):
    pattern = re.compile('virtual .* = 0;')
    for _, line in enumerate(open(filename)):
        it = re.finditer(pattern, line)
        if next(it, None) is not None:
            return True
    return False


def is_header_file(filename):
    ext = os.path.splitext(filename)[-1]
    return ext == '.h' or ext == '.hpp' or ext == '.hxx'


def find_abstract_class_files_recursively_in_current_directory():
    git_files = get_git_not_ignored_and_untracked_files()
    headers = list(filter(is_header_file, git_files))
    abstract_class_files = list(filter(contains_abstract_class, headers))
    return abstract_class_files


def get_class_name_from_file(path):
    regex = r'(struct|class) (\w+).*{'
    with open(path) as f:
        file_content = f.read()
        match = re.search(regex, file_content, re.DOTALL)
        return match.group(2)


def make_list_of_suffices_for_vim_confirm_string(number_of_choices):
    A = ord('A')
    Z = ord('Z')
    if A + number_of_choices > Z:
        max_choices = Z - A + 1
        raise ValueError(
            'Too many choices ({}) for VIM confirm list, max: {}'.format(
                number_of_choices, max_choices))
    suffices = [chr(A + i) for i in range(number_of_choices)]
    return ['&{}: '.format(e) for e in suffices]


def make_vim_confirm_string(suffices, iface_names):
    result = [''.join(e) for e in zip(suffices, iface_names)]
    return '\n'.join(result)


def prompt_for_interface_choice_and_get_choice_number(confirm_string):
    prompt_question = 'Which interface to implement?'
    render_prompt_cmd = 'let choice = confirm("{}", "{}")'.format(
        prompt_question, confirm_string)
    vim.command(render_prompt_cmd)
    return int(vim.eval('choice'))


def get_iface_function_signatures(iface_file):
    pattern = re.compile('virtual (.*) = 0;')
    with open(iface_file) as f:
        matches = [pattern.search(line) for line in f.readlines()]
        actual_matches = list(filter(None, matches))
        return [m.group(1) for m in actual_matches]


def make_overriden_function_declarations(iface_name, iface_file):
    signatures = get_iface_function_signatures(iface_file)
    return ['virtual {} override;'.format(s) for s in signatures]


def find_index_of_line_matching_regex(regex):
    vim_buffer = vim.current.window.buffer
    for i, line in enumerate(vim_buffer):
        if re.search(regex, line):
            return i
    raise VimBufferMatchError('No matching line found')


def find_index_of_line_with_class_declaration():
    regex = r'(struct|class) \w+'
    return find_index_of_line_matching_regex(regex)


def mark_current_class_iface_implementer(iface_name):
    index = find_index_of_line_with_class_declaration()
    vim_buffer = vim.current.window.buffer
    current_decl = vim_buffer[index]
    implementing_iface = '{} : public {}'.format(current_decl, iface_name)
    vim_buffer[index] = implementing_iface


def insert_inside_class_definition(lines):
    index = find_index_of_line_with_class_declaration()
    vim_buffer = vim.current.window.buffer
    index_inside = index + 2
    vim_buffer.append(lines, index_inside)


def find_index_of_line_with_include_statement():
    regex = r'#include'
    return find_index_of_line_matching_regex(regex)


def find_proper_line_for_include_statement():
    try:
        return find_index_of_line_with_include_statement() + 1
    except VimBufferMatchError:
        return find_index_of_line_with_class_declaration()


def add_include(path_to_include):
    index = find_proper_line_for_include_statement()
    include_file = os.path.split(path_to_include)[-1]
    line = '#include "{}"'.format(include_file)
    vim_buffer = vim.current.window.buffer
    vim_buffer.append(line, index)


def implement_interface():
    iface_files = find_abstract_class_files_recursively_in_current_directory()
    iface_names = [get_class_name_from_file(f) for f in iface_files]
    suffices = make_list_of_suffices_for_vim_confirm_string(len(iface_names))
    confirm_string = make_vim_confirm_string(suffices, iface_names)
    choice = prompt_for_interface_choice_and_get_choice_number(confirm_string)
    index = choice - 1
    iface_to_implement = iface_names[index]
    file_with_iface_definition = iface_files[index]
    overriden_function_declarations = make_overriden_function_declarations(
        iface_to_implement, file_with_iface_definition)
    mark_current_class_iface_implementer(iface_to_implement)
    insert_inside_class_definition(overriden_function_declarations)
    add_include(file_with_iface_definition)
