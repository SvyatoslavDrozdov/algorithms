def calculate_matrix_prefix_sum(matrix: list[list[int]]) -> list[list[int]]:
    matrix_height: int = len(matrix)
    matrix_width: int = len(matrix[0])

    matrix_prefix_sum: list[list[int]] = [[0] * (matrix_width + 1) for _ in range(matrix_height + 1)]

    row_prefix_sum: list[list[int]] = [[0] * (matrix_width + 1) for _ in range(matrix_height + 1)]
    for row_number in range(matrix_height):
        for column_number in range(matrix_width):
            row_prefix_sum[row_number + 1][column_number + 1] += (
                    row_prefix_sum[row_number + 1][column_number] + matrix[row_number][column_number]
            )

    for row_number in range(1, matrix_height + 1):
        for column_number in range(1, matrix_width + 1):
            matrix_prefix_sum[row_number][column_number] = (
                    matrix_prefix_sum[row_number - 1][column_number] + row_prefix_sum[row_number][column_number]
            )

    return matrix_prefix_sum


matrix_height_example, matrix_width_example, query_count = map(int, input().split())
matrix_example: list[list[int]] = []

for _ in range(matrix_height_example):
    matrix_example.append(list(map(int, input().split())))

matrix_prefix_sum_example: list[list[int]] = calculate_matrix_prefix_sum(matrix_example)

for _ in range(query_count):
    x_start, y_start, x_end, y_end = map(int, input().split())
    sum_of_elements: int = (matrix_prefix_sum_example[x_end][y_end] - matrix_prefix_sum_example[x_start - 1][y_end] -
                            matrix_prefix_sum_example[x_end][y_start - 1] +
                            matrix_prefix_sum_example[x_start - 1][y_start - 1]
                            )
    print(sum_of_elements)
