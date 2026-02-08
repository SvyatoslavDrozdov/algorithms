def count_operations(number: int) -> list[int]:
    INFTY = 10 ** 6 + 1

    def get_min_and_idx(first_value: int, second_value: int, third_value: int) -> tuple[int, str]:
        if first_value <= second_value and first_value <= third_value:
            return first_value, "+"
        elif second_value <= first_value and second_value <= third_value:
            return second_value, "2"
        else:
            return third_value, "3"

    dp: list[int] = [0] * (number + 1)
    previous = [-1, -1]
    for value in range(2, number + 1):
        add_1: int = dp[value - 1] + 1
        multiply_by_2: int = dp[value // 2] + 1 if value % 2 == 0 else INFTY
        multiply_by_3: int = dp[value // 3] + 1 if value % 3 == 0 else INFTY
        best_value, operation_symbol = get_min_and_idx(add_1, multiply_by_2, multiply_by_3)
        dp[value] = best_value
        if operation_symbol == "+":
            previous_value = value - 1
        elif operation_symbol == "2":
            previous_value = value // 2
        elif operation_symbol == "3":
            previous_value = value // 3
        else:
            raise ValueError
        previous.append(previous_value)

    current: int = number
    transformation_history: list[int] = [current]
    for operation_idx in range(dp[number]):
        current = previous[current]
        transformation_history.append(current)
    return transformation_history[::-1]


number_example: int = int(input())
operations_data: list[int] = count_operations(number_example)
print(len(operations_data) - 1)
print(*operations_data)
