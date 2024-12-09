def get_location_ids_total_distance(location_ids: str) -> int:
    if not isinstance(location_ids, str):
        raise TypeError("The location IDs list is not a str")

    pairs = get_sorted_pairs(location_ids)

    return sum(abs(pair[0] - pair[1]) for pair in pairs)


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


def get_ids_count_dict(location_ids: str):
    if not isinstance(location_ids, str):
        raise TypeError("The location IDs list is not a str")

    ids_count_dict = {"left list": {}, "right list": {}}

    entries = location_ids.splitlines()

    for entry in entries:
        left, right = map(int, entry.split())
        ids_count_dict["left list"][left] = ids_count_dict["left list"].get(left, 0) + 1
        ids_count_dict["right list"][right] = (
            ids_count_dict["right list"].get(right, 0) + 1
        )

    return ids_count_dict


def get_similarity_score(location_ids: str) -> int:
    if not isinstance(location_ids, str):
        raise TypeError("The location IDs list is not a str")

    ids_count = get_ids_count_dict(location_ids)

    return 31


if __name__ == "__main__":
    with open("puzzle_input.txt") as f:
        print(get_location_ids_total_distance(f.read()))
