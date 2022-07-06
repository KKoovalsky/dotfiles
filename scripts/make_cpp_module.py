#!/usr/bin/env python3

import click
import os
from os import path


@click.command()
@click.argument('module_name', type=str)
@click.argument('brief_description_in_header', type=str)
@click.option('--module_type',
              type=click.Choice(['static_lib', 'interface'],
                                case_sensitive=False),
              default='static_lib')
@click.option('--brief_in_cpp', type=str,
              help='Mandatory if --module_type is static_lib')
@click.option('--public_dependencies', type=str,
              help='CMake targets linked to the created library as PUBLIC')
def make_cpp_module(module_name,
                    brief_description_in_header,
                    module_type,
                    brief_in_cpp,
                    public_dependencies):
    if module_type == "static_lib" and not brief_in_cpp:
        raise RuntimeError(
            'Pass --brief_in_cpp as a brief description within the source file'
        )
    if module_type == 'interface':
        raise RuntimeError('Module type = interface not supported yet')

    os.mkdir(module_name)
    generate_header_file(module_name, brief_description_in_header)
    generate_source_file(module_name, brief_in_cpp)
    generate_cmake_file_for_static_lib(module_name, public_dependencies)


def generate_header_file(module_name: str, brief_description_in_header: str):
    filename = '{}.hpp'.format(module_name)
    include_guard = filename.upper().replace('.', '_')
    content = ('/**\n'
               ' * @file        {0}\n'
               ' * @brief       {1}\n'
               ' */\n'
               '#ifndef {2}\n'
               '#define {2}\n'
               '\n'
               '#endif /* {2} */\n').format(
        filename, brief_description_in_header, include_guard)
    p = path.join(module_name, filename)
    with open(p, 'w') as f:
        f.write(content)


def generate_source_file(module_name: str, brief_in_cpp: str):
    filename = '{}.cpp'.format(module_name)
    header_filename = '{}.hpp'.format(module_name)
    content = ('/**\n'
               ' * @file        {0}\n'
               ' * @brief       {1}\n'
               ' */\n'
               '\n'
               '#include "{2}"\n').format(
        filename, brief_in_cpp, header_filename)
    p = path.join(module_name, filename)
    with open(p, 'w') as f:
        f.write(content)


def generate_cmake_file_for_static_lib(module_name: str,
                                       public_dependencies: str):
    source_filename = '{}.cpp'.format(module_name)
    content = (
        'add_library({0} STATIC {1})\n'
        'target_include_directories({0} '
        'PUBLIC ${{CMAKE_CURRENT_LIST_DIR}})\n').format(
            module_name, source_filename)

    if public_dependencies:
        content += 'target_link_libraries({0} PUBLIC {1})'.format(
            module_name, public_dependencies)

    p = path.join(module_name, 'CMakeLists.txt')
    with open(p, 'w') as f:
        f.write(content)


if __name__ == '__main__':
    make_cpp_module()
