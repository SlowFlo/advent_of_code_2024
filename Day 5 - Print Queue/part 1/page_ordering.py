def get_sum_middle_pages_of_correctly_ordered_updates(ordering_rules_and_updates: str):
    if not isinstance(ordering_rules_and_updates, str):
        raise TypeError("The rules and updates must be a string")
