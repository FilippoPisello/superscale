"""Data structure to represent the size of an item."""

from __future__ import annotations

from dataclasses import dataclass
from typing import ClassVar

from superscale import CONFIG
from superscale.config.load_config import UnitOfMeasureNotFoundError
from superscale.extractor import extract_measure_from_string


@dataclass
class ItemMeasure:
    """Size information of an item."""

    units: float | None = None
    unitary_measure: float | None = None
    total_measure: float | None = None
    unit_of_measure: str | None = None

    infer: ClassVar[bool] = True

    def __post_init__(self):
        if self.infer:
            self.fill_in_total_measure()
            self.fill_in_unitary_measure()

    def fill_in_total_measure(self) -> None:
        if self.total_measure is not None:
            return
        if (self.units is not None) and (self.unitary_measure is not None):
            self.total_measure = self.units * self.unitary_measure

    def fill_in_unitary_measure(self) -> None:
        if self.unitary_measure is not None:
            return
        if (self.units is not None) and (self.total_measure is not None):
            self.unitary_measure = self.total_measure / self.units

    @classmethod
    def from_string(cls, string: str) -> ItemMeasure:
        extraction = extract_measure_from_string(input_string=string)

        return cls(**extraction)

    def convert(self) -> "ItemMeasure":
        """Return a new ItemMeasure object with the unit of measure converted."""
        try:
            uom_object = CONFIG.get_unit_of_measure(self.unit_of_measure)
        except UnitOfMeasureNotFoundError:
            return self
        return ItemMeasure(
            units=self.units,
            unitary_measure=self.unitary_measure / uom_object.ratio,
            total_measure=self.total_measure / uom_object.ratio,
            unit_of_measure=uom_object.convert_to,
        )


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
