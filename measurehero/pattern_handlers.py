import re
from abc import ABC, abstractmethod

from . import constants as CN
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
    def search_string(self) -> None:
        ...

    def is_match(self) -> bool:
        return self.match

    def get_units(self) -> int:
        return self.units

    def get_unitary_measure(self) -> float:
        return self.unitary_measure

    def get_total_measure(self) -> float:
        return self.total_measure

    def get_unit_of_measure(self) -> str:
        return self.unit_of_measure

    @staticmethod
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


class HandlerNUMBERxNUMBER_UOM(PatternHandler):
    def search_string(self) -> str:
        res = self._re_search_end_of_string_first(RE.NUMBERxNUMBER_UOM, self.string)
        if not res:
            return

        self.match = True

        self.units = int(res.group(1))
        self.unitary_measure = float(res.group(2))
        self.unit_of_measure = res.group(3)


class HandlerNUMBER_UOM_xNUMBER(PatternHandler):
    def search_string(self) -> str:
        res = self._re_search_end_of_string_first(RE.NUMBER_UOM_xNUMBER, self.string)
        if not res:
            return

        self.match = True

        self.units = int(res.group(4))
        self.unitary_measure = float(res.group(1))
        self.unit_of_measure = res.group(2)


class HandlerNUMBER_UOM(PatternHandler):
    def search_string(self) -> str:
        res = self._re_search_end_of_string_first(RE.NUMBER_UOM, self.string)
        if not res:
            return

        self.match = True

        self.total_measure = float(res.group(1))
        self.unit_of_measure = res.group(2)


class HandlerxNUMBER(PatternHandler):
    def search_string(self) -> str:
        res = self._re_search_end_of_string_first(RE.xNUMBER, self.string)
        if not res:
            return

        self.match = True

        self.units = int(res.group(1))


class HandlerNUMBER_WITH_PIECES_WORD(PatternHandler):
    def search_string(self) -> str:
        if not self._pieces_words_in_name(self.string):
            return

        res = re.search(r"\s*(\d+)", self.string)
        if not res:
            res = re.search(RE.xNUMBER, self.string)

        self.match = True

        self.units = int(res.group(1))

    @staticmethod
    def _pieces_words_in_name(product_name: str) -> bool:
        return any([word in product_name for word in CN.PIECES_WORDS])


PATTERN_HANDLERS: list[type[PatternHandler]] = [
    HandlerNUMBERxNUMBER_UOM,
    HandlerNUMBER_UOM_xNUMBER,
    HandlerNUMBER_WITH_PIECES_WORD,
    HandlerNUMBER_UOM,
    HandlerxNUMBER,
]
