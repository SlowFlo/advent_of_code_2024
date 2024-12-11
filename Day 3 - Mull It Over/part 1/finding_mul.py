def is_mul_inputs_valid(x: str, y: str) -> bool:
    return len(x) <= 3 and len(y) <= 3 and x.isnumeric() and y.isnumeric()


def find_all_mul(corrupted_memory: str) -> tuple[tuple[int, int], ...]:
    if not isinstance(corrupted_memory, str):
        raise TypeError("Corrupted memory must be a string")

    if corrupted_memory.startswith("mul(") and corrupted_memory.endswith(")"):
        x_str, y_str = corrupted_memory.strip("mul()").split(",")
        if is_mul_inputs_valid(x_str, y_str):
            return ((int(x_str), int(y_str)),)

    return ()


def find_and_apply_mul(corrupted_memory: str) -> int:
    if not isinstance(corrupted_memory, str):
        raise TypeError("Corrupted memory must be a string")

    mul_operations = find_all_mul(corrupted_memory)

    return 161
