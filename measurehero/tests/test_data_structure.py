import pytest

from measurehero import ItemMeasure


def test_weight_inferred():
    ItemMeasure.infer = True

    mes = ItemMeasure(
        units=3, unitary_measure=4, total_measure=None, unit_of_measure=None
    )
    assert mes.total_measure == 12
    mes = ItemMeasure(
        units=3, unitary_measure=None, total_measure=12, unit_of_measure=None
    )
    assert mes.unitary_measure == 4


@pytest.mark.parametrize(
    ("measure", "expected"),
    [
        (ItemMeasure(3, 250, 1000, "ml"), ItemMeasure(3, 0.25, 1, "liter")),
        (ItemMeasure(3, None, None, None), ItemMeasure(3, None, None, None)),
    ],
)
def test_conversion(measure, expected):
    measure.convert()
    assert measure == expected
