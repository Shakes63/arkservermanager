import unittest
from pathlib import Path
from servers import Server
import constants


class TestServer(unittest.TestCase):
    def setUp(self) -> None:
        self.server = Server(
            server_name="Test Server",
            server_port=7777,
            server_password="password",
            app_id="2430930",
            map="TheIsland",
            server_admin_password="password",
            UseBattleEye=False,
            ServerCrosshair=True,
            ShowMapPlayerLocation=True,
            AllowThirdPersonPlayer=True,
            TheMaxStructuresInRange=1000,
            ActiveMods=["Mod1", "Mod2"],
            ActiveMapMod="Mod3",
        )

    def test_server_name(self):
        self.assertEqual(self.server.server_name, "Test Server")

    def test_server_port(self):
        self.assertEqual(self.server.server_port, 7777)

    def test_server_password(self):
        self.assertEqual(self.server.server_password, "password")

    def test_app_id(self):
        self.assertEqual(self.server.app_id, "2430930")

    def test_map(self):
        self.assertEqual(self.server.map, "TheIsland")

    def test_server_admin_password(self):
        self.assertEqual(self.server.server_admin_password, "password")

    def test_use_battle_eye(self):
        self.assertEqual(self.server.UseBattleEye, False)

    def test_server_crosshair(self):
        self.assertEqual(self.server.ServerCrosshair, True)

    def test_show_map_player_location(self):
        self.assertEqual(self.server.ShowMapPlayerLocation, True)

    def test_allow_third_person_player(self):
        self.assertEqual(self.server.AllowThirdPersonPlayer, True)

    def test_the_max_structures_in_range(self):
        self.assertEqual(self.server.TheMaxStructuresInRange, 1000)

    def test_active_mods(self):
        self.assertEqual(self.server.ActiveMods, ["Mod1", "Mod2"])

    def test_active_map_mod(self):
        self.assertEqual(self.server.ActiveMapMod, "Mod3")

    def test_server_directory(self):
        self.assertEqual(self.server.server_directory,
                         Path(f"{constants.WORKING_DIR}\\Ark_Servers\\{self.server.server_name}"))

    def test_server_binary_path(self):
        self.assertEqual(
            self.server.server_binary_path,
            self.server.server_directory.joinpath("ShooterGame\\Binaries\\Win64\\ArkAscendedServer.exe"),
        )

    def test_game_user_settings_path(self):
        self.assertEqual(
            self.server.game_user_settings_path,
            self.server.server_directory.joinpath("ShooterGame\\Saved\\Config\\WindowsServer\\GameUserSettings.ini"),
        )


if __name__ == "__main__":
    unittest.main()
