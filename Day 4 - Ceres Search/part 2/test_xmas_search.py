import pytest

from xmas_search import find_number_of_x_mas


def test_find_number_of_x_mas_input_grid_is_str():
    with pytest.raises(TypeError):
        find_number_of_x_mas(45)


def test_empty_str_no_x_mas():
    assert find_number_of_x_mas("") == 0


def test_1_line_no_x_mas():
    assert find_number_of_x_mas("AZERTY") == 0


def test_1_x_mas():
    column = """M.S
.A.
M.S"""

    assert find_number_of_x_mas(column) == 1


def test_find_number_of_x_mas_use_case_is_ok():
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

    assert find_number_of_x_mas(letters_grid) == 9


if __name__ == "__main__":
    pytest.main([__file__])
