import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from src.password_checker import (
    check_length,
    check_uppercase,
    check_lowercase,
    check_digits,
    check_special_characters,
    calculate_score,
    get_strength_label,
)


def test_check_length_valid():
    assert check_length("Password123") is True


def test_check_length_invalid():
    assert check_length("Pass1") is False


def test_check_uppercase():
    assert check_uppercase("Password") is True
    assert check_uppercase("password") is False


def test_check_lowercase():
    assert check_lowercase("Password") is True
    assert check_lowercase("PASSWORD") is False


def test_check_digits():
    assert check_digits("Password123") is True
    assert check_digits("Password") is False


def test_check_special_characters():
    assert check_special_characters("Password!") is True
    assert check_special_characters("Password") is False


def test_calculate_score():
    assert calculate_score("Password123!") == 5
    assert calculate_score("password") == 2


def test_strength_label():
    assert get_strength_label(1) == "🔴 Weak"
    assert get_strength_label(3) == "🟡 Moderate"
    assert get_strength_label(4) == "🟢 Strong"
    assert get_strength_label(5) == "🟢 Very Strong"