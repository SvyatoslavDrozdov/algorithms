def count_operations(number: int) -> tuple[int, str]:
    INFTY = 10 ** 6 + 1

    dp_add_1: list[int] = [0] * (number + 1)
    dp_x2: list[int] = [0] * (number + 1)
    dp_x3: list[int] = [0] * (number + 1)

    dp_add_1[1] = 0
    dp_add_1[2] = 1

    dp_x2[1] = INFTY
    dp_x2[2] = 1

    dp_x3[1] = INFTY
    dp_x3[2] = INFTY

    last_add_1_operation_history: list[str] = ["", "", "+"]
    last_x2_operation_history: list[str] = ["", "", "2"]
    last_x3_operation_history: list[str] = ["", "", ""]
    history = [last_add_1_operation_history, last_x2_operation_history, last_x3_operation_history]

    def get_min_and_idx(first_value: int, second_value: int, third_value: int) -> tuple[int, int]:
        if first_value <= second_value and first_value <= third_value:
            return first_value, 0
        elif second_value <= first_value and second_value <= third_value:
            return second_value, 1
        else:
            return third_value, 2

    for value in range(3, number + 1):
        add_data: tuple[int, int] = get_min_and_idx(dp_add_1[value - 1], dp_x2[value - 1], dp_x3[value - 1])
        dp_add_1[value] = add_data[0] + 1
        last_add_1_operation_history.append(history[add_data[1]][value - 1] + "+")
        if value % 2 != 0:
            dp_x2[value] = INFTY
            last_x2_operation_history.append("")
        else:
            x2_data: tuple[int, int] = get_min_and_idx(dp_add_1[value // 2], dp_x2[value // 2], dp_x3[value // 2])
            dp_x2[value] = x2_data[0] + 1
            last_x2_operation_history.append(history[add_data[1]][value // 2] + "2")
        if value % 3 != 0:
            dp_x3[value] = INFTY
            last_x3_operation_history.append("")
        else:
            x3_data: tuple[int, int] = get_min_and_idx(dp_add_1[value // 3], dp_x2[value // 3], dp_x3[value // 3])
            dp_x3[value] = x3_data[0] + 1
            last_x3_operation_history.append(history[add_data[1]][value // 3] + "3")

    data = get_min_and_idx(dp_add_1[number], dp_x2[number], dp_x3[number])
    min_number_of_operations: int = data[0]
    best_history: str = history[data[1]][number]
    return min_number_of_operations, best_history


number_example: int = int(input())
operations_data: tuple[int, str] = count_operations(number_example)
min_operations_count: int = operations_data[0]
number_transform: list[int] = [1]
current_value: int = 1
for operation in operations_data[1]:
    if operation == "+":
        current_value += 1
    elif operation == "2":
        current_value *= 2
    elif operation == "3":
        current_value *= 3
    else:
        raise ValueError
    number_transform.append(current_value)
print(min_operations_count)
print(*number_transform)
