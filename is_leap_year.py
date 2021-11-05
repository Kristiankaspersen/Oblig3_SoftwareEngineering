
def is_leap_year(year: int) -> bool:
    """Cheking if a year is a leapyear"""
    if isinstance(year, int):
        if year <= 0:
            return False
        elif year % 400 == 0:
            return True
        elif year % 100 != 0 and year % 4 == 0:
            return True
        else:
            return False
    else:
        return False
