def calculate_min_nails_thread_len(nails_positions_input: list[int]) -> int:
    INFTY: int = 10 ** 6
    nails_positions: list[int] = sorted([-INFTY] + nails_positions_input)
    nails_count: int = len(nails_positions) - 1
    dp: list[int] = [0] * (nails_count + 1)
    dp[1] = INFTY
    dp[2] = nails_positions[2] - nails_positions[1]
    for nail_number in range(3, nails_count + 1):
        dp[nail_number] = min(dp[nail_number - 1], dp[nail_number - 2])
        dp[nail_number] += nails_positions[nail_number] - nails_positions[nail_number - 1]

    return dp[nails_count]


nail_count_example: int = int(input())
nails_positions_example: list[int] = list(map(int, input().split()))
min_nails_thread_len: int = calculate_min_nails_thread_len(nails_positions_example)
print(min_nails_thread_len)
