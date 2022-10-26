from __future__ import annotations

from dataclasses import dataclass

from superscale import CONFIG
from superscale.exceptions import UnitOfMeasureNotFoundError
from superscale.extractor import extract_measure_from_string


@dataclass
class ItemMeasure:
    units: float = None
    unitary_measure: float = None
    total_measure: float = None
    unit_of_measure: str = None
    infer = True

    def __post_init__(self):
        if self.infer:
            self.fill_in_total_measure()
            self.fill_in_unitary_measure()

    def fill_in_total_measure(self) -> None:
        if self.total_measure is not None:
            return
        if (self.units is not None) & (self.unitary_measure is not None):
            self.total_measure = self.units * self.unitary_measure

    def fill_in_unitary_measure(self) -> None:
        if self.unitary_measure is not None:
            return
        try:
            self.unitary_measure = self.total_measure / self.units
        except TypeError:
            return

    @classmethod
    def from_string(cls, string: str) -> ItemMeasure:
        extraction = extract_measure_from_string(input_string=string)

        return cls(**extraction)

    def convert(self) -> None:
        try:
            uom_object = CONFIG.get_unit_of_measure(self.unit_of_measure)
        except UnitOfMeasureNotFoundError:
            return
        self.unit_of_measure = uom_object.convert_to
        self.unitary_measure = self.unitary_measure / uom_object.ratio
        self.total_measure = self.total_measure / uom_object.ratio


def scrape_measures(text: str) -> ItemMeasure:
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
    return ItemMeasure.from_string(text)
