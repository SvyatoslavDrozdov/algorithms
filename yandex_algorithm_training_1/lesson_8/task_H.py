"""
Дерево называется АВЛ-сбалансированным, если для любой его вершины высота левого и правого поддерева для этой вершины
различаются не более чем на 1.Вводится последовательность целых чисел, оканчивающаяся нулем. Сам ноль в
последовательность не входит. Постройте дерево, соответствующее данной последовательности.
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

        left_tree_depth: int = -1
        right_tree_depth: int = -1
        if self.left_child:
            left_tree_depth = self.left_child.get_depth()
        if self.right_child:
            right_tree_depth = self.right_child.get_depth()

        if abs(left_tree_depth -right_tree_depth) <= 1:
            yield True
        else:
            yield False
        if self.right_child:
            yield from self.right_child.inorder_traverse()

    def get_depth(self) -> int:
        left_tree_depth: int = -1
        right_tree_depth: int = -1
        if self.left_child:
            left_tree_depth = self.left_child.get_depth()
        if self.right_child:
            right_tree_depth = self.right_child.get_depth()
        depth: int = 1 + max(left_tree_depth, right_tree_depth)
        return depth



input_list = list(map(int, input().split()))[:-1]
my_tree = Tree(input_list[0])
for number in input_list[1:]:
    my_tree.add_new_value(number)

flag_no= False
for value in my_tree.inorder_traverse():
    if not value:
        print("NO")
        flag_no = True
        break
if not flag_no:
    print("YES")