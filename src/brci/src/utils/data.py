from typing import Any
import os

# Paths
BRCI_CWD: str = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
_LOCALAPPDATA: str = os.getenv("LOCALAPPDATA")

if os.name == 'nt':
    _USER: str = os.getenv('%USERNAME%')
    BRICK_RIGS_FOLDER: list[str] = [os.path.join(_LOCALAPPDATA, 'BrickRigs', 'SavedRemastered', 'Vehicles')]
else:
    _USER: str = os.getenv('$USER')
    # TODO: Get something safer than this
    BRICK_RIGS_FOLDER: list[str] = [
        os.path.expanduser(f"~/.steam/steamapps/compatdata/552100/pfx/drive_c/users/steamuser/AppData/Local/BrickRigs/SavedRemastered/Vehicles"),
        os.path.expanduser(f"~/.wine/drive_c/users/{_USER}/AppData/Local/BrickRigs/SavedRemastered/Vehicles"),
        os.path.expanduser(f"~/.local/share/Steam/steamapps/compatdata/552100/pfx/drive_c/users/steamuser/AppData/Local/BrickRigs/SavedRemastered/Vehicles")
    ]

PROJECT_FOLDER: str = os.path.join(BRCI_CWD, 'Projects')
BACKUP_FOLDER: str = os.path.join(BRCI_CWD, 'Backups')

NO_THUMBNAIL: str = os.path.join(BRCI_CWD, 'resources', 'no_thumbnail.png')
BRCI_THUMBNAIL: str = os.path.join(BRCI_CWD, 'resources', 'brci.png')
BLANK_THUMBNAIL: str = os.path.join(BRCI_CWD, 'resources', 'blank.png')
MISSING_THUMBNAIL: str = os.path.join(BRCI_CWD, 'resources', 'missing_thumbnail.png')

# Settings
settings: dict[str, Any] = {
    'numpy': False,
    'show_logs': False,
    'wip_features': False
}
