def is_strictly_increasing(sequence):
    return all(sequence[i] < sequence[i + 1] for i in range(len(sequence) - 1))


def is_strictly_decreasing(sequence):
    return all(sequence[i] > sequence[i + 1] for i in range(len(sequence) - 1))


def is_step_safe(sequence, max_step=3):
    return all(abs(sequence[i] - sequence[i + 1]) <= max_step for i in range(len(sequence) - 1))


def generate_subsequences(sequence):
    return [sequence[:i] + sequence[i + 1 :] for i in range(len(sequence))]


def is_report_safe(report: str) -> bool:
    if not isinstance(report, str):
        raise TypeError("report must be a string")

    values = list(map(int, report.split()))

    # Check if the report is already safe
    if (is_strictly_increasing(values) or is_strictly_decreasing(values)) and is_step_safe(values):
        return True

    # Check whether removing one level make it safe
    for subsequence in generate_subsequences(values):
        if (is_strictly_increasing(subsequence) or is_strictly_decreasing(subsequence)) and is_step_safe(subsequence):
            return True

    return False


def get_nb_safe_reports(reports: str) -> int:
    if not isinstance(reports, str):
        raise TypeError("reports must be a string")

    reports_list = reports.splitlines()

    return sum([is_report_safe(report) for report in reports_list])


if __name__ == "__main__":
    with open("puzzle_input.txt") as f:
        reports = f.read()
        print("Number of safe reports:", get_nb_safe_reports(reports))
