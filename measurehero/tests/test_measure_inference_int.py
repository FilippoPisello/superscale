import pytest

from measurehero import extractors as ext

from .load_test_cases import load_test_cases

LOCALIZATION_CODE_FR = "fr"
TEST_CASES = load_test_cases(LOCALIZATION_CODE_FR)


@pytest.mark.parametrize(
    ("input_string", "units"),
    TEST_CASES.units,
)
def test_units_extraction(input_string, units):
    return ext.extract_units_info(input_string) == units
