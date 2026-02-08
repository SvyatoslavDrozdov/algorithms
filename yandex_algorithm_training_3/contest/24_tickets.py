def find_best_time(customers_data: list[list[int]]):
    customers_count = len(customers_data) - 1
    dp = [0] * (customers_count + 1)

    if customers_count == 1:
        return customers_data[1][0]
    if customers_count == 2:
        A_1 = customers_data[1][0]
        B_1 = customers_data[1][1]
        A_2 = customers_data[2][0]
        return min(A_1 + A_2, B_1)

    A_1 = customers_data[1][0]
    B_1 = customers_data[1][1]
    C_1 = customers_data[1][2]
    A_2 = customers_data[2][0]
    B_2 = customers_data[2][1]
    A_3 = customers_data[3][0]

    dp[1] = A_1
    dp[2] = min(A_1 + A_2, B_1)
    dp[3] = min(A_1 + A_2 + A_3, B_1 + A_3, A_1 + B_2, C_1)

    for client_number in range(4, customers_count + 1):
        A_n = customers_data[client_number][0]
        B_n_1 = customers_data[client_number - 1][1]
        C_n_2 = customers_data[client_number - 2][2]
        dp[client_number] = min(dp[client_number - 1] + A_n, dp[client_number - 2] + B_n_1,
                                dp[client_number - 3] + C_n_2)

    return dp[customers_count]


customers_count_input: int = int(input())
data: list[list[int]] = [[]]
for _ in range(customers_count_input):
    data.append(list(map(int, input().split())))

print(find_best_time(data))