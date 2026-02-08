num_students_example: int = int(input())
num_test_options_example: int = int(input())
raw_number_example: int = int(input())
petya_has_right_position_example: int = int(input())


def find_vasya_position(num_students: int, num_test_options: int, petya_raw_number: int,
                        petya_has_right_position: int) -> list[int] | tuple[int, int]:
    petya_position: int = 2 * (petya_raw_number - 1) + petya_has_right_position

    def get_vasya_position(vasya_position: int):
        if vasya_position % 2 == 0:
            vasya_has_right_position: int = 2
            vasya_raw: int = vasya_position // 2
        else:
            vasya_has_right_position: int = 1
            vasya_raw: int = vasya_position // 2 + 1
        return vasya_raw, vasya_has_right_position

    dist_in_front: int = num_students
    if petya_position - num_test_options >= 1:
        vasya_position_in_front: int = petya_position - num_test_options
        vasya_position_in_front_raw, vasya_position_in_front_has_right_position = (
            get_vasya_position(vasya_position_in_front)
        )
        dist_in_front: int = abs(petya_raw_number - vasya_position_in_front_raw) - 1

    if petya_position + num_test_options <= num_students:
        vasya_position_behind: int = petya_position + num_test_options
        vasya_position_behind_raw, vasya_position_behind_has_right_position = get_vasya_position(vasya_position_behind)
        dist_behind: int = abs(petya_raw_number - vasya_position_behind_raw) - 1
        if dist_behind <= dist_in_front:
            return vasya_position_behind_raw, vasya_position_behind_has_right_position
        return vasya_position_in_front_raw, vasya_position_in_front_has_right_position

    if petya_position - num_test_options >= 1:
        return vasya_position_in_front_raw, vasya_position_in_front_has_right_position

    return [-1]


print(*find_vasya_position(num_students_example, num_test_options_example, raw_number_example,
                           petya_has_right_position_example))
