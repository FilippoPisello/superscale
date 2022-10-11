import pandas as pd

from measurehero import ItemMeasure


def load_test_cases(localization_code: str) -> dict[str, ItemMeasure]:
    file_path = get_test_cases_file_path_per_localization(localization_code)
    df = pd.read_excel(file_path)

    loaded_test_cases = dict()
    for row in df.itertuples(index=False):
        mes = ItemMeasure(
            units=row.units,
            unitary_measure=row.unitary_weight,
            total_measure=row.total_weight,
            unit_of_measure=row.unit_of_measure,
        )
        loaded_test_cases[row.input_string] = mes
    return loaded_test_cases


def get_test_cases_file_path_per_localization(localization_code: str) -> str:
    return rf"measurehero\tests\test_data\test_cases_{localization_code}.xlsx"
