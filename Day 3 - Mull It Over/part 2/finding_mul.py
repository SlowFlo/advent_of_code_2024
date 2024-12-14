import re
import time


def find_mul_in_substring(part_of_corrupted_memory: str) -> tuple[tuple[int, int], ...]:
    if not isinstance(part_of_corrupted_memory, str):
        raise TypeError("Corrupted_memory must be a string")

    if not part_of_corrupted_memory.strip():
        return ()

    valid_mul_pattern = r"mul\([0-9]{1,3},[0-9]{1,3}\)"

    matches = re.findall(valid_mul_pattern, part_of_corrupted_memory)

    result = [tuple(map(int, match[4:-1].split(","))) for match in matches]

    return tuple(result)


def find_valid_substrings(memory: str) -> list[str]:
    # We keep the instruction in the result with the regex group selector ()
    sections = re.split(r"(don't\(\)|do\(\))", memory)
    valid_substrings = []
    is_valid = True

    for section in sections:
        if section == "don't()":
            is_valid = False
        elif section == "do()":
            is_valid = True
        elif is_valid:
            valid_substrings.append(section)

    return valid_substrings


def find_all_mul(memory: str) -> tuple[tuple[int, int], ...]:
    valid_substrings = find_valid_substrings(memory)

    results = [mul for substring in valid_substrings for mul in find_mul_in_substring(substring)]

    return tuple(results)


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
        corrupted_memory = f.read()
        print("Sum of all mul operations:", find_and_apply_mul(corrupted_memory))

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time:.6f} seconds")
