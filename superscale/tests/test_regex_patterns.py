import re

import pytest

from superscale import regex_strings as RE
from superscale.pattern_handlers import HandlerNUMBER_WITH_PIECES_WORD


@pytest.mark.parametrize(
    ("input_string", "expected"),
    [
        ("naturnes epinards des 4/6mois nestle bols 2x130g", "2"),
    ],
)
def test_units_pattern_1(input_string, expected):
    actual = re.search(RE.NUMBERx, input_string).group(1)
    assert actual == expected


@pytest.mark.parametrize(
    ("input_string", "expected"),
    [("naturnes epinards des 4/6mois nestle bols 2x130g", "2")],
)
def test_units_pattern_2(input_string, expected):
    actual = re.search(RE.NUMBERxNUMBER_UOM, input_string).group(1)
    assert actual == expected


@pytest.mark.parametrize(
    ("input_string", "expected"),
    [
        ("couches baby dry pants pampers geant taille 7 x30", "30"),
        ("saum.fume norv.labeyr.x2tr 75g", "2"),
    ],
)
def test_units_pattern_3(input_string, expected):
    actual = re.search(RE.xNUMBER, input_string)
    assert actual.group(1) == expected


@pytest.mark.parametrize(
    ("input_string", "expected"),
    [
        ("naturnes epinards des 4/6mois nestle bols 130g x 2", "2"),
    ],
)
def test_units_pattern_4(input_string, expected):
    actual = re.search(RE.NUMBER_UOM_xNUMBER, input_string)
    assert actual.group(3) == expected


@pytest.mark.parametrize(
    ("input_string", "expected"),
    [
        ("naturnes epinards des 4/6mois nestle bols 2x130g", "130"),
    ],
)
def test_unitary_measure_pattern_1(input_string, expected):
    actual = re.search(RE.NUMBERxNUMBER_UOM, input_string)
    assert actual.group(2) == expected


@pytest.mark.parametrize(
    ("input_string", "expected"),
    [
        ("aluminium rouleau 20 metres x 0.29 metres", "20"),
    ],
)
def test_length_pattern_1(input_string, expected):
    actual = re.search(RE.NUMBER_METERxNUMBER_METER, input_string)
    assert actual.group(1) == expected


def test_fraction_pattern():
    actual = re.search(RE.FRACTION_UOM, "huile d'olive u 1/2 litre")
    assert actual.group(1) == "1"
    assert actual.group(2) == "2"
    assert actual.group(3) == "litre"


def test_kilo_pattern():
    actual = re.search(RE.ISOLATED_KILO, "frites u sachet kg")
    assert actual.group(1) == "kg"


def test_piece_uom_pattern():
    actual = re.search(RE.INTEGER_UOM_PIECE, "saumon fume ecosse 2tr 75g")
    assert actual.group(1) == "2"


@pytest.mark.parametrize(
    ("text", "is_found"),
    [("cora film etirable 20 metres", False), ("saumon fume ecosse 2tr 75g", True)],
)
def test_pieces_word_is_found(text, is_found):
    assert HandlerNUMBER_WITH_PIECES_WORD._pieces_words_in_name(text) == is_found
