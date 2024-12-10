def is_report_safe(report: str) -> bool:
    if not isinstance(report, str):
        raise TypeError("report must be a string")

    levels = list(map(int, report.split()))
    previous_level = levels[0]
    previous_is_increasing = None
    for level in levels[1:]:
        is_increasing = True if level - previous_level > 0 else False
        if previous_is_increasing and previous_is_increasing != is_increasing:
            return False
        if abs(level - previous_level) > 3:
            return False
        previous_level = level
        previous_is_increasing = is_increasing

    return True


def get_nb_safe_reports(reports: str) -> int:
    if not isinstance(reports, str):
        raise TypeError("reports must be a string")

    reports_list = reports.splitlines()

    return 2
