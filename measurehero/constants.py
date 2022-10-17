from measurehero import UOMS

RE_REGULAR_UOMS = "|".join([uom.label for uom in UOMS if not uom.is_piece_measure()])

PIECES_WORDS = [uom.label for uom in UOMS if uom.is_piece_measure()]
