"""The cannon package."""
from pathlib import Path

DATA_DIR = Path.home() / ".local/share/cannon"
TEMPEST_WORKSPACE = DATA_DIR / "cannon-workspace"
TEMPEST_CONF = TEMPEST_WORKSPACE / "etc/tempest.conf"