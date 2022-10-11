UOMS = {
    "ml": ["liter", 1000],
    "cl": ["liter", 100],
    "litres": ["liter", 1],
    "litre": ["liter", 1],
    "l": ["liter", 1],
    "g": ["kilo", 1000],
    "gmes": ["kilo", 1000],
    "kilo": ["kilo", 1],
    "kg": ["kilo", 1],
    "pcs": ["piece", 1],
    "fruits": ["piece", 1],
    "piece": ["piece", 1],
    "pieces": ["piece", 1],
    "unites": ["piece", 1],
    "sachets": ["piece", 1],
    "sachet": ["piece", 1],
}
RE_UOMS = "|".join(UOMS.keys())

EXTRA_UOMS = {
    "metres": ["meter", 1],
    "m": ["meter", 1],
}
RE_EXTRA_UOMS = "|".join(EXTRA_UOMS.keys())

RE_UNIT_QTY = "\d+\.\d+|\d+"

ALL_UOMS = UOMS | EXTRA_UOMS
RE_ALL_UOMS = "|".join(ALL_UOMS.keys())
