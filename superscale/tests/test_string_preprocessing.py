import pytest

from superscale import extractor as ext


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("mètres", "metres"),
        ("François", "francois"),
        ("cora film étirable 2 en 1 20 mètres", "cora film etirable 20 metres"),
        (r"bours.past.sal.ape.afh 40%120g", "bours.past.sal.ape.afh 120g"),
    ],
)
def test_text_preprocessing(text, expected):
    assert ext.clean_input_string(text) == expected
