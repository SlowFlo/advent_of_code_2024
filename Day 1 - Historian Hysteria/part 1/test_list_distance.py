import pytest

from list_distance import get_location_ids_total_distance, get_sorted_pairs


def test_get_sorted_pairs_input_must_be_a_str():
    with pytest.raises(TypeError):
        get_sorted_pairs(45)


def test_location_ids_must_be_a_str():
    with pytest.raises(TypeError):
        get_location_ids_total_distance(45)


def test_distance_total_is_correct():
    location_ids = """3   4
4   3
2   5
1   3
3   9
3   3"""

    total_distance = get_location_ids_total_distance(location_ids)

    assert total_distance == 11


def test_distance_total_of_one_line_is_correct():
    location_ids = "4   9"

    total_distance = get_location_ids_total_distance(location_ids)

    assert total_distance == 5
