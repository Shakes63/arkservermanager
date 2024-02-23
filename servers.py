from dataclasses import dataclass, field
from pathlib import Path
import constants


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
