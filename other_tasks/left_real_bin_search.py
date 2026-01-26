"""
Реализация левого бинарного поиска. Рассматривается вещественный отрезок. Есть функция
is_true(element), которая возвращает bool. Левый бинпоиск возвращает первое число в отрезке,
для которого is_true вернула True с погрешностью eps. Если такого числа нет, возвращается
верхняя грань диапазона с погрешностью eps.
Для возрастающей последовательности чисел функция is_true может давать такую
последовательность bool: F F F F F T T T T
"""

import typing as tp
import numpy as np


def left_real_bin_search(left_boundary: float, right_boundary: float, eps: float,
                         is_true: tp.Callable[[float], bool]) -> float:
    """
    :param left_boundary: нижняя гарница диапазона
    :param right_boundary: верхняя граница диапазона
    :param eps: допустимая погрешность
    :param is_true: функция ставящая в соответствие числу bool
    :return: первое число в отрезке, для которого is_true вернула True с погрешностью eps.
    """
    left = left_boundary
    right = right_boundary

    while right - left > eps:
        middle_point = (left + right) / 2
        if is_true(middle_point):
            right = middle_point
        else:
            left = middle_point
    return left


def x_squared(x: float) -> float:
    return x ** 2 - 1


def sin_x(x: float) -> float:
    return np.sin(x)


def is_true_ex(x: float) -> bool:
    return x_squared(x) > sin_x(x)


left_boundary_ex = 0
right_boundary_ex = 3
eps_ex = 1e-6
root_of_equation = left_real_bin_search(left_boundary_ex, right_boundary_ex, eps_ex, is_true_ex)

print(f"Корень уравнения sin(x) = x**2 это x_0 = {round(root_of_equation, 4)}")
