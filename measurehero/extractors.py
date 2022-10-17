import re

from measurehero import constants as CN

from . import regex_strings as RE


def clean_product_name(input_str: str) -> str:
    return input_str.replace(",", ".").replace("*", "x").strip().lower()


def extract_units(input_str: str) -> int:
    input_str = clean_product_name(input_str)

    if pieces_words_in_name(input_str):
        res = re.search(RE.xNUMBER, input_str)
        if res:
            return int(res.group(0).replace(" ", "").replace("x", ""))
        res = re.search(r"(\s*\d+)", input_str)
        if res:
            return int(res.group(0).replace(" ", ""))

    res = _re_search_end_of_string_first(RE.NUMBERxNUMBER_UOM, input_str)
    if res:
        return int(res.group(0).replace(" ", "").split("x")[0])

    res = re.search(RE.xNUMBER, input_str)
    if res:
        return int(res.group(0).replace(" ", "").replace("x", ""))

    return 1


def extract_unit_of_measure(input_str: str) -> str:
    input_str = clean_product_name(input_str)

    res = _re_search_end_of_string_first(RE.NUMBER_UOM, input_str)
    if res:
        res = res.group(0)
        return get_uom(res)

    return None


def extract_unitary_measure(input_str: str) -> float:
    input_str = clean_product_name(input_str)

    res = _re_search_end_of_string_first(RE.NUMBERxNUMBER_UOM, input_str)
    if res:
        return get_number_only(res.group(0).replace(" ", "").split("x")[1])

    return None


def extract_total_measure(input_str: str) -> float:
    input_str = clean_product_name(input_str)

    res = _re_search_end_of_string_first(RE.NUMBERxNUMBER_UOM, input_str)
    if res:
        substring = res.group(0).strip()
        input_str = input_str.replace(substring, "")

    res = _re_search_end_of_string_first(RE.NUMBER_UOM, input_str)
    if res:
        return get_number_only(res.group(0).replace(" ", ""))

    return None


def pieces_words_in_name(product_name: str) -> bool:
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


def get_number_only(number_and_uom: str) -> float:
    return float("".join([c for c in number_and_uom if c.isdigit() or c == "."]))


def get_uom(number_and_uom: str) -> str:
    res = re.search(rf"(({CN.RE_REGULAR_UOMS}))", number_and_uom)
    return res.group(0)
