from collections import deque

wagons_count: int = int(input())
wagons_positions: list[int] = list(map(int, input().split()))

stack: deque[int] = deque([])

current_needed_wagon_number: int = 1
for wagon in wagons_positions:
    if wagon == current_needed_wagon_number:
        current_needed_wagon_number += 1
        while stack and stack[-1] == current_needed_wagon_number:
            stack.pop()
            current_needed_wagon_number += 1
    else:
        stack.append(wagon)
if stack:
    print("NO")
else:
    print("YES")
