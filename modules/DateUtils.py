from datetime import datetime, date

current_date = datetime.now().date()
date_format = "%d/%m/%Y"


def get_current_date_string():
    return date.strftime(current_date, date_format)


def get_date_from_string(date_string: str):
    return datetime.strptime(date_string, date_format).date()


def compare_date_to_current_date(date_string: str):
    return get_date_from_string(date_string) >= current_date
