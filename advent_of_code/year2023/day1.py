import re
from typing import Iterable

ALPHA_DIGITS = ('one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine')
ALPHA_DIGITS_LOOKUP = {
    **{str(i): str(i) for i in range(10)},
    **{digit: str(i + 1) for i, digit in enumerate(ALPHA_DIGITS)}
}

BASIC_CALIBRATION_REGEX = re.compile(r'(\d)(?:.*(\d))?')
ADVANCED_DIGIT_GROUP = rf'\d|{'|'.join(ALPHA_DIGITS)}'
ADVANCED_CALIBRATION_REGEX = re.compile(rf'({ADVANCED_DIGIT_GROUP})(?:.*({ADVANCED_DIGIT_GROUP}))?')


def sum_calibration_values(filename: str, *, advanced: bool = False) -> int:
    return sum(get_calibration_values(filename, advanced=advanced))


def get_calibration_values(filename: str, *, advanced: bool = False) -> Iterable[int]:
    with open(filename) as f:
        for line in f:
            yield get_calibration_value(line, advanced=advanced)


def get_calibration_value(line: str, *, advanced: bool = False) -> int:
    if advanced:
        calibration_regex = ADVANCED_CALIBRATION_REGEX
    else:
        calibration_regex = BASIC_CALIBRATION_REGEX

    match calibration_regex.search(line).groups():
        case num, None:
            return int(ALPHA_DIGITS_LOOKUP[num] * 2)
        case num_a, num_b:
            return int(ALPHA_DIGITS_LOOKUP[num_a] + ALPHA_DIGITS_LOOKUP[num_b])


def run(filename: str) -> None:
    print('Sum of Calibration Values:', sum_calibration_values(filename))
    print('Sum of Calibration Values (advanced):', sum_calibration_values(filename, advanced=True))
