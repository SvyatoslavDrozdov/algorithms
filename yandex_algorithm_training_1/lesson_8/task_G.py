"""
Вводится последовательность целых чисел,оканчивающаяся нулем. Построить по ней дерево.
Для полученного дерева выведите список всех вершин, имеющих только одного ребёнка, в порядке возрастания.
"""

from __future__ import annotations
from typing import Iterator


class Tree:
    def __init__(self, value: int) -> None:
        self.value: int = value
        self.left_child: Tree | None = None
        self.right_child: Tree | None = None

    def add_new_value(self, new_value: int) -> None:
        """
        Insert a new value into the binary tree. If the value already exists in the tree, no changes are made.
        :param new_value: Integer value to insert.
        """
        if new_value < self.value:
            if self.left_child:
                self.left_child.add_new_value(new_value)
            else:
                self.left_child = Tree(new_value)
        elif new_value > self.value:
            if self.right_child:
                self.right_child.add_new_value(new_value)
            else:
                self.right_child = Tree(new_value)

    def inorder_traverse(self) -> Iterator[int]:
        """
        Perform an in-order traversal of the binary search tree.
        :Yields: Integer node values in ascending order.
        """
        if self.left_child:
            yield from self.left_child.inorder_traverse()
        if (self.left_child and not self.right_child) or (not self.left_child and self.right_child):
            yield self.value
        if self.right_child:
            yield from self.right_child.inorder_traverse()


input_list = list(map(int, input().split()))[:-1]
my_tree = Tree(input_list[0])
for number in input_list[1:]:
    my_tree.add_new_value(number)

for value in my_tree.inorder_traverse():
    print(value)
