def count_binary_sequence(sequence_len: int) -> int:
    dp: list[int] = [0] * (sequence_len + 5)
    dp[0] = 1
    dp[-1] = 1
    for position in range(1, sequence_len + 1):
        dp[position] = 2 * dp[position - 1] - dp[position - 4]

    return dp[sequence_len]


sequence_len_example: int = int(input())
print(count_binary_sequence(sequence_len_example))
