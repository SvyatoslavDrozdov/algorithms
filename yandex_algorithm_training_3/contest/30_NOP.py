def calculate_dp(first_sequence: list[int], second_sequence: list[int]) -> list[list[int]]:
    first_sequence_len: int = len(first_sequence)
    second_sequence_len: int = len(second_sequence)
    first_sequence_padded: list[int | None] = [None] + first_sequence
    second_sequence_padded: list[int | None] = [None] + second_sequence
    dp: list[list[int]] = [[0] * (second_sequence_len + 1) for _ in range(first_sequence_len + 1)]
    for row_number in range(1, first_sequence_len + 1):
        for column_number in range(1, second_sequence_len + 1):
            if first_sequence_padded[row_number] == second_sequence_padded[column_number]:
                dp[row_number][column_number] = dp[row_number - 1][column_number - 1] + 1
            else:
                dp[row_number][column_number] = max(dp[row_number - 1][column_number],
                                                    dp[row_number][column_number - 1])

    return dp


def get_common_subsequence(first_sequence: list[int], second_sequence: list[int]) -> list[int]:
    dp: list[list[int]] = calculate_dp(first_sequence, second_sequence)
    first_sequence_len: int = len(first_sequence)
    second_sequence_len: int = len(second_sequence)
    first_sequence_padded: list[int | None] = [None] + first_sequence
    second_sequence_padded: list[int | None] = [None] + second_sequence
    row_number: int = first_sequence_len
    column_number: int = second_sequence_len
    common_subsequence: list[int] = []
    while row_number > 0 and column_number > 0:
        if first_sequence_padded[row_number] == second_sequence_padded[column_number]:
            common_subsequence.append(first_sequence_padded[row_number])
            row_number -= 1
            column_number -= 1
        elif dp[row_number - 1][column_number] >= dp[row_number][column_number - 1]:
            row_number -= 1
        else:
            column_number -= 1
    return common_subsequence[::-1]


def main() -> None:
    first_sequence_len: int = int(input())
    first_sequence: list[int] = list(map(int, input().split()))
    second_sequence_len: int = int(input())
    second_sequence: list[int] = list(map(int, input().split()))
    max_common_subsequence: list[int] = get_common_subsequence(first_sequence, second_sequence)
    print(*max_common_subsequence)


if __name__ == "__main__":
    main()
