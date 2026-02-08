from typing import Callable


def calculate_constants(value_of_squares: list[list[int]]) -> tuple[int, int, int, int]:
    height: int = len(value_of_squares)
    width: int = len(value_of_squares[0])

    MAX_SQUARE_COST: int = 100
    MAX_WAY_COST: int = MAX_SQUARE_COST * (height + width - 1)
    INFTY: int = MAX_WAY_COST + 1

    return height, width, INFTY, MAX_WAY_COST


def is_possible_to_pass(initial_money: int, value_of_squares: list[list[int]]) -> bool:
    height, width, INFTY, MAX_WAY_COST = calculate_constants(value_of_squares)

    board_cost: list[list[int]] = [[0] * (width + 1)]
    for row_idx in range(height):
        board_cost.append([0] + value_of_squares[row_idx])

    dp: list[list[int]] = [[INFTY] * (width + 1) for _ in range(height + 1)]
    dp[0][1], dp[1][0] = 0, 0
    for raw_number in range(1, height + 1):
        for column_number in range(1, width + 1):
            dp[raw_number][column_number] = (min(dp[raw_number - 1][column_number], dp[raw_number][column_number - 1]) +
                                             board_cost[raw_number][column_number]
                                             )
            if initial_money - dp[raw_number][column_number] < 0:
                dp[raw_number][column_number] = INFTY

    return dp[height][width] < INFTY


def binary_search(numbers: list[int], predicate: Callable[[int], bool]) -> int:
    left: int = 0
    right: int = len(numbers)

    while left < right:
        middle: int = (left + right) // 2
        if predicate(numbers[middle]):
            right = middle
        else:
            left = middle + 1

    return left


def get_predicate(value_of_squares: list[list[int]]) -> Callable[[int], bool]:
    def is_there_enough_money(initial_money: int) -> bool:
        return is_possible_to_pass(initial_money, value_of_squares)

    return is_there_enough_money


def calculate_required_money(values_of_squares: list[list[int]]) -> int:
    *_, MAX_WAY_COST = calculate_constants(values_of_squares)
    possible_money: list[int] = list(range(MAX_WAY_COST + 1))
    required_money: int = binary_search(possible_money, get_predicate(values_of_squares))

    return required_money


board_height, board_width = map(int, input().split())

board_values: list[list[int]] = []

for raw_idx in range(board_height):
    board_values.append(list(map(int, input().split())))

calculated_required_money: int = calculate_required_money(board_values)
print(calculated_required_money)
