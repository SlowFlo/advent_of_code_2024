def get_dict_ordering_rules(ordering_rules: str):
    if not isinstance(ordering_rules, str):
        raise TypeError("The rules must be a string")


def get_correctly_ordered_updates(ordering_rules: str, updates: str):
    if not isinstance(ordering_rules, str):
        raise TypeError("The rules must be a string")

    if not isinstance(updates, str):
        raise TypeError("The updates must be a string")

    get_dict_ordering_rules(ordering_rules)


def get_sum_middle_pages_of_correctly_ordered_updates(ordering_rules_and_updates: str) -> int:
    if not isinstance(ordering_rules_and_updates, str):
        raise TypeError("The rules and updates must be a string")

    ordering_rules, updates = ordering_rules_and_updates.split("\n\n")

    correctly_ordered_updates = get_correctly_ordered_updates(ordering_rules, updates)

    return 143
