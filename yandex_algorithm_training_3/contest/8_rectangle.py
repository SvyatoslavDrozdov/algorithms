cell_count: int = int(input())

points_coordinates: list[tuple[int, int]] = []
for _ in range(cell_count):
    x_coordinate: int
    y_coordinate: int
    x_coordinate, y_coordinate = map(int, input().split())
    points_coordinates.append((x_coordinate, y_coordinate))

MAX_NUMBER: int = 10 ** 9
min_x_coordinate: int = MAX_NUMBER
min_y_coordinate: int = MAX_NUMBER
max_x_coordinate: int = -MAX_NUMBER
max_y_coordinate: int = -MAX_NUMBER

for x_coordinate, y_coordinate in points_coordinates:
    if min_x_coordinate > x_coordinate:
        min_x_coordinate = x_coordinate
    if min_y_coordinate > y_coordinate:
        min_y_coordinate = y_coordinate
    if max_x_coordinate < x_coordinate:
        max_x_coordinate = x_coordinate
    if max_y_coordinate < y_coordinate:
        max_y_coordinate = y_coordinate

print(min_x_coordinate, min_y_coordinate, max_x_coordinate, max_y_coordinate)
