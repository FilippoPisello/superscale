from dataclasses import dataclass, field
from typing import Any

import pandas as pd


@dataclass
class ParametrizedTestCases:
    """Hold data for test cases in a compact way.

    Each attribute is to be passed as parametrized input for pytest."""

    units: list[tuple[str, int]] = field(default_factory=list)
    unitary_measure: list[tuple[str, float | None]] = field(default_factory=list)
    total_measure: list[tuple[str, float | None]] = field(default_factory=list)
    unit_of_measure: list[tuple[str, str | None]] = field(default_factory=list)


def load_test_cases(localization_code: str) -> ParametrizedTestCases:
    """Load test cases from the proper excel file."""
    file_path = _get_test_cases_file_path_per_localization(localization_code)
    df = pd.read_excel(file_path)
    return _test_cases_to_custom_object(df)


def _test_cases_to_custom_object(df: pd.DataFrame) -> ParametrizedTestCases:
    test_cases = ParametrizedTestCases()
    for row in df.itertuples(index=False):

        input_string = _none_if_null(row.input_string)
        units = _none_if_null(row.units)
        unitary_measure = _none_if_null(row.unitary_measure)
        total_measure = _none_if_null(row.total_measure)
        unit_of_measure = _none_if_null(row.unit_of_measure)

        test_cases.units.append((input_string, units))
        test_cases.unitary_measure.append((input_string, unitary_measure))
        test_cases.total_measure.append((input_string, total_measure))
        test_cases.unit_of_measure.append((input_string, unit_of_measure))

    return test_cases


def _get_test_cases_file_path_per_localization(localization_code: str) -> str:
    return rf"measurehero\tests\test_data\test_cases_{localization_code}.xlsx"


def _none_if_null(value: Any) -> Any:
    if pd.isnull(value):
        return None
    return value
