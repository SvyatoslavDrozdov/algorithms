def calculate_max_wellness_of_string(alphabet_size: int, letters_count_input: list[int]) -> int:
    letters_count: list[int] = letters_count_input.copy()
    sorted_letters_count: list[int] = list(set(letters_count))
    sorted_letters_count.sort()

    information_matrix: list[list[int]] = []
    layer_high_list: list[int] = []

    previous_high: int = 0
    for high in sorted_letters_count:
        layer_high: int = high - previous_high
        layer_high_list.append(layer_high)
        previous_high = high

        layer_information_matrix_raw: list[int] = []
        for idx in range(alphabet_size):
            if letters_count[idx] > 0:
                layer_information_matrix_raw.append(1)
            else:
                layer_information_matrix_raw.append(0)
        information_matrix.append(layer_information_matrix_raw)

        for idx in range(alphabet_size):
            letters_count[idx] -= layer_high

    wellness: int = 0

    for idx in range(len(information_matrix)):
        units_in_raw: int = 0
        for number in information_matrix[idx]:
            if number:
                units_in_raw += 1
            else:
                if units_in_raw >= 1:
                    wellness += layer_high_list[idx] * (units_in_raw - 1)
                units_in_raw = 0
        if units_in_raw >= 1:
            wellness += layer_high_list[idx] * (units_in_raw - 1)

    return wellness


def calculate_max_wellness_of_string_fast(alphabet_size: int, letters_count_input: list[int]) -> int:
    letters_count: list[int] = letters_count_input.copy()
    wellness: int = 0
    for idx in range(alphabet_size - 1):
        wellness += min(letters_count[idx + 1], letters_count[idx])
    return wellness


alphabet_size_example: int = int(input())
letters_count_example: list[int] = []
for _ in range(alphabet_size_example):
    letters_count_example.append(int(input()))
# print(calculate_max_wellness_of_string(alphabet_size_example, letters_count_example))
print(calculate_max_wellness_of_string_fast(alphabet_size_example, letters_count_example))