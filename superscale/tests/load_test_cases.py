from __future__ import annotations

import csv
from pathlib import Path
from typing import Any, Type

from superscale.itemmeasure import ItemMeasure


def load_test_cases(localization_code: str) -> list[tuple[str, ItemMeasure]]:
    """Load test cases from the proper csv file."""
    file_path = _get_test_cases_file_path_per_localization(localization_code)
    return _test_cases_to_custom_object(file_path)


def _test_cases_to_custom_object(file_path: str) -> list[tuple[str, ItemMeasure]]:
    test_cases = []
    ItemMeasure.infer = False

    with open(file_path, encoding="utf8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")

        for row_number, row in enumerate(csv_reader):
            # Skip header row
            if row_number == 0:
                continue

            input_string = _coerce_to_type(row[0], str)
            test_case = ItemMeasure(
                units=_coerce_to_type(row[1], int),
                unitary_measure=_coerce_to_type(row[2], float),
                total_measure=_coerce_to_type(row[3], float),
                unit_of_measure=_coerce_to_type(row[4], str),
            )

            test_cases.append((input_string, test_case))

    return test_cases


def _get_test_cases_file_path_per_localization(localization_code: str) -> str:
    _current_dir = Path(__file__).parent.resolve()
    suffix = rf"test_data\test_cases_{localization_code}.csv"
    return Path(_current_dir / suffix)


def _coerce_to_type(value: Any, type: Type) -> Any:
    if not value:
        return None
    return type(value)
