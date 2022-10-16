import json
from typing import Any


def load_region(file_path: str) -> list[str]:
    content = _load_json_from_path(file_path)
    return content["region"]


def load_uoms(file_path: str, region: list[str]) -> dict[str, list]:
    content = _load_json_from_path(file_path)

    all_uoms = dict()

    for reg in region:
        all_uoms.update(content[reg])
    return all_uoms


def _load_json_from_path(file_path: str) -> dict[Any, Any]:
    with open(file_path) as f:
        return json.load(f)
