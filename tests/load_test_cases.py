from __future__ import annotations

import csv
from pathlib import Path
from typing import Any, Type

from superscale.itemmeasure import ItemMeasure
from tests import TEST_DATA_DIR


def load_test_cases(localization_code: str) -> list[tuple[str, ItemMeasure]]:
    """Load test cases from the proper csv file."""
    file_path = TEST_DATA_DIR / f"test_cases_{localization_code}.csv"
    return _test_cases_to_custom_object(file_path)


def _test_cases_to_custom_object(file: Path) -> list[tuple[str, ItemMeasure]]:
    test_cases = []
    ItemMeasure.infer = False

    with open(file, encoding="utf8") as csv_file:
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


def _coerce_to_type(value: Any, _type: Type) -> Any:
    if not value:
        return None
    return _type(value)
