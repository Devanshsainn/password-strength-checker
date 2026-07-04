from src.password_checker import check_length


def test_check_length_valid():
    assert check_length("Password123") is True


def test_check_length_invalid():
    assert check_length("Pass1") is False