import pytest

from xmas_search import find_number_of_xmas


def test_find_number_of_xmas_input_grid_is_str():
    with pytest.raises(TypeError):
        find_number_of_xmas(45)


def test_empty_str_no_xmas():
    assert find_number_of_xmas("") == 0


def test_1_line_no_xmas():
    assert find_number_of_xmas("AZERTY") == 0


def test_1_line_with_1_xmas():
    assert find_number_of_xmas("XMAS") == 1


def test_1_line_with_2_xmas():
    assert find_number_of_xmas("ZQDQZXMASerzQDZXMASZQD") == 2


def test_1_line_with_1_reversed_xmas():
    assert find_number_of_xmas("SAMX") == 1


def test_1_line_with_2_reversed_xmas():
    assert find_number_of_xmas("DZSAMX45GUVSAMXTCTC") == 2


def test_1_line_with_both_normal_and_reversed_xmas():
    assert find_number_of_xmas("DZXMAS45GUVSAMXTCTC") == 2


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
