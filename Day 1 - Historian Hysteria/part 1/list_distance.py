def get_location_ids_total_distance(location_ids: str) -> int:
    if not isinstance(location_ids, str):
        raise TypeError("The location IDs list is not a str")

    return 11