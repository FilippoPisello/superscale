from measurehero import UOMS

RE_ALL_UOMS = "|".join([uom.label for uom in UOMS])

PIECES_WORDS = [uom.label for uom in UOMS if uom.is_piece_measure()]
