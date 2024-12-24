from __future__ import annotations

import re
from abc import ABC, abstractmethod

from . import regex_strings as RE


class PatternHandler(ABC):
    def __init__(self, string: str) -> None:
        self.string = string

        self.match = False
        self.units = 1
        self.unitary_measure = None
        self.total_measure = None
        self.unit_of_measure = None

        self.search_string()

    @abstractmethod
    def search_string(self) -> None: ...

    def is_match(self) -> bool:
        return self.match

    def get_units(self) -> int:
        return self.units

    def get_unitary_measure(self) -> float | None:
        return self.unitary_measure

    def get_total_measure(self) -> float | None:
        return self.total_measure

    def get_unit_of_measure(self) -> str | None:
        return self.unit_of_measure


class NUMBER_METERxNUMBER_METER(PatternHandler):
    def search_string(self) -> str | None:
        res = re.search(RE.NUMBER_METERxNUMBER_METER, self.string)
        if not res:
            return

        self.match = True

        dim1 = float(res.group(1))
        dim2 = float(res.group(3))
        self.total_measure = max(dim1, dim2)
        self.unit_of_measure = res.group(2)


class NUMBERxNUMBER_UOM(PatternHandler):
    def search_string(self) -> str | None:
        res = re.search(RE.NUMBERxNUMBER_UOM, self.string)
        if not res:
            return

        self.match = True

        self.units = float(res.group(1))
        self.unitary_measure = float(res.group(2))
        self.unit_of_measure = res.group(3)


class NUMBER_UOM_xNUMBER(PatternHandler):
    def search_string(self) -> str | None:
        res = re.search(RE.NUMBER_UOM_xNUMBER, self.string)
        if not res:
            return

        self.match = True

        self.units = float(res.group(3))
        self.unitary_measure = float(res.group(1))
        self.unit_of_measure = res.group(2)


class xNUMBER(PatternHandler):
    def search_string(self) -> str | None:
        res = re.search(RE.xNUMBER, self.string)
        if not res:
            return

        self.match = True

        self.units = float(res.group(1))

        res = re.search(RE.NO_SYMBOL_NUMBER_UOM, self.string)
        if not res:
            return
        self.total_measure = float(res.group(1))
        self.unit_of_measure = res.group(2)


class NUMBER_UOM(PatternHandler):
    def search_string(self) -> str | None:
        res = re.search(RE.NO_SYMBOL_NUMBER_UOM, self.string)
        if not res:
            return

        self.match = True

        self.total_measure = float(res.group(1))
        self.unit_of_measure = res.group(2)


class NUMBER_WITH_PIECES_WORD(PatternHandler):
    def search_string(self) -> str | None:
        if not self._pieces_words_in_name(self.string):
            return

        for pattern in [RE.ISOLATED_INTEGER, RE.xNUMBER, RE.INTEGER_UOM_PIECE]:
            res = re.search(pattern, self.string)
            if res:
                break
        if not res:
            return

        self.match = True

        self.units = float(res.group(1))

        res = re.search(RE.NUMBER_UOM, self.string)
        if not res:
            return
        self.total_measure = float(res.group(1))
        self.unit_of_measure = res.group(2)

    @staticmethod
    def _pieces_words_in_name(product_name: str) -> bool:
        if re.search(RE.UOM_WORD, product_name):
            return True
        return False


class FRACTION_UOM(PatternHandler):
    def search_string(self) -> str | None:
        res = re.search(RE.FRACTION_UOM, self.string)
        if not res:
            return

        self.match = True

        self.total_measure = float(res.group(1)) / float(res.group(2))
        self.unit_of_measure = res.group(3)


class NUMBER(PatternHandler):
    def search_string(self) -> str | None:
        res = re.search(RE.NUMBER, self.string)
        if not res:
            return

        self.match = True

        self.units = float(res.group(1))


class ISOLATED_KILO(PatternHandler):
    def search_string(self) -> str | None:
        res = re.search(RE.ISOLATED_KILO, self.string)
        if not res:
            return

        self.match = True

        self.total_measure = 1
        self.unit_of_measure = res.group(1)


class NUMBER_UOM_LETTER(PatternHandler):
    def search_string(self) -> str | None:
        res = re.search(RE.NUMBER_UOM_LETTER, self.string)
        if not res:
            return

        self.match = True

        self.total_measure = float(res.group(1))
        self.unit_of_measure = res.group(2)


class xNUMBER_LETTER(PatternHandler):
    def search_string(self) -> str | None:
        res = re.search(RE.xNUMBER_LETTER, self.string)
        if not res:
            return

        self.match = True

        self.units = float(res.group(1))

        res = re.search(RE.NO_SYMBOL_NUMBER_UOM, self.string)
        if not res:
            return
        self.total_measure = float(res.group(1))
        self.unit_of_measure = res.group(2)


PATTERN_HANDLERS: list[type[PatternHandler]] = [
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
