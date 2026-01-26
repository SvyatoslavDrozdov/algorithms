"""
Реализация левого бинарного поиска. Рассматривается массив целых чисел. Есть функция
is_true(element), которая возвращает bool. Левый бинпоиск возвращает индекс первого элемента
исходного массива, для которого is_true вернула True. Если такого элемента нет, возвращается
длина исходного массива.
Примеры: F F F F T T T -> 4, F F F -> 3.
"""

import typing as tp


def left_bin_search(array: list[int], is_true: tp.Callable[[int], bool]) -> int:
    """
    :param array: список целых чисел
    :param is_true: функция, ставящая в соответствие числу True или False
    :return: индекс первого элемента, для которого is_true вернула True или длина array,
        если такого элемента не существует.
    """
    left_idx = 0
    right_idx = len(array)
    while left_idx < right_idx:
        middle_idx = (left_idx + right_idx) // 2
        if is_true(middle_idx):
            right_idx = middle_idx
        else:
            left_idx = middle_idx + 1
    return left_idx


def is_true_ex_1(x: int) -> bool:
    return x > 5


array_ex_1 = [0, 1, 2, 3, 4, 5, 9, 10]
print(left_bin_search(array_ex_1, is_true_ex_1))
