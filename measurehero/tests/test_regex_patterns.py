import re

import pytest

from measurehero import regex_strings as RE


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
    assert actual.group(4) == expected


@pytest.mark.parametrize(
    ("input_string", "expected"),
    [
        ("naturnes epinards des 4/6mois nestle bols 2x130g", "130"),
    ],
)
def test_unitary_measure_pattern_1(input_string, expected):
    actual = re.search(RE.NUMBERxNUMBER_UOM, input_string)
    assert actual.group(2) == expected
