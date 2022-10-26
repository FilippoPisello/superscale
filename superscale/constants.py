from superscale import CONFIG

REGULAR_UOMS = []
LENGTH_UOMS = []
PIECES_UOMS = []
KILO_UOMS = []

for _, uom in CONFIG.units_of_measure.items():
    if uom.is_piece_measure():
        PIECES_UOMS.append(uom.label)
        continue
    if uom.is_length_measure():
        LENGTH_UOMS.append(uom.label)
    if uom.is_kilo_synonym():
        KILO_UOMS.append(uom.label)
    REGULAR_UOMS.append(uom.label)

RE_REGULAR_UOMS = "|".join(REGULAR_UOMS)
RE_LENGTH_UOMS = "|".join(LENGTH_UOMS)
RE_KILO_UOMS = "|".join(KILO_UOMS)
