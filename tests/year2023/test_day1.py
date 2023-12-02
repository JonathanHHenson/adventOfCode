import pytest

from advent_of_code.year2023.day1 import sum_calibration_values, get_calibration_value


@pytest.mark.parametrize('advanced,line,expected', [
    (False, '1abc2', 12),
    (False, 'pqr3stu8vwx', 38),
    (False, 'a1b2c3d4e5f', 15),
    (False, 'treb7uchet', 77),
    (True, 'two1nine', 29),
    (True, 'eightwothree', 83),
    (True, 'abcone2threexyz', 13),
    (True, 'xtwone3four', 24),
    (True, '4nineeightseven2', 42),
    (True, 'zoneight234', 14),
    (True, '7pqrstsixteen', 76),
    (True, 'trknlxnv43zxlrqjtwonect', 41)
])
def test_get_calibration_value(advanced: bool, line: str, expected: int):
    result = get_calibration_value(line, advanced=advanced)
    assert result == expected


def test_sum_calibration(tc_2023_day1_a):
    result = sum_calibration_values(tc_2023_day1_a)
    assert result == 142


def test_sum_calibration_advanced(tc_2023_day1_b):
    result = sum_calibration_values(tc_2023_day1_b, advanced=True)
    assert result == 281
