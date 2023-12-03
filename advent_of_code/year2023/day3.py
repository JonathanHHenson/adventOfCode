from typing import Optional, NamedTuple

from lark import Lark, Transformer, Token

engine_grid_grammar = r'''
start: row+

row: item+ _NL
?item: INT    -> num
     | SYMBOL -> symbol
     | EMPTY  -> empty

SYMBOL: /[^0-9\.]/
EMPTY : "."
_NL   : NEWLINE

%import common.INT
%import common.NEWLINE
'''

PartNum = int
Symbol = str

type SchematicItem = PartNum | Symbol
type SchematicRow = list[Optional[SchematicItem]]
type EngineSchematic = list[SchematicRow]


class SymbolCoords(NamedTuple):
    symbol: Symbol
    row: int
    col: int


class TreeToEngineGrid(Transformer):
    start = list

    @staticmethod
    def row(row: list[list[Optional[SchematicItem]]]) -> SchematicRow:
        return [val for cells in row for val in cells]

    @staticmethod
    def num(num: list[Token]) -> list[PartNum]:
        return [int(num[0].value) for _ in num[0].value]

    @staticmethod
    def symbol(symbol: list[Token]) -> list[Symbol]:
        return [symbol[0].value]

    @staticmethod
    def empty(_) -> list[None]:
        return [None]


def parse_grid(filename: str) -> EngineSchematic:
    with open(filename) as f:
        parsed_tree = Lark(engine_grid_grammar, parser='lalr').parse(f.read())
        return TreeToEngineGrid().transform(parsed_tree)


def get_symbol_coords(grid: EngineSchematic) -> set[SymbolCoords]:
    return {
        SymbolCoords(val, row_i, col_i)
        for row_i, row in enumerate(grid)
        for col_i, val in enumerate(row)
        if isinstance(val, Symbol)
    }


def get_part_nums(grid: EngineSchematic, *, at_symbol: SymbolCoords) -> set[PartNum]:
    part_nums = set()

    for row in range(at_symbol.row - 1, at_symbol.row + 2):
        if not 0 <= row < len(grid):
            continue

        for col in range(at_symbol.col - 1, at_symbol.col + 2):
            if 0 <= col < len(grid[row]) and isinstance(part_num := grid[row][col], PartNum):
                part_nums.add(part_num)

    return part_nums


def sum_part_numbers(filename: str) -> int:
    grid = parse_grid(filename)
    symbol_coords = get_symbol_coords(grid)
    part_numbers = [
        part_num
        for coords in symbol_coords
        for part_num in get_part_nums(grid, at_symbol=coords)
    ]
    return sum(part_numbers)


def run(filename: str) -> None:
    print('Sum of Part Numbers:', sum_part_numbers(filename))
