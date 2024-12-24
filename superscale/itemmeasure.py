"""Data structure to represent the size of an item."""

from __future__ import annotations

from dataclasses import dataclass
from typing import ClassVar

from superscale import CONFIG
from superscale.config.load_config import UnitOfMeasureNotFoundError


@dataclass
class ItemMeasure:
    """Size information of an item."""

    units: float | None = None
    total_measure: float | None = None
    unit_of_measure: str | None = None

    infer: ClassVar[bool] = True

    @property
    def unitary_measure(self) -> float | None:
        """Return the unitary measure of the item.

        For example in a six pack of 330ml cans, the unitary measure is 330
        while the total measure is 6x330=1980.
        """
        if self.units and self.total_measure:
            return self.total_measure / self.units
        return None

    def convert(self) -> "ItemMeasure":
        """Return a new ItemMeasure object with the unit of measure converted."""
        try:
            uom_object = CONFIG.get_unit_of_measure(self.unit_of_measure)
        except UnitOfMeasureNotFoundError:
            return self
        return ItemMeasure(
            units=self.units,
            total_measure=self.total_measure / uom_object.ratio,
            unit_of_measure=uom_object.convert_to,
        )
