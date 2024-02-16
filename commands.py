from urllib.request import urlretrieve
from zipfile import ZipFile
import constants as c
import subprocess
import logging
from pathlib import Path

logging.basicConfig(format='%(asctime)s:%(name)s:%(levelname)s:%(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def download_from_url(url: str, filepath: Path):
    url: str = url
    filepath = filepath
    if filepath.is_file():
        logger.info('File has already been downloaded. Skipping Download.')
    else:
        Path.mkdir(filepath.parent, parents=True, exist_ok=True)
        logger.info("Starting SteamCMD Download")
        urlretrieve(url, filepath)
        logger.info("Download Complete")
    return


def unzip_file(path: Path):
    if c.STEAMCMD_EXE_PATH.is_file():
        logger.info("File has already been unzipped")
    else:
        logger.info("Unzipping downloaded file.")
        # loading the zip file and creating a zip object
        with ZipFile(path, 'r') as zObject:
            # Extracting all the members of the zip
            # into a specific location.
            zObject.extractall(path=path.parent)
        logger.info("Successfully unzipped file.")
    return


def run_steam_cmd():
    steam_user = 'anonymous'
    app_id = c.ASA_STEAM_ID
    steamcmd = c.STEAMCMD_EXE_PATH
    login = "+login " + steam_user
    server_path = c.SERVER_PATH.joinpath(c.SERVER_NAME)
    install_dir = str('+force_install_dir ' + str(server_path))
    app_update = "+app_update " + app_id

    if server_path.is_dir():
        logger.warning("Server has already been installed there."
                       "Please choose another location or server name to continue.")
    else:
        logger.info(f"Creating directory for server at {server_path}")
        Path.mkdir(server_path, parents=True)
        logger.info("Starting Server Install")
        proc = subprocess.run(
            [steamcmd, install_dir, login, app_update, "validate", "+quit"],
            capture_output=True, text=True)
        if proc.returncode == 0:
            logger.debug(str(proc.returncode))
            logger.debug(str(proc.stdout))
            logger.info(f"Ark Server have been installed at {server_path}")
        else:
            logger.debug(str(proc.returncode))
            logger.warning("SteamCMD ran into an error")
            logger.debug(str(proc.stderr))
    return
