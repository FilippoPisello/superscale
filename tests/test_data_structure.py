import pytest

from superscale import ItemMeasure


@pytest.mark.parametrize(
    ("measure", "expected"),
    [
        (ItemMeasure(3, 1000, "ml"), ItemMeasure(3, 1, "liter")),
        (ItemMeasure(3, None, None), ItemMeasure(3, None, None)),
    ],
)
def test_conversion(measure, expected):
    assert measure.convert() == expected
