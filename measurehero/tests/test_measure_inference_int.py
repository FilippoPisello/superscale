import pytest

from measurehero import extractors as ext

from .load_test_cases import load_test_cases

LOCALIZATION_CODE_FR = "fr"
TEST_CASES = load_test_cases(LOCALIZATION_CODE_FR)


@pytest.mark.parametrize(
    ("input_string", "expected_units"),
    TEST_CASES.units,
)
def test_units_extraction(input_string, expected_units):
    assert ext.extract_units(input_string) == expected_units
