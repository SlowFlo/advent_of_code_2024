import pytest

from page_ordering import get_sum_middle_pages_of_correctly_ordered_updates


def test_get_sum_middle_pages_of_correctly_ordered_updates_input_is_str():
    with pytest.raises(TypeError):
        get_sum_middle_pages_of_correctly_ordered_updates(45)


if __name__ == "__main__":
    pytest.main([__file__])
