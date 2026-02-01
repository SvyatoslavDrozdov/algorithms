"""
Экзамен по бердянскому языку проходит в узкой и длинной аудитории. На экзамен пришло N студентов. Все они посажены в
ряд. Таким образом, позиция каждого человека задается координатой на оси Ox (эта ось ведет вдоль длинной аудитории).
Два человека могут разговаривать, если расстояние между ними меньше или равно D. Какое наименьшее количество типов
билетов должен подготовить преподаватель, чтобы никакие два студента с одинаковыми билетами не могли разговаривать?
Выведите способ раздачи преподавателем билетов.

В первую строчку выходного файла выведите количество вариантов, а во вторую, разделяя пробелами, номера вариантов
студентов в том порядке, в каком они перечислены во входном файле.
"""


def get_minimum_ticket_number(max_distance: int, students_positions: list[int]) -> int:
    """
    :param max_distance: Максимальное расстояние на котором два студента могут вести диалог.
    :param students_positions: Координаты студентов.
    :return: Минимальное количество типов билетов, не дающее студентам списывать друг с друга.
    """
    events: list[tuple[float, int]] = []
    EVENT_START: int = -1
    EVENT_END: int = 1
    EPS: float = 1e-6
    for position in students_positions:
        events.append((position - max_distance / 2 - EPS, EVENT_START))
        events.append((position + max_distance / 2 + EPS, EVENT_END))

    events.sort()
    current_interacting_count: int = 0
    max_interacting_count: int = 0
    for event in events:
        event_type: int = event[1]
        if event_type == EVENT_START:
            current_interacting_count += 1
        elif event_type == EVENT_END:
            current_interacting_count -= 1
        else:
            raise NotImplemented(f"Тип события {event_type} не определен.")

        if max_interacting_count < current_interacting_count:
            max_interacting_count = current_interacting_count

    return max_interacting_count


def give_tickets(students_positions: list[int], num_tickets_options: int) -> list[int]:
    """
    :param students_positions: Координаты студентов.
    :param num_tickets_options: Количество типов билетов
    :return: Номера билетов записанные для студентов в том же порядке, в котором записаны их позиции.
    """
    sorted_students: list[tuple[int, int]] = []
    for student_number, student_position in enumerate(students_positions):
        sorted_students.append((student_position, student_number))
    sorted_students.sort()

    tickets_distribution = [0] * len(students_positions)
    ticket_option = 0
    for student in sorted_students:
        ticket_option += 1
        if ticket_option == num_tickets_options + 1:
            ticket_option = 1

        student_number = student[1]
        tickets_distribution[student_number] = ticket_option

    return tickets_distribution


N, D = map(int, input().split())
X = list(map(int, input().split()))
tickets_options = get_minimum_ticket_number(D, X)
print(get_minimum_ticket_number(D, X))
print(*give_tickets(X, tickets_options))
