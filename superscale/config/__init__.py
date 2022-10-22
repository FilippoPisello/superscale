from . import load_config as config

REGION = config.load_region(r"superscale\config\region.json")
UOMS = config.load_uoms(r"superscale\config\unit_of_measure.json", REGION)
