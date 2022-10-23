import pytest

from superscale.config import Config
from superscale.unit_of_measure import UnitOfMeasure


@pytest.fixture
def test_config():
    TEST_CONFIG = Config(r"superscale\tests\test_data\config.json")
    TEST_CONFIG.load()
    return TEST_CONFIG


def test_region_is_parsed_from_config(test_config):
    assert test_config.region == ["int", "fr"]


def test_unit_of_measure_is_parsed_from_config_with_one_region(test_config):
    test_config.change_region(["int"])

    expected = {
        "ml": UnitOfMeasure("ml", "liter", 1000, 1),
        "cl": UnitOfMeasure("cl", "liter", 100, 1),
    }
    assert test_config.units_of_measure == expected


def test_unit_of_measure_is_parsed_from_config_with_two_regions(test_config):
    test_config.change_region(["int", "fr"])

    expected = {
        "litres": UnitOfMeasure("litres", "liter", 1, 1),
        "litre": UnitOfMeasure("litre", "liter", 1, 1),
        "ml": UnitOfMeasure("ml", "liter", 1000, 1),
        "cl": UnitOfMeasure("cl", "liter", 100, 1),
    }
    assert test_config.units_of_measure == expected
