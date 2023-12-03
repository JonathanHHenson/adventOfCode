import pytest

from advent_of_code.year2023.day3 import sum_all_part_numbers, EngineSchematic, sum_all_gear_ratios


def test_get_symbol_coords(tc_2023_day3_a):
    schematic = EngineSchematic.from_file(tc_2023_day3_a)
    parts = [(part.symbol, part.row, part.col) for part in schematic.parts]

    assert parts == [
        ('*', 1, 3),
        ('#', 3, 6),
        ('*', 4, 3),
        ('+', 5, 5),
        ('$', 8, 3),
        ('*', 8, 5)
    ]


@pytest.mark.parametrize('row,col,expected', [
    (1, 3, [467, 467]),
    (3, 6, [42, 633]),
    (4, 3, [42, 617]),
    (5, 5, [42, 592]),
    (8, 3, [664]),
    (8, 5, [598, 755]),
])
def test_get_part_nums(tc_2023_day3_a, row: int, col: int, expected: set[int]):
    schematic = EngineSchematic.from_file(tc_2023_day3_a)

    part_nums = sorted(schematic.get_part_numbers(row, col))

    assert part_nums == expected


def test_sum_part_numbers(tc_2023_day3_a):
    schematic = EngineSchematic.from_file(tc_2023_day3_a)

    result = sum_all_part_numbers(schematic)

    assert result == 4919


def test_sum_all_gear_ratios(tc_2023_day3_b):
    schematic = EngineSchematic.from_file(tc_2023_day3_b)

    result = sum_all_gear_ratios(schematic)

    assert result == 467835

