import vim


class MatchNotFoundError(Exception):
    pass


def create_unity_test(name):
    lines = current_vim_buffer_to_lines()
    declaration_line_nr = find_number_of_line_to_put_declaration(lines)
    definition_line_nr = find_number_of_line_to_put_definition(lines)
    invocation_line_nr = find_number_of_line_to_put_test_invocation(lines)

    declaration = make_test_declaration_string(name)
    definition = make_test_definition_lines(name)
    invocation = make_test_invocation_string(name)

    current_buffer = vim.current.buffer
    current_buffer.append([declaration], declaration_line_nr)

    declaration_line_length = 1
    current_buffer.append(
        definition, definition_line_nr + declaration_line_length)

    definition_line_length = len(definition)
    current_buffer.append(
        invocation,
        invocation_line_nr + definition_line_length + declaration_line_length)


def current_vim_buffer_to_lines():
    return list(vim.current.buffer)


def find_number_of_line_to_put_declaration(lines):
    matcher = 'End of group'
    return find_line_that_contains(lines, matcher) - 2


def find_number_of_line_to_put_definition(lines):
    runner_heading_line_nr = find_line_that_contains(
        lines, 'Runner')
    return runner_heading_line_nr - 2


def find_number_of_line_to_put_test_invocation(lines):
    return find_line_that_contains(lines, 'UNITY_END') - 2


def make_test_declaration_string(name):
    return 'static void {}();'.format(name)


def make_test_definition_lines(name):
    return ['static void {}()'.format(name),
            '{',
            '    TEST_ASSERT(FALSE);',
            '}',
            '']


def make_test_invocation_string(name):
    return '    RUN_TEST({});'.format(name)


def find_line_that_contains(lines, matcher):
    first_line_nr = 1
    try:
        return next(i for i, v in enumerate(
            lines, first_line_nr) if matcher in v)
    except StopIteration:
        raise MatchNotFoundError


def find_line_that_contains_reverse_search_from_line(
        lines, matcher, line_begin):
    first_line_nr = 1
    lines_range = lines[:line_begin]
    try:
        return next(i for i, v in reversed(list(enumerate(
            lines_range, first_line_nr))) if matcher in v)
    except StopIteration:
        raise MatchNotFoundError
