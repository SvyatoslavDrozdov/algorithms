from collections import deque

chess_height, chess_width, feeder_x_coord, feeder_y_coord, fleas_count = map(int, input().split())
fleas_positions: list[tuple[int, ...]] = []
for _ in range(fleas_count):
    fleas_positions.append(tuple(map(int, input().split())))

adjacency_list: dict[tuple[int, int], list[tuple[int, int]]] = {}

x_step: list[int] = [-2, -2, -1, -1, 1, 1, 2, 2]
y_step: list[int] = [-1, 1, -2, 2, -2, 2, -1, 1]
for x_position in range(1, chess_width + 1):
    for y_position in range(1, chess_height + 1):
        available_positions: list[tuple[int, int]] = []

        for next_x_step, next_y_step in zip(x_step, y_step):
            next_x = x_position + next_x_step
            next_y = y_position + next_y_step
            if 1 <= next_x <= chess_width and 1 <= next_y <= chess_height:
                available_positions.append((next_x, next_y))

        adjacency_list[(x_position, y_position)] = available_positions.copy()

visited: set = {(feeder_x_coord, feeder_y_coord)}
stack: deque[tuple[int, int]] = deque()
stack.append((feeder_x_coord, feeder_y_coord))
way_length: list[list[int]] = [[-1] * (chess_width + 1) for _ in range(chess_height + 1)]

way_length[feeder_x_coord][feeder_y_coord] = 0

while stack:
    from_cell: tuple[int, int] = stack.popleft()
    for to_cell in adjacency_list[from_cell]:
        if to_cell not in visited:
            visited.add(to_cell)
            way_length[to_cell[0]][to_cell[1]] = way_length[from_cell[0]][from_cell[1]] + 1
            stack.append(to_cell)

all_ways_are_possible: bool = True
sum_ways_length: int = 0
for flea_x_position, flea_y_position in fleas_positions:
    current_way_length: int = way_length[flea_x_position][flea_y_position]
    if current_way_length == -1:
        print(-1)
        all_ways_are_possible = False
        break
    sum_ways_length += current_way_length

if all_ways_are_possible:
    print(sum_ways_length)
