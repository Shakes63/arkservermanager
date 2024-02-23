from pathlib import Path
import commands
import constants as c
from servers import Server

import flet as ft


def main(page: ft.Page):
    page.title = "Ark Server Manager"

    def close_banner(_):
        page.banner.open = False
        page.update()

    page.banner = ft.Banner(
        bgcolor=ft.colors.AMBER_100,
        leading=ft.Icon(ft.icons.WARNING_AMBER_ROUNDED, color=ft.colors.AMBER, size=40),
        content=ft.Text(
            ""
        ),
        actions=[
            ft.TextButton("OK", on_click=close_banner)
        ],
    )

    def on_install_steamcmd(_):
        c.working_dir = Path(server_path_field.value)
        if c.STEAMCMD_EXE_PATH.is_file():
            page.banner.content = ft.Text(value="SteamCMD already installed.", color=ft.colors.BLACK)
            page.banner.open = True
            page.update()
            return
        commands.download_from_url(c.STEAMCMD_URL, c.STEAMCMD_ZIP_PATH)
        commands.unzip_file(c.STEAMCMD_ZIP_PATH)

    def on_start_server(_):
        server: Server = Server(server_name=server_name_field.value, server_port=int(server_port_field.value))
        if server.server_directory.is_dir():
            server.start()
        else:
            server.install()
            server.start()

    server_path_field = ft.TextField(label="Server Location",
                                     expand=True,
                                     value=str(c.DEFAULT_WORKING_DIR))
    install_steamcmd_button = ft.TextButton(text="Install",
                                            on_click=on_install_steamcmd)
    server_name_field = ft.TextField(label="Server Name")

    server_start_button = ft.IconButton(icon=ft.icons.START,
                                        on_click=on_start_server,
                                        tooltip="Install and Start Server")

    server_port_field = ft.TextField(label="Port", hint_text='27019')

    page.add(ft.Row([
        server_path_field,
        install_steamcmd_button
    ]),
        ft.Row([
            server_name_field,
            server_port_field,
            server_start_button
        ])
    )


if __name__ == "__main__":
    ft.app(target=main)
