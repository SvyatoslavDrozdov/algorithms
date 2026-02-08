def count_possible_ways(desk_size: int, max_jump_size: int) -> int:
    dp: list[int] = [0] * (desk_size + 1)
    dp[1] = 1
    for position in range(2, desk_size + 1):
        for possible_jump in range(1, min(max_jump_size + 1, desk_size)):
            dp[position] += dp[position - possible_jump]
    return dp[desk_size]


desk_size_example, max_jump_size_example = map(int, input().split())
print(count_possible_ways(desk_size_example, max_jump_size_example))
