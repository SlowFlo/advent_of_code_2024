import pytest

from report_safety import get_nb_safe_reports, is_problem_dampened_report_safe


def test_get_nb_safe_reports_reports_is_str():
    with pytest.raises(TypeError):
        get_nb_safe_reports(4.9)


def test_is_report_safe_report_is_str():
    with pytest.raises(TypeError):
        is_problem_dampened_report_safe(1)


def test_report_gradually_decreasing_is_safe():
    report = "7 6 4 2 1"

    assert is_problem_dampened_report_safe(report) == True


def test_report_gradually_increasing_is_safe():
    report = "1 3 6 7 9"

    assert is_problem_dampened_report_safe(report) == True


def test_report_increase_more_than_3_is_unsafe():
    report = "1 2 7 8 9"

    assert is_problem_dampened_report_safe(report) == False


def test_report_decrease_more_than_3_is_unsafe():
    report = "9 7 6 2 1"

    assert is_problem_dampened_report_safe(report) == False


def test_both_increasing_and_decreasing_is_unsafe():
    report = "1 3 2 4 2"

    assert is_problem_dampened_report_safe(report) == False


def test_report_become_safe_by_removing_a_decreasing_level():
    # become safe if 3 is removed
    report = "1 3 2 4 5"

    assert is_problem_dampened_report_safe(report) == True


def test_report_become_safe_by_removing_the_first_level():
    report = "5 1 2 3 4 5"

    assert is_problem_dampened_report_safe(report) == True


def test_neither_increasing_or_decreasing_is_unsafe():
    report = "8 6 4 4 4 1"

    assert is_problem_dampened_report_safe(report) == False


def test_report_become_safe_by_removing_a_level_of_same_value():
    report = "8 6 4 4 1"

    assert is_problem_dampened_report_safe(report) == True


def test_nb_safe_reports_is_correct():
    reports = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""

    nb_safe_reports = get_nb_safe_reports(reports)

    assert nb_safe_reports == 4


def test_edge_cases_are_correct():
    reports = """48 46 47 49 51 54 56
1 1 2 3 4 5
1 2 3 4 5 5
5 1 2 3 4 5
1 4 3 2 1
1 6 7 8 9
1 2 3 4 3
9 8 7 6 7
7 10 8 10 11
29 28 27 25 26 25 22 20"""

    nb_safe_reports = get_nb_safe_reports(reports)

    assert nb_safe_reports == 10


if __name__ == "__main__":
    pytest.main([__file__])
