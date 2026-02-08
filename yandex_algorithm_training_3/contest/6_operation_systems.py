def count_installed_systems(operation_systems_positions: list[tuple[int, int]]) -> int:
    current_operation_systems: dict[int, tuple[int, int]] = {}

    for idx, operation_system in enumerate(operation_systems_positions):
        start: int = operation_system[0]
        end: int = operation_system[1]
        idx_to_delete: list[int] = []
        for installed_op_sys_idx, installed_operation_system in current_operation_systems.items():
            installed_start: int = installed_operation_system[0]
            installed_end: int = installed_operation_system[1]
            if not (end < installed_start or installed_end < start):
                idx_to_delete.append(installed_op_sys_idx)
        for delete_idx in idx_to_delete:
            del current_operation_systems[delete_idx]

        current_operation_systems[idx] = operation_system

    return len(current_operation_systems)


sectors_count_example: int = int(input())
sections_count_example: int = int(input())

operation_systems_positions_example: list[tuple[int, int]] = []
for _ in range(sections_count_example):
    input_data: tuple[int, ...] = tuple(map(int, input().split()))
    system_position: tuple[int, int] = (input_data[0], input_data[1])
    operation_systems_positions_example.append(system_position)

print(count_installed_systems(operation_systems_positions_example))
