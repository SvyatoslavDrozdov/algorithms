"""
Дан список целых чисел. Для каждого числа в этом списке найти индекс ближайшего справа меньшего числа.
"""

from collections import deque


def find_nearest_less_value_index(numbers: list[int]) -> list[tuple[int, int]]:
    numbers_len: int = len(numbers)
    numbers_and_indexes_list: list[tuple[int, int]] = [(number, numbers_len) for number in numbers]
    stack: deque[tuple[int, int]] = deque()
    for number_idx, number in enumerate(numbers):
        while stack and stack[-1][0] > number:
            last_number, last_number_idx = stack.pop()
            numbers_and_indexes_list[last_number_idx] = (last_number, number_idx)
        stack.append((number, number_idx))

    return numbers_and_indexes_list


numbers_example: list[int] = list(map(int, input().split()))
print(find_nearest_less_value_index(numbers_example))
