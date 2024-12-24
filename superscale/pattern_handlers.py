from __future__ import annotations

import re
from typing import Callable

from superscale.itemmeasure import ItemMeasure

from . import constants as CN
from . import regex_strings as RE

PatternMatcher = Callable[[str], ItemMeasure | None]

UOM_GROUPS = [CN.RE_WEIGHT_UOMS, CN.RE_VOLUME_UOMS, CN.RE_REGULAR_UOMS]


def NUMBER_METERxNUMBER_METER(string: str) -> ItemMeasure | None:
    res = re.search(RE.NUMBER_METERxNUMBER_METER, string)
    if not res:
        return

    dim1 = float(res.group(1))
    dim2 = float(res.group(3))
    return ItemMeasure(
        units=1, total_measure=max(dim1, dim2), unit_of_measure=res.group(2)
    )


def NUMBERxNUMBER_UOM(string: str) -> ItemMeasure | None:
    res = _match_against_uom_groups(RE.NUMBERxNUMBER_UOM, string)
    if not res:
        return

    units = float(res.group(1))
    return ItemMeasure(
        units=units,
        total_measure=float(res.group(2)) * units,
        unit_of_measure=res.group(3),
    )


def NUMBER_UOM_xNUMBER(string: str) -> ItemMeasure | None:
    res = _match_against_uom_groups(RE.NUMBER_UOM_xNUMBER, string)
    if not res:
        return

    units = float(res.group(3))
    return ItemMeasure(
        units=units,
        total_measure=float(res.group(1)) * units,
        unit_of_measure=res.group(2),
    )


def xNUMBER(string: str) -> ItemMeasure | None:
    res = re.search(RE.xNUMBER, string)
    if not res:
        return

    units = float(res.group(1))

    res = _match_against_uom_groups(RE.NO_SYMBOL_NUMBER_UOM, string)
    if not res:
        return ItemMeasure(units=units)

    return ItemMeasure(
        units=units,
        total_measure=float(res.group(1)),
        unit_of_measure=res.group(2),
    )


def NUMBER_UOM(string: str) -> ItemMeasure | None:
    res = _match_against_uom_groups(RE.NO_SYMBOL_NUMBER_UOM, string)
    if not res:
        return

    return ItemMeasure(
        units=1,
        total_measure=float(res.group(1)),
        unit_of_measure=res.group(2),
    )


def NUMBER_WITH_PIECES_WORD(string: str) -> ItemMeasure | None:
    if not _pieces_words_in_name(string):
        return

    for pattern in [RE.ISOLATED_INTEGER, RE.xNUMBER, RE.INTEGER_UOM_PIECE]:
        res = re.search(pattern, string)
        if res:
            break
    else:
        return

    units = float(res.group(1))

    res = _match_against_uom_groups(RE.NUMBER_UOM, string)
    if not res:
        return ItemMeasure(units=units)

    return ItemMeasure(
        units=units,
        total_measure=float(res.group(1)),
        unit_of_measure=res.group(2),
    )


def _pieces_words_in_name(product_name: str) -> bool:
    if re.search(RE.UOM_WORD, product_name):
        return True
    return False


def FRACTION_UOM(string: str) -> ItemMeasure | None:
    res = _match_against_uom_groups(RE.FRACTION_UOM, string)
    if not res:
        return

    return ItemMeasure(
        units=1,
        total_measure=float(res.group(1)) / float(res.group(2)),
        unit_of_measure=res.group(3),
    )


def NUMBER(string: str) -> ItemMeasure | None:
    res = re.search(RE.NUMBER, string)
    if not res:
        return

    return ItemMeasure(units=float(res.group(1)))


def ISOLATED_KILO(string: str) -> ItemMeasure | None:
    res = re.search(RE.ISOLATED_KILO, string)
    if not res:
        return

    return ItemMeasure(units=1, total_measure=1, unit_of_measure=res.group(1))


def NUMBER_UOM_LETTER(string: str) -> ItemMeasure | None:
    res = _match_against_uom_groups(RE.NUMBER_UOM_LETTER, string)
    if not res:
        return

    return ItemMeasure(
        units=1,
        total_measure=float(res.group(1)),
        unit_of_measure=res.group(2),
    )


def xNUMBER_LETTER(string: str) -> ItemMeasure | None:
    res = re.search(RE.xNUMBER_LETTER, string)
    if not res:
        return

    units = float(res.group(1))

    res = _match_against_uom_groups(RE.NO_SYMBOL_NUMBER_UOM, string)
    if not res:
        return ItemMeasure(units=units)

    return ItemMeasure(
        units=units,
        total_measure=float(res.group(1)),
        unit_of_measure=res.group(2),
    )


def _match_against_uom_groups(pattern: str, string: str) -> re.Match | None:
    """Test the same pattern against different UOM groups.

    We need to test UOMs in this way to force priority over the different types,
    in particular trying weight and volume before other less likely stuff like
    length.

    Setting the UOMs directly in the pattern does not result in the same behavior
    because the regex might branch out on the wrong UOM because of an earlier
    alternative block.
    """
    for uom_patterns in UOM_GROUPS:
        res = re.search(pattern.replace("<uom-regex>", uom_patterns), string)
        if res:
            return res
    return None


PATTERN_HANDLERS: list[PatternMatcher] = [
    NUMBER_METERxNUMBER_METER,
    NUMBERxNUMBER_UOM,
    NUMBER_UOM_xNUMBER,
    xNUMBER,
    xNUMBER_LETTER,
    NUMBER_WITH_PIECES_WORD,
    FRACTION_UOM,
    NUMBER_UOM,
    NUMBER_UOM_LETTER,
    NUMBER,
    ISOLATED_KILO,
]
