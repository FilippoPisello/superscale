from . import constants as CN

# For every variable comment expresses patterns to be matched

# General
NUMBER = "(\d+\.\d+|\d+)"  # number with or without decimals
NUMBER_UOM = rf"({NUMBER}\s*({CN.RE_REGULAR_UOMS}))"  # 30g / 30 g / 30.0 g
NUMBERxNUMBER_UOM = rf"(\d+\s*x\s*{NUMBER_UOM[1:-1]})"  # 20x30g / 20 x 30g / 20x32.5g

# Units
xNUMBER = r"((?<!\d)x\d+)"  # 'x30' but not '10x30'