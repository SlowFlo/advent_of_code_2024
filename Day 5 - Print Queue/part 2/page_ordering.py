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


def sort_incorrect_updates(pages, dict_ordering_rules):
    def priority(val):
        visited = set()
        stack = [val]
        priorite_val = 0
        while stack:
            current = stack.pop()
            if current not in visited:
                visited.add(current)
                priorite_val += 1
                if current in dict_ordering_rules:
                    stack.extend(dict_ordering_rules[current])
        return priorite_val

    return sorted(pages, key=lambda x: (-priority(x), -x))


def filter_correct_and_incorrect_updates(
    updates: str, dict_ordering_rules: dict[int, tuple[int]]
) -> dict[str, list[tuple[int]]]:
    if not isinstance(updates, str):
        raise TypeError("The rules must be a string")

    if not isinstance(dict_ordering_rules, dict):
        raise TypeError("The ordering rules must be a dict")

    correct_and_incorrect_updates = {"correct": [], "incorrect": []}

    if not updates.strip():
        return correct_and_incorrect_updates

    for str_update in updates.splitlines():
        insert_key = "correct"
        update = tuple(map(int, str_update.split(",")))

        seen_pages = []
        for page_number in update:
            rules = dict_ordering_rules.get(page_number, ())
            if any(must_be_before_page in seen_pages for must_be_before_page in rules):
                insert_key = "incorrect"

            seen_pages.append(page_number)

        if insert_key == "incorrect":
            seen_pages = sort_incorrect_updates(seen_pages, dict_ordering_rules)

        correct_and_incorrect_updates[insert_key].append(tuple(seen_pages))

    return correct_and_incorrect_updates


def get_correctly_and_incorrectly_ordered_updates(ordering_rules: str, updates: str) -> dict[str, list[tuple[int]]]:
    if not isinstance(ordering_rules, str):
        raise TypeError("The rules must be a string")

    if not isinstance(updates, str):
        raise TypeError("The updates must be a string")

    dict_ordering_rules = get_dict_ordering_rules(ordering_rules)

    return filter_correct_and_incorrect_updates(updates, dict_ordering_rules)


def get_sum_middle_pages_of_correctly_and_incorrectly_ordered_updates(
    ordering_rules_and_updates: str,
) -> tuple[int, int]:
    if not isinstance(ordering_rules_and_updates, str):
        raise TypeError("The rules and updates must be a string")

    ordering_rules, updates = ordering_rules_and_updates.split("\n\n")

    updates = get_correctly_and_incorrectly_ordered_updates(ordering_rules, updates)

    correctly_ordered_sum = 0
    for correct_update in updates["correct"]:
        correctly_ordered_sum += correct_update[len(correct_update) // 2]

    incorrectly_ordered_sum = 0
    for incorrect_update in updates["incorrect"]:
        incorrectly_ordered_sum += incorrect_update[len(incorrect_update) // 2]

    return correctly_ordered_sum, incorrectly_ordered_sum


if __name__ == "__main__":
    start_time = time.time()
    with open("puzzle_input.txt") as f:
        letters_grid = f.read()
        correctly_ordered_sum, incorrectly_ordered_sum = (
            get_sum_middle_pages_of_correctly_and_incorrectly_ordered_updates(letters_grid)
        )

        print("Sum of the correct updates middle pages numbers:", correctly_ordered_sum)
        print("Sum of the incorrect updates middle pages numbers:", incorrectly_ordered_sum)

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time:.6f} seconds")
