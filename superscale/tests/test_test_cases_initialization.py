import pandas as pd

from superscale.itemmeasure import ItemMeasure

from .load_test_cases import load_test_cases


def test_test_cases_loaded_into_proper_data_structure():
    test_cases = load_test_cases("fr")

    assert isinstance(test_cases, list)
    assert isinstance(test_cases[0], tuple)
    assert isinstance(test_cases[0][0], str)
    assert isinstance(test_cases[0][1], ItemMeasure)
