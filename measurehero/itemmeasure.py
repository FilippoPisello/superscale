from __future__ import annotations

from dataclasses import dataclass

from measurehero.extractors import extract_measure_from_string


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
