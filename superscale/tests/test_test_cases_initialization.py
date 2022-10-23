import pandas as pd

from superscale.itemmeasure import ItemMeasure

from .load_test_cases import _test_cases_to_custom_object


def test_custom_test_cases_object_with_expected_input():
    df = pd.DataFrame(
        {
            "input_string": ["A", "B"],
            "units": [1, 2],
            "unitary_measure": [3, 4],
            "total_measure": [5, None],
            "unit_of_measure": ["kg", "g"],
        }
    )
    test_cases = _test_cases_to_custom_object(df)
    expected = [
        ("A", ItemMeasure(1, 3, 5, "kg")),
        ("B", ItemMeasure(2, 4, None, "g")),
    ]
    assert test_cases == expected
