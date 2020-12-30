import subprocess
import vim


def replace_word_project_wise(word, replace_word):
    files_having_word = _get_cpp_files_containing(word)
    for f in files_having_word:
        if _is_file_currently_open_in_vim(f):
            _replace_in_vim_buffer(f, word, replace_word)
        else:
            _replace_in_place(f, word, replace_word)


def _get_cpp_files_containing(word):
    cmd = ['git', 'grep', '--untracked', '-l', '-rne',
           word, '--', '*.c', '*.cpp', '*.h', '*.hpp']
    res = subprocess.run(cmd, stdout=subprocess.PIPE)
    return [e.decode('utf-8') for e in res.stdout.splitlines()]


def _replace_in_place(filepath, word_to_be_replaced, new_word):
    cmd = ['sed', '-i',
           "s/{}/{}/g".format(word_to_be_replaced, new_word), filepath]
    subprocess.run(cmd)


def _is_file_currently_open_in_vim(filepath):
    buffer_names = [b.name for b in list(vim.buffers)]
    has_filepath = (n for n in buffer_names if n.endswith(filepath))
    return next(has_filepath, None) is not None


def _replace_in_vim_buffer(filepath, word_to_be_replaced, new_word):
    corresponding_buffer = next(filter(lambda b: b.name.endswith(filepath),
                                       list(vim.buffers)))
    num_lines = len(corresponding_buffer)
    for line_nr in range(num_lines):
        current_line = corresponding_buffer[line_nr]
        if word_to_be_replaced in current_line:
            corresponding_buffer[line_nr] = current_line.replace(
                word_to_be_replaced, new_word)
