"""
Рассмотрим задачу: клиенты приходят и уходят с сайта в моменты времени [t_i_start, t_i_end].
Требуется найти сколько времени на сайте были хотя бы min_number человек.
"""


def calculate_time_under_load(min_number: int, people_data: list[tuple[float, float]]) -> float:
    """
    :param min_number: минимальное число людей на сайте, при котором считается время его работы
    :param people_data: список кортежей (время прихода человека, время ухода человека)
    :return: время работы сайта, когда на нем не менее, чем min_number человек.
    """
    EVENT_START: int = -1
    EVENT_END: int = 1

    events: list[tuple[float, int]] = []
    for come_time, leave_time in people_data:
        events.append((come_time, EVENT_START))
        events.append((leave_time, EVENT_END))
    events.sort()

    current_online: int = 0
    time_above_threshold: float = 0.0

    for event_idx in range(len(events)):
        if current_online >= min_number:
            time_above_threshold += events[event_idx][0] - events[event_idx - 1][0]

        if events[event_idx][1] == EVENT_START:
            current_online += 1
        elif events[event_idx][1] == EVENT_END:
            current_online -= 1
        else:
            raise NotImplemented(f"Код не предполагает типа события {events[event_idx][0]}.")

    return time_above_threshold


data_ex = [(0, 1), (1, 4), (2, 5)]
min_number_ex = 2
time_under_load = calculate_time_under_load(min_number_ex, data_ex)
print(f"время работы под нагрузкой: {time_under_load}")
