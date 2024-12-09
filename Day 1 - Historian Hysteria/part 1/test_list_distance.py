import pytest

from list_distance import get_location_ids_total_distance


def test_location_ids_not_a_str_must_fail():
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
