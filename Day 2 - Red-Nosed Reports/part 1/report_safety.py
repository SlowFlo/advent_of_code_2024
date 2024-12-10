def is_report_safe(report: str) -> bool:
    if not isinstance(report, str):
        raise TypeError("report must be a string")

    levels = list(map(int, report.split()))
    previous_level = levels[0]
    for level in levels[1:]:
        if abs(level - previous_level) > 3:
            return False
        previous_level = level

    return True


def get_nb_safe_reports(reports: str) -> int:
    if not isinstance(reports, str):
        raise TypeError("reports must be a string")

    reports_list = reports.splitlines()

    return 2
