"""
В генеалогическом древе у каждого человека, кроме родоначальника, есть ровно один родитель. Каждому элементу дерева
сопоставляется целое неотрицательное число, называемое высотой. У родоначальника высота равна 0, у любого другого
элемента высота на 1 больше, чем у его родителя. Вам дано генеалогическое древо, определите высоту всех его элементов.

Программа получает на вход число элементов в генеалогическом древе N. Далее следует N−1 строка, задающие родителя для
каждого элемента древа, кроме родоначальника. Каждая строка имеет вид имя_потомка имя_родителя.

Программа должна вывести список всех элементов древа в лексикографическом порядке. После вывода имени каждого элемента
необходимо вывести его высоту.
"""

from __future__ import annotations
import sys

sys.setrecursionlimit(100000)


class Node:
    def __init__(self, person_name: str) -> None:
        self.person_name: str = person_name
        self.children: list[Node] = []
        self.high: int = 0

    def add_child(self, child: Node) -> None:
        self.children.append(child)

    def update_high(self) -> None:
        if self.children:
            for person in self.children:
                person.high = self.high + 1
                person.update_high()


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

root_node.update_high()

for human_name in tree_info:
    human_high = tree_info[human_name].high
    children_amount_data.append((human_name, human_high))

children_amount_data.sort()
for human_name, children_number in children_amount_data:
    print(human_name, children_number)
