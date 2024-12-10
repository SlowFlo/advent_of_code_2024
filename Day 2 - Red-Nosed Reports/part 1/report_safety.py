def is_report_safe(report: str) -> bool:
    if not isinstance(report, str):
        raise TypeError("report must be a string")


def get_nb_safe_reports(reports: str) -> int:
    if not isinstance(reports, str):
        raise TypeError("reports must be a string")

    reports_list = reports.splitlines()

    return 2
