import json
from typing import Any

from superscale.unit_of_measure import UnitOfMeasure


def load_region(file_path: str) -> list[str]:
    content = _load_json_from_path(file_path)
    return content["region"]


def _load_json_from_path(file_path: str) -> dict[Any, Any]:
    with open(file_path) as f:
        return json.load(f)


def load_uoms(file_path: str, region: list[str]) -> dict[str, UnitOfMeasure]:
    content = _load_json_from_path(file_path)

    all_uoms = dict()

    for reg in region:
        all_uoms.update(content[reg])

    sorted_all_uoms = _sort_uoms_by_label_length_descending(all_uoms)
    return _uoms_dict_to_custom_objects(sorted_all_uoms)


def _sort_uoms_by_label_length_descending(uoms_dict):
    return {
        k: v
        for k, v in sorted(uoms_dict.items(), key=lambda key: len(key[0]), reverse=True)
    }


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
