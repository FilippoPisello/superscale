from dataclasses import dataclass


@dataclass
class ItemMeasure:
    units: float = None
    unitary_measure: float = None
    total_measure: float = None
    unit_of_measure: str = None

    def __post_init__(self):
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
