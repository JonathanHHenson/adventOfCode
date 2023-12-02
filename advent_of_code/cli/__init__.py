import importlib
from pathlib import Path

import typer


def main(year: int, day: int, filename: Path) -> None:
    aoc_day = importlib.import_module(f'advent_of_code.year{year}.day{day}')
    print(f'Running Advent of Code ({year=}, {day=})')
    aoc_day.run(filename)


def run():
    typer.run(main)


if __name__ == '__main__':
    run()
