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


def find_all_mul(memory: str) -> tuple[tuple[int, int], ...]:
    """
    Trouve toutes les instructions valides `mul(...)` dans une chaîne.
    - Les sections avant `don't()` sont analysées.
    - Les sections après un `do()` sont analysées.
    - Les sections entre un `do()` et un `don't()` sont analysées.
    """
    if not isinstance(memory, str):
        raise TypeError("Memory must be a string")

    # Trouver toutes les instructions `do()` et `don't()` et leurs positions
    sections = re.split(r"(don't\(\)|do\(\))", memory)

    valid_substrings = []
    is_valid = True  # Indique si la section actuelle est valide

    for section in sections:
        if section == "don't()":
            is_valid = False  # Désactiver l'analyse après un `don't()`
        elif section == "do()":
            is_valid = True  # Réactiver l'analyse après un `do()`
        elif is_valid:
            valid_substrings.append(section)  # Ajouter la partie valide pour analyse

    # Analyser chaque sous-chaîne valide avec la fonction donnée
    results = []
    for substring in valid_substrings:
        results.extend(find_mul_in_substring(substring))

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
        reports = f.read()
        print("Sum of all mul operations:", find_and_apply_mul(reports))

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time:.6f} seconds")
