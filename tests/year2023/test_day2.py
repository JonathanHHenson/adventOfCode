import pytest

from advent_of_code.year2023.day2 import sum_valid_games, validate_game, parse_game, min_cube_power, sum_min_cube_powers

PART1_INIT_CUBES = {
    'red': 12,
    'green': 13,
    'blue': 14
}


@pytest.mark.parametrize('game_str,expected', [
    ('Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green', True),
    ('Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue', True),
    ('Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red', False),
    ('Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red', False),
    ('Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green', True),
])
def test_validate_game(game_str: str, expected: bool) -> None:
    _, moves = parse_game(game_str)
    result = validate_game(PART1_INIT_CUBES, moves)
    assert result == expected


@pytest.mark.parametrize('game_str,expected', [
    ('Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green', 48),
    ('Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue', 12),
    ('Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red', 1560),
    ('Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red', 630),
    ('Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green', 36),
])
def test_min_cube_power(game_str: str, expected: int) -> None:
    _, moves = parse_game(game_str)
    result = min_cube_power(moves)
    assert result == expected


def test_sum_calibration(tc_2023_day2):
    result = sum_valid_games(tc_2023_day2, PART1_INIT_CUBES)
    assert result == 8


def test_sum_min_cube_powers(tc_2023_day2):
    result = sum_min_cube_powers(tc_2023_day2)
    assert result == 2286
