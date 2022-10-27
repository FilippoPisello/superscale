from . import constants as CN

# For every variable comment expresses patterns to be matched

# General
ISOLATED_INTEGER = r"\s+(\d+)(?:$|\s)"
NUMBER = r"(\d+\.\d+|\d+)"  # number with or without decimals
FRACTION = r"(\d+)/(\d+)"  # 1/3 | 10/30 | 1/30 | 30/5

INTEGER_UOM_PIECE = rf"(\d+)\s*({CN.RE_PIECES_UOMS})" # 2pieces | 3tr. | 4 units

NUMBER_UOM = rf"{NUMBER}\s*({CN.RE_REGULAR_UOMS})(?:$|\s)"  # 30g | 30 g | 30.0 g
NO_SYMBOL_NUMBER_UOM = rf"(?:^|\s|[a-z]|[a-z].){NUMBER_UOM}"  # NOT 15/30kg | A/30kg
FRACTION_UOM = rf"{FRACTION}\s*({CN.RE_REGULAR_UOMS})(?:$|\s)"
NUMBER_UOM_LETTER = rf"{NUMBER}\s*({CN.RE_REGULAR_UOMS})(?:$|\s|[a-z])"  # 30gA | 30 gA | 30.0 gA


NUMBERx = r"(\d+)\s*x\s*"  # 30x | 30 x
xNUMBER = r"(?<!\d)x\s*(\d+)(?:$|\s|[a-z])"  # 'x30' | 'x 30' | NOT '10x30' | NOT 'x30.3'

xNUMBER_LETTER = r"(?<!\d)x\s*(\d+)(?:$|\s)"  # 'x30' | 'x 30' | NOT '10x30' | NOT 'x30.3'


NUMBERxNUMBER_UOM = rf"{NUMBERx}{NUMBER_UOM}"  # 20x30g | 20 x 30g | 20x32.5g
NUMBER_UOM_xNUMBER = rf"{NUMBER_UOM}{xNUMBER}"  # 30g x 2 | 30gx2 | 32.5gx20

NUMBER_LENGHT_UOM = rf"{NUMBER}\s*({CN.RE_LENGTH_UOMS})(?:$|\s)"  # 30m | 30 meters
NUMBER_METERxNUMBER_METER = rf"{NUMBER_LENGHT_UOM}\s*x\s*{NUMBER_LENGHT_UOM}"  # 30m x 20m

ISOLATED_KILO = rf"\s+({CN.RE_KILO_UOMS})(?:$|\s)"  # ' KG ' | ' kilo '

UOM_WORD = rf"(?<![a-z])({CN.RE_PIECES_UOMS})(?![a-z])"

UNWANTED_PATTERNS = [
    r"(\d\s*(in|en)\s*\d)", # '3 in 1 ' | '3in1'
    r"(\d+\s*%)", # '3 in 1 ' | '3in1'
]