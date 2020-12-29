import os
from pathlib import Path


def find_corresponding_source_or_header_file(cpp_file: str):
    if cpp_file.endswith('.cpp'):
        return find_corresponding_header_file(cpp_file)
    else:
        return find_corresponding_source_file(cpp_file)


def find_corresponding_source_file(header_file):
    corresponding_source_file = _get_filename_without_extension(
        header_file) + '.cpp'
    return _find_file_recursively(corresponding_source_file)


def find_corresponding_header_file(source_file):
    corresponding_header_file = _get_filename_without_extension(
        source_file) + '.hpp'
    return _find_file_recursively(corresponding_header_file)


def _get_filename_without_extension(path):
    fname = os.path.basename(path)
    return os.path.splitext(fname)[0]


def _find_file_recursively(filename):
    matches = Path('.').rglob(filename)
    match = next(matches, None)
    if not match:
        raise FileNotFoundError(filename)
    return str(match.absolute())
