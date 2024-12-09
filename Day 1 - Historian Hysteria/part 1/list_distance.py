from typing import Tuple


def get_location_ids_total_distance(location_ids: str) -> int:
    if not isinstance(location_ids, str):
        raise TypeError("The location IDs list is not a str")

    pairs = get_sorted_pairs(location_ids)

    raise NotImplementedError()

    return 11


def get_sorted_pairs(location_ids: str) -> tuple[tuple[int, int], ...]:
    if not isinstance(location_ids, str):
        raise TypeError("The location IDs list is not a str")

    entries = location_ids.splitlines()

    first_numbers = []
    second_numbers = []

    for entry in entries:
        first, second = map(int, entry.split())
        first_numbers.append(first)
        second_numbers.append(second)

    first_numbers.sort()
    second_numbers.sort()

    return tuple(zip(first_numbers, second_numbers))
