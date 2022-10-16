import pandas as pd

from .load_test_cases import _test_cases_to_custom_object


def test_custom_test_cases_object_with_expected_input():
    df = pd.DataFrame(
        {
            "input_string": ["A", "B"],
            "units": [1, 2],
            "unitary_measure": [3, 4],
            "total_measure": [5, 6],
            "unit_of_measure": ["kg", "g"],
        }
    )
    test_cases = _test_cases_to_custom_object(df)

    assert test_cases.units == [("A", 1), ("B", 2)]
    assert test_cases.unitary_measure == [("A", 3), ("B", 4)]
    assert test_cases.total_measure == [("A", 5), ("B", 6)]
    assert test_cases.unit_of_measure == [("A", "kg"), ("B", "g")]
