from urllib.request import urlretrieve
from zipfile import ZipFile
import constants
import logging
from pathlib import Path

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
    if constants.STEAMCMD_EXE_PATH.is_file():
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
