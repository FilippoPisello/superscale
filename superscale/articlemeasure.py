from __future__ import annotations

from dataclasses import dataclass

from superscale import UOMS
from superscale.extractor import extract_measure_from_string


@dataclass
class ArticleMeasure:
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
    def from_string(cls, string: str) -> ArticleMeasure:
        extraction = extract_measure_from_string(input_string=string)

        return cls(**extraction)

    def convert(self) -> None:
        try:
            uom_object = UOMS[self.unit_of_measure]
        except KeyError:
            return
        self.unit_of_measure = uom_object.convert_to
        self.unitary_measure = self.unitary_measure / uom_object.ratio
        self.total_measure = self.total_measure / uom_object.ratio