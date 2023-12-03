from typing import Optional, NamedTuple, Iterable

from lark import Lark, Transformer, Token

engine_grid_grammar = r'''
start: row+

row: item+ _NL
?item: INT    -> number
     | SYMBOL -> part_symbol
     | EMPTY  -> empty

SYMBOL: /[^0-9\.]/
EMPTY : "."
_NL   : NEWLINE

%import common.INT
%import common.NEWLINE
'''

type SchematicItem = int | str
type SchematicRow = list[Optional[SchematicItem]]


class TreeToSchematic(Transformer):
    start = list

    @staticmethod
    def row(row: list[list[Optional[SchematicItem]]]) -> SchematicRow:
        return [val for cells in row for val in cells]

    @staticmethod
    def number(number: list[Token]) -> list[int]:
        return [int(number[0].value) for _ in number[0].value]

    @staticmethod
    def part_symbol(part_symbol: list[Token]) -> list[str]:
        return [part_symbol[0].value]

    @staticmethod
    def empty(_) -> list[None]:
        return [None]


class Part:
    def __init__(self, schematic: 'EngineSchematic', *, symbol: str, row: int, col: int) -> None:
        self._schematic = schematic
        self._numbers = None
        self.symbol = symbol
        self.row = row
        self.col = col

    @property
    def is_gear(self) -> bool:
        return self.symbol == '*' and len(self.numbers) == 2

    @property
    def numbers(self) -> list[int]:
        if self._numbers is None:
            self._numbers = self._schematic.get_part_numbers(self.row, self.col)

        return self._numbers


class EngineSchematic(list[SchematicRow]):
    def __init__(self, rows: list[SchematicRow]):
        super().__init__(rows)
        self._parts = None

    @property
    def parts(self) -> list[Part]:
        if self._parts is None:
            self._parts = [
                Part(self, symbol=val, row=row_i, col=col_i)
                for row_i, row in enumerate(self)
                for col_i, val in enumerate(row)
                if isinstance(val, str)
            ]
        return self._parts

    def get_part_numbers(self, row: int, col: int) -> list[int]:
        numbers = []

        for _row in range(row - 1, row + 2):
            if not 0 <= _row < len(self):
                continue

            found_col = None
            for _col in range(col - 1, col + 2):
                if 0 <= _col < len(self[_row]) and isinstance(part_num := self[_row][_col], int):
                    if found_col and found_col + 1 == _col:
                        found_col = _col
                        continue

                    numbers.append(part_num)
                    found_col = _col

        return numbers

    @classmethod
    def from_file(cls, filename: str) -> 'EngineSchematic':
        with open(filename) as f:
            parsed_tree = Lark(engine_grid_grammar, parser='lalr').parse(f.read())
            return cls(TreeToSchematic().transform(parsed_tree))


def sum_all_part_numbers(schematic: EngineSchematic) -> int:
    return sum(number for part in schematic.parts for number in part.numbers)


def sum_all_gear_ratios(schematic: EngineSchematic) -> int:
    return sum(part.numbers[0] * part.numbers[1] for part in schematic.parts if part.is_gear)


def run(filename: str) -> None:
    schematic = EngineSchematic.from_file(filename)
    print('Sum of Part Numbers:', sum_all_part_numbers(schematic))
    print('Sum of Gear Ratios:', sum_all_gear_ratios(schematic))
