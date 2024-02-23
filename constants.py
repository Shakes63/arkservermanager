from pathlib import Path

STEAMCMD_URL: str = 'https://steamcdn-a.akamaihd.net/client/installer/steamcmd.zip'

DEFAULT_WORKING_DIR: Path = Path.home().joinpath('Ark_Server_Manager')

working_dir: Path = Path.home().joinpath('Ark_Server_Manager')

STEAMCMD_EXE_PATH: Path = working_dir / 'Steam' / 'steamcmd.exe'

STEAMCMD_ZIP_PATH: Path = working_dir / 'Steam' / Path(STEAMCMD_URL).name
