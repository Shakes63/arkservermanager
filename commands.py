from urllib.request import urlretrieve
from zipfile import ZipFile
import constants as c
import subprocess
import logging
from pathlib import Path
import configparser
from servers import Server

logging.basicConfig(format='%(asctime)s:%(name)s:%(levelname)s:%(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p',
                    filename="ASM.log")
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def download_from_url(url: str, filepath: Path):
    url: str = url
    filepath: Path = filepath
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


def run_steam_cmd(server: Server):
    steamcmd = c.STEAMCMD_EXE_PATH
    install_dir = str('+force_install_dir ' + str(server.server_directory))
    app_update = "+app_update " + server.app_id

    if server.server_directory.is_dir():
        logger.warning("Server has already been installed there."
                       "Please choose another location or server name to continue.")
    else:
        logger.info(f"Creating directory for server at {server.server_directory}")
        Path.mkdir(server.server_directory, parents=True)
        logger.info("Starting Server Install")
        proc = subprocess.run(
            [steamcmd, install_dir, "+login anonymous", app_update, "validate", "+quit"],
            capture_output=True, text=True)
        if proc.returncode == 7:
            logger.debug(f"Steamcmd return code: {proc.returncode}")
            logger.debug(str(proc.stdout))
            logger.info(f"Ark Server have been installed at {server.server_directory}")
        else:
            logger.debug(f"Steamcmd return code: {proc.returncode}")
            logger.warning("SteamCMD ran into an error")
            logger.debug(str(proc.stderr))
    return


def start_server(server: Server):
    logger.info(f"Ark Server {server.server_name} Starting up. This may take a while.")
    proc = subprocess.run([server.server_binary_path,
                           "TheIsland?ServerCrosshair=true?ShowMapPlayerLocation=true=AllowThirdPersonPlayer=true?TheMaxStructuresInRange=1000",
                           "-NoBattlEye"])
    logger.info(f"Ark Server return code: {proc.returncode}")
