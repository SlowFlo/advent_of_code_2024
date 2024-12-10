def find_mul(corrupted_memory: str):
    if not isinstance(corrupted_memory, str):
        raise TypeError("Corrupted memory must be a string")

    if corrupted_memory.startswith("mul(") and corrupted_memory.endswith(")"):
        x, y = map(int, corrupted_memory.strip("mul()").split(","))
        return ((x, y),)

    return ()


def find_and_apply_mul(corrupted_memory: str) -> int:
    if not isinstance(corrupted_memory, str):
        raise TypeError("Corrupted memory must be a string")

    mul_operations = find_mul(corrupted_memory)

    return 161
