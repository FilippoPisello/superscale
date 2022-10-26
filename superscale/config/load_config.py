from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from superscale.exceptions import UnitOfMeasureNotFoundError
from superscale.unit_of_measure import UnitOfMeasure


@dataclass
class Config:
    config_file_path: Path

    def load(self) -> None:
        """Overwrite current settings with content of config.json"""
        self._content = self._load_json_from_path(self.config_file_path)

        self.multipack_symbols = self._get_multipack_symbols()
        self.region = self._get_region()
        self.units_of_measure = self._get_units_of_measure()

    @staticmethod
    def _load_json_from_path(file_path: str) -> dict[Any, Any]:
        with open(file_path) as f:
            return json.load(f)

    def _get_multipack_symbols(self) -> list[str]:
        return self._content["multipack_symbols"]

    def _get_region(self) -> list[str]:
        return self._content["region"]

    def _get_units_of_measure(self) -> dict[str, UnitOfMeasure]:
        config_uoms = self._content["units_of_measure"]

        all_uoms = dict()

        for reg in self.region:
            all_uoms.update(config_uoms[reg])

        sorted_all_uoms = self._sort_uoms_by_label_length_descending(all_uoms)
        return self._uoms_dict_to_custom_objects(sorted_all_uoms)

    @staticmethod
    def _sort_uoms_by_label_length_descending(
        uoms_dict: dict[str, dict]
    ) -> dict[str, dict]:
        return {
            k: v
            for k, v in sorted(
                uoms_dict.items(), key=lambda key: len(key[0]), reverse=True
            )
        }

    @staticmethod
    def _uoms_dict_to_custom_objects(
        uoms_dict: dict[str, dict]
    ) -> dict[str, UnitOfMeasure]:
        return {
            uom: UnitOfMeasure(
                label=uom,
                convert_to=data["convert_to"],
                ratio=data["ratio"],
                priority=data["priority"],
            )
            for uom, data in uoms_dict.items()
        }

    def get_unit_of_measure(self, uom_string: str) -> UnitOfMeasure:
        """Return the UnitOfMeasure object corresponding to the provided
        string."""
        try:
            return self.units_of_measure[uom_string]
        except KeyError as e:
            raise UnitOfMeasureNotFoundError from e

    def change_region(self, region: list[str]) -> None:
        """Update region setting and refresh units of measure accordingly."""
        self.region = region
        self.units_of_measure = self._get_units_of_measure()
