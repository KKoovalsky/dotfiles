import clang.cindex as clcidx
import os


def _is_constructor_of_class(class_name):
    return lambda node: node.kind == clcidx.CursorKind.CONSTRUCTOR and \
        '{}'.format(class_name) in node.displayname


def find_last_line_of_constructor(class_name, source_file):
    cursor = _get_translation_unit_nodes_from_file(source_file)
    ctor = next(filter(_is_constructor_of_class(
        class_name), cursor.walk_preorder()))
    return ctor.extent.end.line


def _get_translation_unit_nodes_from_file(source_file):
    index = clcidx.Index.create()
    tu = index.parse(source_file)
    filename = os.path.split(source_file)[-1]
    return next(filter(lambda x: x.location.file.name.endswith(filename),
                       tu.cursor.get_children()))
