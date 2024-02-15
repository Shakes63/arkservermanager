import os
from pathlib import Path

ASA_STEAM_ID: str = '2430930'

STEAMCMD_URL: str = 'https://steamcdn-a.akamaihd.net/client/installer/steamcmd.zip'

USERNAME: str = os.getlogin()

DEFAULT_WORKING_DIR: Path = Path.home().joinpath('Ark_Server_Manager')

WORKING_DIR: Path = Path.home().joinpath('Ark_Server_Manager')

STEAMCMD_EXE_PATH: Path = WORKING_DIR / 'Steam' / 'steamcmd.exe'

STEAMCMD_ZIP_PATH: Path = WORKING_DIR / 'Steam' / Path(STEAMCMD_URL).name

SERVER_NAME: str = ""

SERVER_PATH = WORKING_DIR / 'Ark_Servers' / SERVER_NAME

# ASA_INSTALL_COMMANDS = [
#     f"+force_install_dir \"{WORKING_DIR}\"",
#     "+login anonymous",
#     "+app_update 2430930 validate",
#     "+exit"
# ]

# ASA_INSTALL_COMMAND = f"+force_install_dir {WORKING_DIR} && +login anonymous && +app_update 2430930 validate && +exit"
