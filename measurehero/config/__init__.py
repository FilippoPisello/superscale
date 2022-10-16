from . import load_config as config

REGION = config.load_region(r"measurehero\config\region.json")
UOMS = config.load_uoms(r"measurehero\config\unit_of_measure.json", REGION)
