def test_distance_total_is_correct():
    location_ids = """3   4
4   3
2   5
1   3
3   9
3   3"""

    total_distance = get_location_ids_total_distance(location_ids)

    assert total_distance == 11
