import pytest

from advent_of_code.year2023.day4 import parse_card, Card, parse_cards, scratch_card_total, dupe_cards_total


@pytest.mark.parametrize('card_str,expected', [
    (
        'Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53',
        Card(1, {41, 48, 83, 86, 17}, {83, 86, 6, 31, 17, 9, 48, 53})
    )
])
def test_parse_card(card_str: str, expected: Card):
    parsed_card = parse_card(card_str)

    assert parsed_card == expected


@pytest.mark.parametrize('card,expected', [
    (Card(1, {41, 48, 83, 86, 17}, {83, 86, 6, 31, 17, 9, 48, 53}), 8),
    (Card(2, {13, 32, 20, 16, 61}, {61, 30, 68, 82, 17, 32, 24, 19}), 2),
    (Card(3, {1, 21, 53, 59, 44}, {69, 82, 63, 72, 16, 21, 14, 1}), 2),
    (Card(4, {41, 92, 73, 84, 69}, {59, 84, 76, 51, 58, 5, 54, 83}), 1),
    (Card(5, {87, 83, 26, 28, 32}, {88, 30, 70, 12, 93, 22, 82, 36}), 0),
    (Card(6, {31, 18, 13, 56, 72}, {74, 77, 10, 23, 35, 67, 36, 11}), 0),
])
def test_score_card(card: Card, expected: int):
    assert card.score == expected


def test_scratch_card_total(tc_2023_day4):
    cards = parse_cards(tc_2023_day4)

    result = scratch_card_total(cards)

    assert result == 13


def test_dupe_cards_total(tc_2023_day4):
    cards = parse_cards(tc_2023_day4)

    result = dupe_cards_total(cards)

    assert result == 30
