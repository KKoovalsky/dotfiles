import clang.cindex as clcidx
import os
import itertools


def find_last_line_of_constructor(class_name, source_file):
    ctor = _get_first_node_that_matches(
        _is_constructor_of_class(class_name), source_file)
    return ctor.extent.end.line


def find_class_name_of_method_at_line(header_file, method_line_num):
    method_cursor = _find_method_at_line(header_file, method_line_num)
    return method_cursor.semantic_parent.displayname


def _find_method_at_line(source_file, line_number):
    return _get_first_node_that_matches(_is_method_at_line(line_number),
                                        source_file)


def _get_first_node_that_matches(predicate, source_file):
    nodes_it = _get_translation_unit_nodes_from_file(source_file)
    matches_it = _filter_nodes(nodes_it, predicate)
    return next(matches_it)


def _get_translation_unit_nodes_from_file(source_file):
    index = clcidx.Index.create()
    tu = index.parse(source_file)
    filename = os.path.split(source_file)[-1]
    return filter(lambda x: x.location.file.name.endswith(filename),
                  tu.cursor.get_children())


def _filter_nodes(nodes_it, predicate):
    list_with_filtered = [
        filter(predicate, node.walk_preorder()) for node in nodes_it]
    return itertools.chain.from_iterable(list_with_filtered)


def _is_constructor_of_class(class_name):
    return lambda node: node.kind == clcidx.CursorKind.CONSTRUCTOR and \
        '{}'.format(class_name) in node.displayname


def _is_method_at_line(line_number):
    return lambda node: node.kind == clcidx.CursorKind.CXX_METHOD and \
        node.extent.start.line == line_number
