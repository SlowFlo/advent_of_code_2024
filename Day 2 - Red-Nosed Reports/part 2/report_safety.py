import time


def is_strictly_increasing(sequence):
    return all(i < j for i, j in zip(sequence, sequence[1:]))


def is_strictly_decreasing(sequence):
    return all(i > j for i, j in zip(sequence, sequence[1:]))


def is_step_safe(sequence, max_step=3):
    return all(abs(i - j) <= max_step for i, j in zip(sequence, sequence[1:]))


def generate_problem_dampened_reports(sequence):
    for i in range(len(sequence)):
        yield sequence[:i] + sequence[i + 1 :]


def is_report_safe(values):
    return (is_strictly_increasing(values) or is_strictly_decreasing(values)) and is_step_safe(values)


def is_problem_dampened_report_safe(report: str) -> bool:
    if not isinstance(report, str):
        raise TypeError("report must be a string")

    values = list(map(int, report.split()))

    if is_report_safe(values):
        return True

    for problem_dampened_report in generate_problem_dampened_reports(values):
        if is_report_safe(problem_dampened_report):
            return True

    return False


def get_nb_safe_reports(reports: str) -> int:
    if not isinstance(reports, str):
        raise TypeError("reports must be a string")

    reports_list = reports.splitlines()

    return sum([is_problem_dampened_report_safe(report) for report in reports_list])


if __name__ == "__main__":
    start_time = time.time()
    with open("puzzle_input.txt") as f:
        reports = f.read()
        print("Number of safe reports:", get_nb_safe_reports(reports))

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time:.6f} seconds")
