import is_leap_year 


def test_is_leap_year_not_zero() -> None:
    """There is no year 0, it starts on 1, so year 0 is False"""
    assert is_leap_year(0) == False

def test_is_leap_year_not_negative_number() -> None:
    assert is_leap_year(-4) == False
    assert is_leap_year(-12) == False
    assert is_leap_year(-20) == False

def test_is_leap_year_not_divisible_by_100() -> None:
    assert is_leap_year(100) == False
    assert is_leap_year(200) == False
    assert is_leap_year(300) == False
    assert is_leap_year(1000) == False
    assert is_leap_year(1700) == False
    assert is_leap_year(2100) == False

def test_is_leap_year_divisible_by_4() -> None:
    assert is_leap_year(4) == True
    assert is_leap_year(12) == True
    assert is_leap_year(20) == True

def test_is_leap_year_is_divisible_by_400() -> None:
    assert is_leap_year(400) == True
    assert is_leap_year(800) == True
    assert is_leap_year(1200) == True
    assert is_leap_year(1600) == True
    assert is_leap_year(2000) == True
    assert is_leap_year(2400) == True
    assert is_leap_year(2800) == True

def test_is_leap_year__numbers_that_are_divisable_to_4():
    assert is_leap_year(3) == False
    assert is_leap_year(9) == False
    assert is_leap_year(233) == False
    assert is_leap_year(2003) == False

def test_is_leap_year_is_int_datatype() -> None:
    """Checking datatype int is the only acceptable input"""
    assert is_leap_year(4.0) == False
    assert is_leap_year(True) == False
    assert is_leap_year("4") == False
