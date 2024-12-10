import pytest

from report_safety import get_nb_safe_reports, is_report_safe


def test_get_nb_safe_reports_reports_is_str():
    with pytest.raises(TypeError):
        get_nb_safe_reports(4.9)


def test_is_report_safe_report_is_str():
    with pytest.raises(TypeError):
        is_report_safe(1)


def test_report_gradually_decreasing_is_safe():
    report = "7 6 4 2 1"

    assert is_report_safe(report) == True


def test_report_gradually_increasing_is_safe():
    report = "1 3 6 7 9"

    assert is_report_safe(report) == True


def test_report_increase_more_than_3_is_unsafe():
    report = "1 2 7 8 9"

    assert is_report_safe(report) == False


def test_report_decrease_more_than_3_is_unsafe():
    report = "9 7 6 2 1"

    assert is_report_safe(report) == False


def test_both_increasing_and_decreasing_is_unsafe():
    report = "1 3 2 4 5"

    assert is_report_safe(report) == False


def test_neither_increasing_or_decreasing_is_unsafe():
    report = "8 6 4 4 1"

    assert is_report_safe(report) == False


def test_nb_safe_reports_is_correct():
    reports = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""

    nb_safe_reports = get_nb_safe_reports(reports)

    assert nb_safe_reports == 2


if __name__ == "__main__":
    pytest.main([__file__])
