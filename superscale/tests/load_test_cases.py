from typing import Any

import pandas as pd

from superscale.itemmeasure import ItemMeasure


def load_test_cases(localization_code: str) -> list[tuple[str, ItemMeasure]]:
    """Load test cases from the proper excel file."""
    file_path = _get_test_cases_file_path_per_localization(localization_code)
    df = pd.read_excel(file_path)
    return _test_cases_to_custom_object(df)


def _test_cases_to_custom_object(df: pd.DataFrame) -> list[tuple[str, ItemMeasure]]:
    test_cases = []
    ItemMeasure.infer = False

    for row in df.itertuples(index=False):

        input_string = _none_if_null(row.input_string)
        test_case = ItemMeasure(
            units=_none_if_null(row.units),
            unitary_measure=_none_if_null(row.unitary_measure),
            total_measure=_none_if_null(row.total_measure),
            unit_of_measure=_none_if_null(row.unit_of_measure),
        )

        test_cases.append((input_string, test_case))

    return test_cases


def _get_test_cases_file_path_per_localization(localization_code: str) -> str:
    return rf"superscale\tests\test_data\test_cases_{localization_code}.xlsx"


def _none_if_null(value: Any) -> Any:
    if pd.isnull(value):
        return None
    return value
