import pytest

from superscale.extractor import scrape_measures

from .load_test_cases import load_test_cases

LOCALIZATION_CODE_FR = "fr"
TEST_CASES = load_test_cases(LOCALIZATION_CODE_FR)


@pytest.mark.parametrize(
    ("input_string", "expected"),
    TEST_CASES,
)
def test_units_extraction(input_string, expected):
    actual = scrape_measures(input_string)

    for attr in ["units", "total_measure", "unit_of_measure"]:
        assert getattr(actual, attr) == getattr(expected, attr)
