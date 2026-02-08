def calculate_profit_board(board_cell_values: list[list[int]]) -> list[list[int]]:
    height: int = len(board_cell_values)
    width: int = len(board_cell_values[0])
    board_cell_values_padded: list[list[int]] = [[0] * (width + 1)]
    for row_idx in range(height):
        board_cell_values_padded.append([0] + board_cell_values[row_idx])

    dp: list[list[int]] = [[0] * (width + 1) for _ in range(height + 1)]

    for row_number in range(1, height + 1):
        for column_number in range(1, width + 1):
            dp[row_number][column_number] = (max(dp[row_number - 1][column_number], dp[row_number][column_number - 1])
                                             + board_cell_values_padded[row_number][column_number]
                                             )
    return dp


def find_profit_and_path(board_cell_values: list[list[int]]) -> tuple[int, str]:
    max_income_padded: list[list[int]] = calculate_profit_board(board_cell_values)
    height: int = len(max_income_padded) - 1
    width: int = len(max_income_padded[0]) - 1
    current_cell: tuple[int, int] = (height, width)
    way_list: list[str] = []

    while current_cell != (1, 1):
        row, column = current_cell
        current_income: int = max_income_padded[row][column]
        previous_income: int = current_income - board_cell_values[row - 1][column - 1]

        if row - 1 >= 1 and max_income_padded[row - 1][column] == previous_income:
            current_cell = (row - 1, column)
            way_list.append("D")
        else:
            current_cell = (row, column - 1)
            way_list.append("R")
    way_str = " ".join(way_list[::-1])
    return max_income_padded[height][width], way_str


def main() -> None:
    board_height, _ = map(int, input().split())
    board_cell_values: list[list[int]] = []
    for _ in range(board_height):
        board_cell_values.append(list(map(int, input().split())))

    profit, way = find_profit_and_path(board_cell_values)
    print(profit)
    print(way)


if __name__ == "__main__":
    main()
