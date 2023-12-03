import pytest

from advent_of_code.year2023.day3 import sum_part_numbers, get_symbol_coords, get_part_nums, parse_grid, SymbolCoords


def test_get_symbol_coords(tc_2023_day3):
    grid = parse_grid(tc_2023_day3)
    coords = get_symbol_coords(grid)

    assert coords == {
        SymbolCoords('*', 1, 3),
        SymbolCoords('#', 3, 6),
        SymbolCoords('*', 4, 3),
        SymbolCoords('+', 5, 5),
        SymbolCoords('$', 8, 3),
        SymbolCoords('*', 8, 5)
    }


@pytest.mark.parametrize('coords, expected', [
    (SymbolCoords('*', 1, 3), {467, 35}),
    (SymbolCoords('#', 3, 6), {633, 42}),
    (SymbolCoords('*', 4, 3), {617, 42}),
    (SymbolCoords('+', 5, 5), {592, 42}),
    (SymbolCoords('$', 8, 3), {664}),
    (SymbolCoords('*', 8, 5), {598, 755}),
])
def test_get_part_nums(tc_2023_day3, coords: SymbolCoords, expected: set[int]):
    grid = parse_grid(tc_2023_day3)

    part_nums = get_part_nums(grid, at_symbol=coords)

    assert part_nums == expected


def test_sum_part_numbers(tc_2023_day3):
    result = sum_part_numbers(tc_2023_day3)

    assert result == 4487
