import pytest

from xmas_search import find_number_of_xmas


def test_find_number_of_xmas_input_grid_is_str():
    with pytest.raises(TypeError):
        find_number_of_xmas(45)


if __name__ == "__main__":
    pytest.main([__file__])
