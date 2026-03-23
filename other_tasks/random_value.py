"""
задан список вероятностей P = [0.1, 0.2, ...], так, что их сумма равна 1.
Сгенерировать случайный индекс с соответствующей вероятностью.
"""

from typing import Callable
import random


def bin_search(array: list[float], check: Callable[[list[float], int], bool]):
    left: int = 0
    right: int = len(array)
    while left < right:
        middle: int = (left + right) // 2
        if check(array, middle):
            right = middle
        else:
            left = middle + 1
    return left

def get_random_list(size: int, probabilities: list[float]):
    interval_value_list: list[float] = []
    for number in range(size):
        random_value: float = random.random()

print(random.random())