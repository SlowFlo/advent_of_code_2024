import pytest

from xmas_search import find_number_of_xmas


def test_find_number_of_xmas_input_grid_is_str():
    with pytest.raises(TypeError):
        find_number_of_xmas(45)


def test_find_number_of_xmas_use_case_is_ok():
    letters_grid = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""

    assert find_number_of_xmas(letters_grid) == 18


if __name__ == "__main__":
    pytest.main([__file__])
