import re
from typing import Iterable

ALPHA_DIGITS = ('one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine')
ALPHA_DIGITS_LOOKUP = {
    **{str(i): str(i) for i in range(10)},
    **{digit: str(i + 1) for i, digit in enumerate(ALPHA_DIGITS)}
}

BASIC_CALIBRATION_REGEX = re.compile(r'\d')
ADVANCED_CALIBRATION_REGEX = re.compile(rf'(?=(\d|{'|'.join(ALPHA_DIGITS)}))')


def sum_calibration_values(filename: str, *, advanced: bool = False) -> int:
    return sum(get_calibration_values(filename, advanced=advanced))


def get_calibration_values(filename: str, *, advanced: bool = False) -> Iterable[int]:
    return (get_calibration_value(line, advanced=advanced) for line in open(filename))


def get_calibration_value(line: str, *, advanced: bool = False) -> int:
    if advanced:
        digits = [m.group(1) for m in ADVANCED_CALIBRATION_REGEX.finditer(line)]
    else:
        digits = BASIC_CALIBRATION_REGEX.findall(line)

    return int(ALPHA_DIGITS_LOOKUP[digits[0]] + ALPHA_DIGITS_LOOKUP[digits[-1]])


def run(filename: str) -> None:
    print('Sum of Calibration Values:', sum_calibration_values(filename))
    print('Sum of Calibration Values (advanced):', sum_calibration_values(filename, advanced=True))
