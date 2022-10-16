from measurehero import UOMS

RE_UOMS = "|".join(UOMS.keys())

EXTRA_UOMS = {
    "metres": ["meter", 1],
    "m": ["meter", 1],
}
RE_EXTRA_UOMS = "|".join(EXTRA_UOMS.keys())


ALL_UOMS = UOMS | EXTRA_UOMS
RE_ALL_UOMS = "|".join(ALL_UOMS.keys())
