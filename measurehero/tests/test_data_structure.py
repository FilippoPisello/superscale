from measurehero import ItemMeasure


def test_weight_inferred():
    ItemMeasure.infer = True

    mes = ItemMeasure(
        units=3, unitary_measure=4, total_measure=None, unit_of_measure=None
    )
    assert mes.total_measure == 12
    mes = ItemMeasure(
        units=3, unitary_measure=None, total_measure=12, unit_of_measure=None
    )
    assert mes.unitary_measure == 4
