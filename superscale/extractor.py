from __future__ import annotations

import re
import unicodedata
from typing import Any

from superscale import CONFIG
from superscale.pattern_handlers import PATTERN_HANDLERS
from superscale.regex_strings import UNWANTED_PATTERNS


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
    input_str = _remove_accents(input_str)
    input_str = _remove_unwanted_patterns(input_str)
    for character in CONFIG.multipack_symbols:
        input_str = input_str.replace(character, "x")
    return _remove_double_spaces(input_str)


def _remove_accents(text: str) -> str:
    return "".join(
        c for c in unicodedata.normalize("NFD", text) if unicodedata.category(c) != "Mn"
    )


def _remove_unwanted_patterns(text: str) -> str:
    for pattern in UNWANTED_PATTERNS:
        res = re.search(pattern, text)
        if not res:
            continue
        text = text.replace(res.group(0), "")
    return text


def _remove_double_spaces(text: str) -> str:
    return text.replace("  ", " ")
