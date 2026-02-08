from typing import Callable
import bisect


def calculate_constants(value_of_squares: list[list[int]]) -> tuple[int, int, int, int]:
    height: int = len(value_of_squares)
    wide: int = len(value_of_squares[0])

    MAX_SQUARE_COST: int = 100
    MAX_WAY_COST: int = MAX_SQUARE_COST * (height + wide - 1)
    INFTY: int = MAX_WAY_COST + 1

    return height, wide, INFTY, MAX_WAY_COST


def is_possible_to_pass(initial_money: int, value_of_squares: list[list[int]]) -> bool:
    height, wide, INFTY, MAX_WAY_COST = calculate_constants(value_of_squares)

    board_cost: list[list[int]] = [[0] * (wide + 1)]
    for row_idx in range(height):
        board_cost.append([0] + value_of_squares[row_idx])

    dp: list[list[int]] = [[INFTY] * (wide + 1) for _ in range(height + 1)]
    dp[0][1], dp[1][0] = 0, 0
    for raw_number in range(1, height + 1):
        for column_number in range(1, wide + 1):
            dp[raw_number][column_number] = (min(dp[raw_number - 1][column_number], dp[raw_number][column_number - 1]) +
                                             board_cost[raw_number][column_number]
                                             )
            if initial_money - dp[raw_number][column_number] < 0:
                dp[raw_number][column_number] = INFTY

    return dp[height][wide] < INFTY


def get_predicate(value_of_squares: list[list[int]]) -> Callable[[int], bool]:
    def is_there_enough_money(initial_money: int) -> bool:
        return is_possible_to_pass(initial_money, value_of_squares)

    return is_there_enough_money


def calculate_required_money(values_of_squares: list[list[int]]) -> int:
    *_, MAX_WAY_COST = calculate_constants(values_of_squares)
    possible_money: list[int] = list(range(MAX_WAY_COST + 1))
    required_money: int = bisect.bisect_left(possible_money, True, key=get_predicate(values_of_squares))
    return required_money


board_height, board_wide = map(int, input().split())

board_values: list[list[int]] = []

for raw_idx in range(board_height):
    board_values.append(list(map(int, input().split())))

calculated_required_money: int = calculate_required_money(board_values)
print(calculated_required_money)
