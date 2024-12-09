import pytest

from list_distance import (
    get_location_ids_total_distance,
    get_sorted_pairs,
    get_similarity_score,
    get_ids_count_dict,
)


def test_get_sorted_pairs_input_must_be_a_str():
    with pytest.raises(TypeError):
        get_sorted_pairs(2)


def test_get_sorted_pairs_returns_correct_pairs():
    location_ids = """3   4
4   3
2   5
1   3
3   9
3   3"""

    pairs = get_sorted_pairs(location_ids)

    assert pairs == ((1, 3), (2, 3), (3, 3), (3, 4), (3, 5), (4, 9))


def test_total_distance_location_ids_must_be_a_str():
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


def test_ids_count_dict_location_ids_must_be_a_str():
    with pytest.raises(TypeError):
        get_ids_count_dict(45)

def test_ids_count_is_correct():
    location_ids = """3   4
    4   3
    2   5
    1   3
    3   9
    3   3"""

    ids_count = get_ids_count_dict(location_ids)

    assert ids_count == {
        "left list": {1: 1, 2: 1, 3: 3, 4: 1},
        "right list": {3: 3, 4: 1, 5: 1, 9: 1},
    }


def test_similarity_score_location_ids_must_be_a_str():
    with pytest.raises(TypeError):
        get_similarity_score(3.2)


def test_similarity_score_is_correct():
    location_ids = """3   4
4   3
2   5
1   3
3   9
3   3"""

    similarity_score = get_similarity_score(location_ids)

    assert similarity_score == 31


if __name__ == "__main__":
    pytest.main([__file__])
