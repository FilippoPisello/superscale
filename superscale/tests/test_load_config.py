from superscale import UnitOfMeasure
from superscale.config import load_config as config


def test_region_is_parsed_from_config():
    actual = config.load_region(r"superscale\tests\test_data\region.json")
    assert actual == ["int", "fr"]


def test_unit_of_measure_is_parsed_from_config_with_one_region():
    file_path = r"superscale\tests\test_data\unit_of_measure.json"
    actual = config.load_uoms(file_path, ["int"])
    expected = {
        "ml": UnitOfMeasure("ml", "liter", 1000, 1),
        "cl": UnitOfMeasure("cl", "liter", 100, 1),
    }
    assert actual == expected


def test_unit_of_measure_is_parsed_from_config_with_two_regions():
    file_path = r"superscale\tests\test_data\unit_of_measure.json"
    actual = config.load_uoms(file_path, ["int", "fr"])
    expected = {
        "litres": UnitOfMeasure("litres", "liter", 1, 1),
        "litre": UnitOfMeasure("litre", "liter", 1, 1),
        "ml": UnitOfMeasure("ml", "liter", 1000, 1),
        "cl": UnitOfMeasure("cl", "liter", 100, 1),
    }
    assert actual == expected
