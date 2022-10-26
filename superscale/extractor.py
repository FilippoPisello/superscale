from __future__ import annotations

from typing import Any

from superscale import CONFIG
from superscale.pattern_handlers import PATTERN_HANDLERS


def extract_measure_from_string(input_string: str) -> dict[str, Any]:
    input_string = clean_input_string(input_string)

    measure_dict = {
        "units": None,
        "unitary_measure": None,
        "total_measure": None,
        "unit_of_measure": None,
    }

    for pattern in PATTERN_HANDLERS:
        pattern = pattern(input_string)
        if pattern.is_match():
            measure_dict["units"] = pattern.get_units()
            measure_dict["unitary_measure"] = pattern.get_unitary_measure()
            measure_dict["total_measure"] = pattern.get_total_measure()
            measure_dict["unit_of_measure"] = pattern.get_unit_of_measure()

            return measure_dict

    return measure_dict


def clean_input_string(input_str: str) -> str:
    input_str = input_str.replace(",", ".").strip().lower()
    for character in CONFIG.multipack_symbols:
        input_str = input_str.replace(character, "x")
    return input_str
