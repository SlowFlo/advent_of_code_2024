def get_location_ids_total_distance(location_ids: str) -> int:
    if not isinstance(location_ids, str):
        raise TypeError("The location IDs list is not a str")

    pairs = get_sorted_pairs(location_ids)

    raise NotImplementedError()

    return 11


def get_sorted_pairs(location_ids: str):
    if not isinstance(location_ids, str):
        raise TypeError("The location IDs list is not a str")
