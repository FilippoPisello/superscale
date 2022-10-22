import re

from measurehero import constants as CN

from . import regex_strings as RE


def clean_input_string(input_str: str) -> str:
    return input_str.replace(",", ".").replace("*", "x").strip().lower()


def extract_units(input_str: str) -> int:
    input_str = clean_input_string(input_str)

    if _pieces_words_in_name(input_str):
        res = re.search(RE.xNUMBER, input_str)
        if res:
            return int(res.group(1))
        res = re.search(r"\s*(\d+)", input_str)
        if res:
            return int(res.group(1))

    res = _re_search_end_of_string_first(RE.NUMBERxNUMBER_UOM, input_str)
    if res:
        return int(res.group(1))

    res = _re_search_end_of_string_first(RE.NUMBER_UOM_xNUMBER, input_str)
    if res:
        return int(res.group(4))

    res = re.search(RE.xNUMBER, input_str)
    if res:
        return int(res.group(1))

    return 1


def extract_unit_of_measure(input_str: str) -> str:
    input_str = clean_input_string(input_str)

    res = _re_search_end_of_string_first(RE.NUMBER_UOM, input_str)
    if res:
        return res.group(2)

    return None


def extract_unitary_measure(input_str: str) -> float:
    input_str = clean_input_string(input_str)

    res = _re_search_end_of_string_first(RE.NUMBERxNUMBER_UOM, input_str)
    if res:
        return float(res.group(2))

    res = _re_search_end_of_string_first(RE.NUMBER_UOM_xNUMBER, input_str)
    if res:
        return int(res.group(1))

    return None


def extract_total_measure(input_str: str) -> float:
    input_str = clean_input_string(input_str)

    res = _re_search_end_of_string_first(RE.NUMBERxNUMBER_UOM, input_str)
    if res:
        substring = res.group(0).strip()
        input_str = input_str.replace(substring, "")

    res = _re_search_end_of_string_first(RE.NUMBER_UOM_xNUMBER, input_str)
    if res:
        substring = res.group(0).strip()
        input_str = input_str.replace(substring, "")

    res = _re_search_end_of_string_first(RE.NUMBER_UOM, input_str)
    if res:
        return float(res.group(1))

    return None


def _pieces_words_in_name(product_name: str) -> bool:
    return any([word in product_name for word in CN.PIECES_WORDS])


def _re_search_end_of_string_first(
    pattern: str, input_str: str
) -> re.Match[str] | None:
    """Apply re.search first at the end input_string. If no match, apply with
    no constraint."""
    res = re.search(pattern + "$", input_str)
    if res:
        return res

    res = re.search(pattern, input_str)
    return res
