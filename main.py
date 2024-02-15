from pathlib import Path
import flet as ft
import commands
import constants as c


def main(page: ft.Page):
    page.title = "Ark Server Manager"

    def on_install_steamcmd(_):
        c.SERVER_NAME = str(server_name_field.value)
        c.WORKING_DIR = Path(server_path_field.value)
        commands.download_from_url(c.STEAMCMD_URL, c.STEAMCMD_ZIP_PATH)
        commands.unzip_file(c.STEAMCMD_ZIP_PATH)
        commands.run_steam_cmd()

    server_path_field = ft.TextField(label="Server Location",
                                     expand=True,
                                     value=str(c.DEFAULT_WORKING_DIR))
    install_steamcmd_button = ft.TextButton(text="Install",
                                            on_click=on_install_steamcmd)
    server_name_field = ft.TextField(label="Server Name")
    page.add(ft.Row([
        server_path_field,
        install_steamcmd_button
    ]),
        ft.Row([
            server_name_field
        ])
    )


ft.app(target=main)
