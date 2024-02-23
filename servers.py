from dataclasses import dataclass, field
from pathlib import Path
import constants
import logging
import subprocess

logging.basicConfig(format='%(asctime)s:%(name)s:%(levelname)s:%(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p',
                    filename="ASM.log")
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


@dataclass
class Server:
    server_name: str
    server_port: int
    server_password: str = ""
    app_id: str = "2430930"
    map: str = "TheIsland"
    server_admin_password: str = ""
    UseBattleEye: bool = field(default_factory=lambda: False)
    ServerCrosshair: bool = field(default_factory=lambda: True)
    ShowMapPlayerLocation: bool = field(default_factory=lambda: True)
    AllowThirdPersonPlayer: bool = field(default_factory=lambda: True)
    TheMaxStructuresInRange: int = field(default_factory=lambda: 1000)
    ActiveMods: list = field(default_factory=list)
    ActiveMapMod: str = ""

    @property
    def server_directory(self) -> Path:
        return Path(f"{constants.working_dir}\\Ark_Servers\\{self.server_name}")

    @property
    def server_binary_path(self) -> Path:
        return self.server_directory.joinpath("ShooterGame\\Binaries\\Win64\\ArkAscendedServer.exe")

    @property
    def game_user_settings_path(self) -> Path:
        return self.server_directory.joinpath("ShooterGame\\Saved\\Config\\WindowsServer\\GameUserSettings.ini")

    def start(self):
        logger.info(f"Ark Server {self.server_name} Starting up. This may take a while.")
        proc = subprocess.run([self.server_binary_path,
                               "TheIsland?ServerCrosshair=true?ShowMapPlayerLocation=true=AllowThirdPersonPlayer=true?TheMaxStructuresInRange=1000",
                               "-NoBattlEye"])
        logger.info(f"Ark Server return code: {proc.returncode}")
        logger.info(f"Ark Server {self.server_name} Started.")

    def install(self):
        install_dir = str('+force_install_dir ' + str(self.server_directory))
        app_update = "+app_update " + self.app_id

        if self.server_directory.is_dir():
            logger.warning("Server has already been installed there."
                           "Please choose another location or server name to continue.")
        else:
            logger.info(f"Creating directory for server at {self.server_directory}")
            Path.mkdir(self.server_directory, parents=True)
            logger.info("Starting Server Install")
            proc = subprocess.run(
                [constants.STEAMCMD_EXE_PATH, install_dir, "+login anonymous", app_update, "validate", "+quit"],
                capture_output=True, text=True)
            if proc.returncode == 7:
                logger.debug(f"Steamcmd return code: {proc.returncode}")
                logger.debug(str(proc.stdout))
                logger.info(f"Ark Server have been installed at {self.server_directory}")
            else:
                logger.debug(f"Steamcmd return code: {proc.returncode}")
                logger.warning("SteamCMD ran into an error")
                logger.debug(str(proc.stderr))
        return
