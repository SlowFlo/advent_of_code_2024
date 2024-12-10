import pytest

from report_safety import get_nb_safe_reports


def test_get_nb_safe_reports_reports_is_str():
    with pytest.raises(TypeError):
        get_nb_safe_reports(4.9)


def test_nb_safe_reports_is_correct():
    reports = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""

    nb_safe_reports = get_nb_safe_reports(reports)

    assert nb_safe_reports == 2
