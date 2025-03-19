from typing import Any, Optional
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

PROJECT_FOLDER: str = os.path.join(os.path.dirname(BRCI_CWD), 'Projects')
BACKUP_FOLDER: str = os.path.join(os.path.dirname(BRCI_CWD), 'Backups')
BRCI_RESOURCES_FOLDER: str = os.path.join(os.path.dirname(BRCI_CWD), 'resources')

NO_THUMBNAIL: str = os.path.join(BRCI_RESOURCES_FOLDER, 'no_thumbnail.png')
BRCI_THUMBNAIL: str = os.path.join(BRCI_RESOURCES_FOLDER, 'brci.png')
BLANK_THUMBNAIL: str = os.path.join(BRCI_RESOURCES_FOLDER, 'blank.png')
MISSING_THUMBNAIL: str = os.path.join(BRCI_RESOURCES_FOLDER, 'missing_thumbnail.png')

# Settings
settings: dict[str, Any] = {
    'numpy': False,
    'show_logs': False,
    'wip_features': False
}

def wip_features(new_setting: Optional[bool]) -> bool:
    """
    Change wip_features setting.

    Arguments:
        new_setting (Optional[bool]): Set setting or toggle if None.

    Returns:
        bool: New setting
    """
    settings['wip_features'] = new_setting if new_setting is not None else not settings['wip_features']
    return settings['wip_features']

def try_numpy(new_setting: Optional[bool]) -> bool:
    """
    Change try_numpy (numpy) setting.

    Arguments:
        new_setting (Optional[bool]): Set setting or toggle if None.

    Returns:
        bool: New setting
    """
    settings['numpy'] = new_setting if new_setting is not None else not settings['numpy']
    return settings['numpy']

def show_logs(new_setting: Optional[bool]) -> bool:
    """
    Change show_logs setting.

    Arguments:
        new_setting (Optional[bool]): Set setting or toggle if None.

    Returns:
        bool: New setting
    """
    settings['show_logs'] = new_setting if new_setting is not None else not settings['show_logs']
    return settings['show_logs']