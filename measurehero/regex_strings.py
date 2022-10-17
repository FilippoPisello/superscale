from . import constants as CN

# For every variable comment expresses patterns to be matched

# General
NUMBER = "(\d+\.\d+|\d+)"  # number with or without decimals
NUMBERxNUMBER_UOM = rf"(\d+\s*x\s*{NUMBER}\s*({CN.RE_REGULAR_UOMS}))"  # 20x30g / 20 x 30 g / 20 x 30.5 g

# Units
xNUMBER = r"((?<!\d)x\d+)"  # 'x30' but not '10x30'
