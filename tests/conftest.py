import re
import pathlib

import pytest

DATA_DIR = pathlib.Path(__file__).parent / 'data'
TC_FIXTURE_REGEX = re.compile(r'^tc_(?P<year>\d+)_(?P<file>\w+)$')


def pytest_generate_tests(metafunc):
    """
    Creates fixtures to obtain files for Advent of Code tests
    """
    for fixture in metafunc.fixturenames:
        if match := TC_FIXTURE_REGEX.match(fixture):
            filename = DATA_DIR / match.group('year') / f'{match.group('file')}.txt'
            if not filename.exists():
                raise IOError(f'File {filename} does not exist')

            metafunc.parametrize(fixture, [filename.absolute()])
