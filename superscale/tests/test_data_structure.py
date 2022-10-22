import pytest

from superscale import ArticleMeasure


def test_weight_inferred():
    ArticleMeasure.infer = True

    mes = ArticleMeasure(
        units=3, unitary_measure=4, total_measure=None, unit_of_measure=None
    )
    assert mes.total_measure == 12
    mes = ArticleMeasure(
        units=3, unitary_measure=None, total_measure=12, unit_of_measure=None
    )
    assert mes.unitary_measure == 4


@pytest.mark.parametrize(
    ("measure", "expected"),
    [
        (ArticleMeasure(3, 250, 1000, "ml"), ArticleMeasure(3, 0.25, 1, "liter")),
        (ArticleMeasure(3, None, None, None), ArticleMeasure(3, None, None, None)),
    ],
)
def test_conversion(measure, expected):
    measure.convert()
    assert measure == expected
