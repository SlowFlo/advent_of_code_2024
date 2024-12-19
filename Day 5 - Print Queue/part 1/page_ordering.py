import re
import time


def get_dict_ordering_rules(ordering_rules: str) -> dict[int, tuple[int]]:
    if not isinstance(ordering_rules, str):
        raise TypeError("The rules must be a string")

    if not ordering_rules.strip():
        return {}

    dict_ordering_rules = {}
    for rule in ordering_rules.splitlines():
        if not (match := re.match(r"(\d{2})\|(\d{2})", rule)):
            raise ValueError(f"The rules must be of format XX|XX, got : {rule}")

        dict_ordering_rules[int(match.group(1))] = dict_ordering_rules.get(int(match.group(1)), ()) + (
            int(match.group(2)),
        )

    return dict_ordering_rules


def filter_correct_updates(updates: str, dict_ordering_rules: dict[int, tuple[int]]):
    if not isinstance(updates, str):
        raise TypeError("The rules must be a string")

    if not isinstance(dict_ordering_rules, dict):
        raise TypeError("The ordering rules must be a dict")


def get_correctly_ordered_updates(ordering_rules: str, updates: str):
    if not isinstance(ordering_rules, str):
        raise TypeError("The rules must be a string")

    if not isinstance(updates, str):
        raise TypeError("The updates must be a string")

    dict_ordering_rules = get_dict_ordering_rules(ordering_rules)

    return filter_correct_updates(updates, dict_ordering_rules)


def get_sum_middle_pages_of_correctly_ordered_updates(ordering_rules_and_updates: str) -> int:
    if not isinstance(ordering_rules_and_updates, str):
        raise TypeError("The rules and updates must be a string")

    ordering_rules, updates = ordering_rules_and_updates.split("\n\n")

    correctly_ordered_updates = get_correctly_ordered_updates(ordering_rules, updates)

    return 143


if __name__ == "__main__":
    start_time = time.time()
    with open("puzzle_input.txt") as f:
        letters_grid = f.read()
        print(
            "Sum of the correct updates middle pages numbers:",
            get_sum_middle_pages_of_correctly_ordered_updates(letters_grid),
        )

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time:.6f} seconds")
