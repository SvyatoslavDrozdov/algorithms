"""
В генеалогическом древе у каждого человека, кроме родоначальника, есть ровно один родитель.
Для каждого элемента дерева определите число всех его потомков (не считая его самого).
Программа получает на вход число элементов в генеалогическом древе N. Далее следует N−1 строка, задающие родителя для
каждого элемента древа, кроме родоначальника. Каждая строка имеет вид имя_потомка имя_родителя.

Выведите список всех элементов в лексикографическом порядке, для каждого элемента выводите количество всех его потомков.
"""

from __future__ import annotations
import sys

sys.setrecursionlimit(100000)


class Node:
    def __init__(self, person_name: str) -> None:
        self.person_name: str = person_name
        self.children: list[Node] = []
        self.all_children_children_info: dict[str, int] = {}

    def add_child(self, child: Node) -> None:
        self.children.append(child)

    def get_descendant_number(self, root: Node) -> int:
        number_of_descendants: int = 0

        if self.children:
            for person in self.children:
                number_of_descendants += 1
                number_of_descendants += person.get_descendant_number(root)
        else:
            root.all_children_children_info[self.person_name] = 0
            return 0
        root.all_children_children_info[self.person_name] = number_of_descendants
        return number_of_descendants


number_of_peoples: int = int(input())
tree_info: dict[str, Node] = {}
for _ in range(number_of_peoples - 1):
    child_name, parent_name = input().split()

    if parent_name in tree_info:
        parent_node = tree_info[parent_name]
    else:
        parent_node = Node(parent_name)
        tree_info[parent_name] = parent_node
    if child_name in tree_info:
        parent_node.add_child(tree_info[child_name])
    else:
        child_node = Node(child_name)
        parent_node.add_child(child_node)
        tree_info[child_name] = child_node

children_amount_data: list[tuple[str, int]] = []

has_parent = set()
for name in tree_info:
    node = tree_info[name]
    for child_node in node.children:
        has_parent.add(child_node.person_name)

root_node: Node | None = None
for name in tree_info:
    if name not in has_parent:
        root_node = tree_info[name]

root_children = root_node.get_descendant_number(root_node)
children_children_info = root_node.all_children_children_info
for human_name in children_children_info:
    children_number = children_children_info[human_name]
    children_amount_data.append((human_name, children_number))

children_amount_data.sort()
for human_name, children_number in children_amount_data:
    print(human_name, children_number)
