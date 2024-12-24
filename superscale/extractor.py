from __future__ import annotations

import re
import unicodedata

from superscale import CONFIG
from superscale.itemmeasure import ItemMeasure
from superscale.pattern_handlers import PATTERN_HANDLERS
from superscale.regex_strings import UNWANTED_PATTERNS


def scrape_measures(string: str) -> ItemMeasure:
    """Return size information found in the provided text.

    Args:
        text (str): the string to be searched.

    Returns:
        ArticleMeasure: custom object holding all the size information found.

    Examples:
        >>> import superscale
        >>> article = "Heinz Baked Beans In Tomato Sauce 4X415g"
        >>> superscale.scrape_measures(article)
        ItemMeasure(units=4.0, unitary_measure=415.0, total_measure=1660.0,
        unit_of_measure='g')
    """
    string = clean_input_string(string)

    for pattern in PATTERN_HANDLERS:
        result = pattern(string)
        if result is None:
            continue
        return result

    return ItemMeasure()


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
