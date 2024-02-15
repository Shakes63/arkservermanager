from urllib.request import urlretrieve
from zipfile import ZipFile
import constants as c
import subprocess
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO)


def download_from_url(url: str, filepath: Path):
    url: str = url
    filepath = filepath
    if filepath.is_file():
        logging.info('File has already been downloaded. Skipping Download.')
    else:
        Path.mkdir(filepath.parent, parents=True, exist_ok=True)
        logging.info("Starting SteamCMD Download")
        urlretrieve(url, filepath)
        logging.info("Download Complete")
    return


def unzip_file(path: Path):
    if c.STEAMCMD_EXE_PATH.is_file():
        logging.info("File has already been unzipped")
    else:
        logging.info("Unzipping downloaded file.")
        # loading the zip file and creating a zip object
        with ZipFile(path, 'r') as zObject:
            # Extracting all the members of the zip
            # into a specific location.
            zObject.extractall(path=path.parent)
        logging.info("Successfully unzipped file.")
    return


def run_steam_cmd():
    steam_user = 'anonymous'
    app_id = c.ASA_STEAM_ID  # Eg Skyrim Special edition is 489830
    steamcmd = c.STEAMCMD_EXE_PATH
    login = "+login " + steam_user
    install_dir = str('+force_install_dir ' + str(c.SERVER_PATH))
    app_update = "+app_update " + app_id

    if c.SERVER_PATH.is_dir():
        logging.info("Server has already been installed there."
                     "Please choose another location or server name to continue.")
    else:
        logging.info(f"Creating directory for server at {c.SERVER_PATH}")
        Path.mkdir(c.SERVER_PATH, parents=True)
        logging.info("Starting SteamCMD Install")
        subprocess.call(
            [steamcmd, "+@sSteamCmdForcePlatformTypewindows", login, install_dir, app_update, "validate", "+quit"])
        logging.info(f"SteamCMD has been installed at {c.WORKING_DIR} and "
                     f"Ark Server have been installed at {c.SERVER_PATH}")
    return
