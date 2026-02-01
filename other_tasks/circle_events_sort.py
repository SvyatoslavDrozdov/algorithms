"""
На вход подаются данные об открытии и закрытии ларьков [(open_time_1, close_time_1), (open-time_2, close_time_2), ...]
отвечающие времени открытия и закрытия ларьков. Время это вещественно число от 0 до 24. Требуется определить максимальное
количество одновременно открытых ларьков и время, в течении которого был открыт хотя бы один ларек.
"""


def calculate_stall_statistics(data: list[tuple[float, float]]) -> tuple[float, int]:
    """
    :param data: данные об открытии и закрытии касс [(open_time_1, close_time_1), (open-time_2, close_time_2), ...].
    :return: максимальное количество одновременно открытых касс.
    """

    EVENT_OPEN: int = -1
    EVENT_CLOSE: int = 1

    events: list[tuple[float, int, int]] = []
    stall_number = 1
    for open_time, close_time in data:
        events.append((open_time, EVENT_OPEN, stall_number))
        events.append((close_time, EVENT_CLOSE, stall_number))
        stall_number += 1
    events.sort()

    opened_stall_set: set = set()
    working_time: float = 0
    current_open: int = 0
    max_open: int = 0

    for bypass in range(1, 3):
        bypass_calculated_time: float = working_time
        for event_idx in range(len(events)):
            current_event = events[event_idx]
            current_event_time = current_event[0]
            current_event_type = current_event[1]
            current_stall_number = current_event[2]

            if current_open >= 1:
                previous_event = events[event_idx - 1]
                previous_event_time = previous_event[0]
                time_to_add = current_event_time - previous_event_time
                if time_to_add < 0:
                    time_to_add = current_event_time + 24 - previous_event_time
                working_time += time_to_add

            if current_event_type == EVENT_OPEN:
                current_open += 1
                opened_stall_set.add(current_stall_number)
            elif current_event_type == EVENT_CLOSE and current_stall_number in opened_stall_set:
                current_open -= 1
                opened_stall_set.remove(current_stall_number)
            elif current_event_type != EVENT_OPEN and current_event_type != EVENT_CLOSE:
                raise NotImplemented(f"Код не предполагает типа события {current_event[0]}.")

            if max_open < current_open:
                max_open = current_open
        working_time = working_time - bypass_calculated_time

    return working_time, max_open


tests = [
    ([(9, 12), (10, 14), (13, 15)], (6.0, 2)),

    ([(21, 3), (22, 5), (0, 6)], (9, 3)),

    ([(21, 3), (0, 6), (9, 12), (12, 15), (12, 18), (18, 7)], (22, 3)),

    ([(0, 24), (1, 23)], (24.0, 2)),

    ([(23, 2)], (3.0, 1)),

    ([(3, 1)], (22, 1)),

    ([(20, 5), (21, 6), (22, 7), (0, 3)], (11, 4)),

    ([(21, 1), (23, 3)], (6, 2)),

    ([(3, 1), (4, 2)], (23, 2)),

    ([(22, 1), (23, 2), (0, 3)], (5, 3)),

    ([(23, 3.5), (0.5, 4)], (5, 2)),

    ([(20, 2), (6, 12), (18, 1)], (14 ,2))
]

for stalls, expected in tests:
    result = calculate_stall_statistics(stalls)
    print(f"{stalls} → {result}", end=" ")

    print("OK" if result == expected else f"Ожидалось {expected}")
