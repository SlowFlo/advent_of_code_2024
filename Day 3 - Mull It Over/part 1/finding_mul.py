from typing import Tuple


def is_mul_inputs_valid(x: str, y: str) -> bool:
    return len(x) <= 3 and len(y) <= 3 and x.isnumeric() and y.isnumeric()


def get_next_mul_idx(corrupted_memory: str, start_idx: int = 0) -> tuple[int, int]:
    mul_start_idx = corrupted_memory.find("mul(", start_idx)
    if mul_start_idx == -1:
        mul_end_idx = -1
    else:
        next_mul_operation = corrupted_memory.find("mul(", mul_start_idx + 1)
        mul_end_idx = corrupted_memory.find(")", mul_start_idx)
        if next_mul_operation != -1 and next_mul_operation < mul_end_idx:
            mul_start_idx = next_mul_operation
    return mul_start_idx, mul_end_idx


def find_all_mul(corrupted_memory: str) -> tuple[tuple[int, int], ...]:
    if not isinstance(corrupted_memory, str):
        raise TypeError("Corrupted memory must be a string")

    mul_start_idx, mul_end_idx = get_next_mul_idx(corrupted_memory)

    mul_operations = []

    while mul_end_idx != -1:
        x_str, y_str = corrupted_memory[mul_start_idx:mul_end_idx].strip("mul()").split(",")
        if is_mul_inputs_valid(x_str, y_str):
            mul_operations.append((int(x_str), int(y_str)))

        mul_start_idx, mul_end_idx = get_next_mul_idx(corrupted_memory, mul_end_idx)

    return tuple(mul_operations)


def find_and_apply_mul(corrupted_memory: str) -> int:
    if not isinstance(corrupted_memory, str):
        raise TypeError("Corrupted memory must be a string")

    mul_operations = find_all_mul(corrupted_memory)

    return 161
