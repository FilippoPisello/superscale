from __future__ import annotations

from dataclasses import dataclass


@dataclass
class UnitOfMeasure:
    label: str
    convert_to: str
    ratio: float
    priority: int = 1

    def is_piece_measure(self) -> bool:
        return self.convert_to == "piece"

    def is_length_measure(self) -> bool:
        return self.convert_to == "meter"

    def is_weight_measure(self) -> bool:
        return self.convert_to == "kilo"

    def is_volume_measure(self) -> bool:
        return self.convert_to == "liter"

    def is_kilo_synonym(self) -> bool:
        return (self.convert_to == "kilo") and (self.ratio == 1)
