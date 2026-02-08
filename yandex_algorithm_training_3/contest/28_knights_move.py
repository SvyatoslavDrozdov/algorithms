def count_knight_paths(board_height: int, board_width: int) -> int:
    """
    :param board_height: Height of the board.
    :param board_width: Width of the board.
    :return: Number of possible knight paths from cell (1,1) to cell (board_height, board_width).
    """
    dp: list[list[int]] = [[0] * (board_width + 1) for _ in range(board_height + 1)]
    dp[1][1] = 1
    for row_number in range(2, board_height + 1):
        for column_number in range(2, board_width + 1):
            dp[row_number][column_number] = (dp[row_number - 2][column_number - 1]
                                             + dp[row_number - 1][column_number - 2]
                                             )
    return dp[board_height][board_width]


def main() -> None:
    board_height, board_width = map(int, input().split())
    print(count_knight_paths(board_height, board_width))


if __name__ == "__main__":
    main()
