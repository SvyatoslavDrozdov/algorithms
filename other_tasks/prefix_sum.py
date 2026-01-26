"""
Реализация префиксной суммы.
"""


def get_prefix_sum(array: list[int]) -> list[int]:
    """
    Создает список префиксных сумм.
    :param array: входной список чисел
    :return: список префиксных сумм. Сумма от элемента с индексом left включительно
        до элемента с индексом right не включительно считается по формуле:
        sum_left_right = prefix_sum(right) - prefix_sum(left)
    """
    prefix_sum: list[int] = [0] * (len(array) + 1)
    for i in range(1, len(array) + 1):
        prefix_sum[i] = prefix_sum[i - 1] + array[i - 1]
    return prefix_sum


array_1 = [1, 2, 3, 4, 5, 6, 7]
left_1 = 1
right_1 = 4
prefix_sum_1 = get_prefix_sum(array_1)
sum_left_right_1 = prefix_sum_1[right_1] - prefix_sum_1[left_1]
print(sum_left_right_1)
