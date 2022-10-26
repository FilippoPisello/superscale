from pathlib import Path

from .load_config import Config

_config_dir = Path(__file__).parent.resolve()
CONFIG = Config(Path(_config_dir / "config.json"))
CONFIG.load()
