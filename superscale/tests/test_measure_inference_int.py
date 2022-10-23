import pytest

from superscale.itemmeasure import ItemMeasure

from .load_test_cases import load_test_cases

LOCALIZATION_CODE_FR = "fr"
TEST_CASES = load_test_cases(LOCALIZATION_CODE_FR)


@pytest.mark.parametrize(
    ("input_string", "expected"),
    TEST_CASES,
)
def test_units_extraction(input_string, expected):
    ItemMeasure.infer = True
    actual = ItemMeasure.from_string(input_string)

    for attr in ["units", "unitary_measure", "total_measure", "unit_of_measure"]:
        assert getattr(actual, attr) == getattr(expected, attr)
