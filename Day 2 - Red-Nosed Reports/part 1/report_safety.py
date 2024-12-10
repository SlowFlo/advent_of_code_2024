def get_nb_safe_reports(reports: str):
    if not isinstance(reports, str):
        raise TypeError("reports must be a string")
