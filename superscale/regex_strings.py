from . import constants as CN

# For every variable comment expresses patterns to be matched

# General
NUMBER = "(\d+\.\d+|\d+)"  # number with or without decimals
FRACTION = "(\d+)/(\d+)"  # 1/3 | 10/30 | 1/30 | 30/5

NUMBER_UOM = rf"{NUMBER}\s*({CN.RE_REGULAR_UOMS})(?:$|\s)"  # 30g | 30 g | 30.0 g
NO_SYMBOL_NUMBER_UOM = rf"(?:^|\s|[a-z]){NUMBER_UOM}"  # like above but NOT 15|30kg
FRACTION_UOM = rf"{FRACTION}\s*({CN.RE_REGULAR_UOMS})(?:$|\s)"

NUMBERx = r"(\d+)\s*x\s*"  # 30x | 30 x
xNUMBER = r"(?<!\d)x\s*(\d+)(?:$|\s)"  # 'x30' | 'x 30' | NOT '10x30' | NOT 'x30.3'

NUMBERxNUMBER_UOM = rf"{NUMBERx}{NUMBER_UOM}"  # 20x30g | 20 x 30g | 20x32.5g
NUMBER_UOM_xNUMBER = rf"{NUMBER_UOM}{xNUMBER}"  # 30g x 2 | 30gx2 | 32.5gx20

NUMBER_LENGHT_UOM = rf"{NUMBER}\s*({CN.RE_LENGTH_UOMS})(?:$|\s)"  # 30m | 30 meters
NUMBER_METERxNUMBER_METER = (
    rf"{NUMBER_LENGHT_UOM}\s*x\s*{NUMBER_LENGHT_UOM}"  # 30m x 20m
)
