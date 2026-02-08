from collections import deque

number_of_cities: int = int(input())
average_cost_of_life: list[int] = list(map(int, input().split()))


def find_idx_of_first_less_number(numbers: list[int]) -> list[int]:
    stack: deque[int] = deque([])
    idx_of_less_numbers: list[int] = [0] * len(numbers)

    for number_idx, number in enumerate(numbers):
        while stack and number < numbers[stack[-1]]:
            value_idx = stack.pop()
            idx_of_less_numbers[value_idx] = number_idx
        stack.append(number_idx)

    while stack:
        value_idx = stack.pop()
        idx_of_less_numbers[value_idx] = -1

    return idx_of_less_numbers


print(*find_idx_of_first_less_number(average_cost_of_life))
