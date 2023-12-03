from functools import reduce
from typing import Iterable

from lark import Lark, Transformer, Token

type Move = dict[str, int]
type GameRecord = tuple[int, list[Move]]

game_records_grammar = '''
start: game

game: "Game" id ":" moves
id: NUMBER
moves: move (";" move)*
move: cube ("," cube)*
cube: NUMBER WORD

%import common.WORD
%import common.NUMBER
%import common.WS

%ignore WS
'''


class TreeToGameRecords(Transformer):
    game = tuple
    moves = list
    move = dict

    @staticmethod
    def start(game: tuple[GameRecord]) -> GameRecord:
        return game[0]

    @staticmethod
    def id(_id: tuple[Token]) -> int:
        return int(_id[0].value)

    @staticmethod
    def cube(cube: tuple[Token, Token]) -> tuple[str, int]:
        return cube[1].value, int(cube[0].value)


def parse_game(game_str: str) -> GameRecord:
    parser_tree = Lark(game_records_grammar, parser='lalr').parse(game_str)
    return TreeToGameRecords().transform(parser_tree)


def parse_games(filename: str) -> Iterable[GameRecord]:
    with open(filename) as f:
        for line in f:
            yield parse_game(line)


def validate_game(init_cubes: dict[str, int], moves: list[Move]) -> bool:
    for move in moves:
        for colour, amount in move.items():
            if amount > init_cubes.get(colour, 0):
                return False
    return True


def min_init_cubes(moves: list[Move]) -> dict[str, int]:
    init_cubes = dict()
    for move in moves:
        for colour, amount in move.items():
            if amount > init_cubes.get(colour, 1):
                init_cubes[colour] = amount
    return init_cubes


def min_cube_power(moves: list[Move]) -> int:
    return reduce(lambda a, b: a * b, min_init_cubes(moves).values(), 1)


def sum_valid_games(filename: str, init_cubes: dict[str, int]) -> int:
    return sum(i for i, moves in parse_games(filename) if validate_game(init_cubes, moves))


def sum_min_cube_powers(filename: str) -> int:
    return sum(min_cube_power(moves) for _, moves in parse_games(filename))


def run(filename: str) -> None:
    print('Sum of Valid Game Ids:', sum_valid_games(filename, {
        'red': 12,
        'green': 13,
        'blue': 14
    }))
    print('Sum of Min Cube Powers:', sum_min_cube_powers(filename))
