from typing import NamedTuple

from lark import Transformer, Token, Lark

scratch_card_grammar = r'''
?start: card

card: "Card" INT ":" numbers "|" numbers
numbers: INT+

%import common.INT
%import common.WS

%ignore WS
'''


class Card(NamedTuple):
    num: int
    winning_nums: set[int]
    selected_nums: set[int]

    @property
    def score(self) -> int:
        score_power = self.matched - 1
        return 2 ** score_power if score_power >= 0 else 0

    @property
    def matched(self) -> int:
        return len(self.winning_nums & self.selected_nums)


class TreeToScratchCard(Transformer):
    INT = int
    numbers = set

    @staticmethod
    def card(card: list[int, set[int], set[int]]) -> Card:
        return Card(*card)


def parse_card(card_str: str) -> Card:
    tree = Lark(scratch_card_grammar, parser='lalr').parse(card_str)
    return TreeToScratchCard().transform(tree)


def parse_cards(filename) -> list[Card]:
    with open(filename) as f:
        return [parse_card(card_str) for card_str in f]


def scratch_card_total(cards: list[Card]) -> int:
    return sum(card.score for card in cards)


def dupe_cards_total(cards: list[Card]) -> int:
    copies = {card.num: 1 for card in cards}
    for card in cards:
        for num in range(card.num + 1, card.num + card.matched + 1):
            if num in copies:
                copies[num] += copies[card.num]
    return sum(copies.values())


def run(filename: str) -> None:
    cards = parse_cards(filename)

    print('Scratch Card Total:', scratch_card_total(cards))
    print('Dupe Cards Total:', dupe_cards_total(cards))
