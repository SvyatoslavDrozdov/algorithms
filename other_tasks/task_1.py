"""
На вход подается последовательность чисел [a_1, ..., a_n] упорядоченная по возрастанию и число k.
Требуется найти 2 числа из массива, в сумме дающие число k.
"""


def find_values_with_given_sum(sorted_array: list[int], given_sum: int) -> set[tuple[int]]:
    values_with_given_sum = []

    left_index = 0
    right_index = len(sorted_array) - 1

    while left_index < right_index:
        left_value = sorted_array[left_index]
        right_value = sorted_array[right_index]
        current_sum = left_value + right_value
        if current_sum == given_sum:
            values_with_given_sum.append((left_value, right_value))
            left_index += 1
            right_index -= 1
        elif current_sum < given_sum:
            left_index += 1
        else:
            right_index -= 1

    return set(values_with_given_sum)


array_1 = [1, 2, 3, 4, 5]
sum_1 = 6
print(find_values_with_given_sum(array_1, sum_1))

array_2 = [0, 1, 5, 5, 5, 5, 10]
sum_2 = 10
print(find_values_with_given_sum(array_2, sum_2))

array_3 = [-1, 2, 5, 8]
sum_3 = 7
print(find_values_with_given_sum(array_3, sum_3))
