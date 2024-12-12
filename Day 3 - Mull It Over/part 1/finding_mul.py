import re
import time


def find_all_mul(corrupted_memory: str) -> tuple[tuple[int, int], ...]:
    if not isinstance(corrupted_memory, str):
        raise TypeError("Corrupted_memory must be a string")

    if not corrupted_memory.strip():
        return ()

    valid_mul_pattern = r"mul\([0-9]{1,3},[0-9]{1,3}\)"

    matches = re.findall(valid_mul_pattern, corrupted_memory)

    result = [tuple(map(int, match[4:-1].split(","))) for match in matches]

    return tuple(result)


def find_and_apply_mul(corrupted_memory: str) -> int:
    if not isinstance(corrupted_memory, str):
        raise TypeError("Corrupted memory must be a string")

    mul_operations = find_all_mul(corrupted_memory)

    total = 0
    for mul in mul_operations:
        total += mul[0] * mul[1]

    return total


if __name__ == "__main__":
    start_time = time.time()
    with open("puzzle_input.txt") as f:
        reports = f.read()
        print("Sum of all mul operations:", find_and_apply_mul(reports))

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time:.6f} seconds")
