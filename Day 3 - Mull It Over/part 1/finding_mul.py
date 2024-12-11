def is_mul_inputs_valid(x: str, y: str) -> bool:
    return len(x) <= 3 and len(y) <= 3 and x.isnumeric() and y.isnumeric()


def find_all_mul(corrupted_memory: str) -> tuple[tuple[int, int], ...]:
    if not isinstance(corrupted_memory, str):
        raise TypeError("Corrupted memory must be a string")

    mul_operation_start_idx = corrupted_memory.find("mul(")
    if mul_operation_start_idx == -1:
        mul_operation_end_idx = -1
    else:
        mul_operation_end_idx = corrupted_memory.find(")", mul_operation_start_idx)

    mul_operations = []

    while mul_operation_end_idx != -1:
        x_str, y_str = corrupted_memory[mul_operation_start_idx:mul_operation_end_idx].strip("mul()").split(",")
        if is_mul_inputs_valid(x_str, y_str):
            mul_operations.append((int(x_str), int(y_str)))

        mul_operation_start_idx = corrupted_memory.find("mul(", mul_operation_end_idx)
        if mul_operation_start_idx == -1:
            mul_operation_end_idx = -1
        else:
            mul_operation_end_idx = corrupted_memory.find(")", mul_operation_start_idx)

    return tuple(mul_operations)


def find_and_apply_mul(corrupted_memory: str) -> int:
    if not isinstance(corrupted_memory, str):
        raise TypeError("Corrupted memory must be a string")

    mul_operations = find_all_mul(corrupted_memory)

    return 161
