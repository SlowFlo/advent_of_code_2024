def is_report_safe(report: str) -> bool:
    if not isinstance(report, str):
        raise TypeError("report must be a string")

    levels = list(map(int, report.split()))
    previous_level = levels[0]
    previous_is_increasing = None
    has_problem_dampener_been_activated = False

    for level in levels[1:]:
        is_increasing = level > previous_level
        if previous_is_increasing is not None and previous_is_increasing != is_increasing:
            if has_problem_dampener_been_activated:
                return False
            else:
                has_problem_dampener_been_activated = True
                continue

        difference_previous_level = abs(level - previous_level)
        if difference_previous_level == 0 or difference_previous_level > 3:
            if has_problem_dampener_been_activated:
                return False
            else:
                has_problem_dampener_been_activated = True
                continue

        previous_level = level
        previous_is_increasing = is_increasing

    return True


def get_nb_safe_reports(reports: str) -> int:
    if not isinstance(reports, str):
        raise TypeError("reports must be a string")

    reports_list = reports.splitlines()

    return sum([is_report_safe(report) for report in reports_list])


if __name__ == "__main__":
    with open("puzzle_input.txt") as f:
        reports = f.read()
        print("Number of safe reports:", get_nb_safe_reports(reports))
