from tempfile import NamedTemporaryFile

from loguru import logger

from tracklist_to_spotify.downloaders.spotdl.run import SpotDL


def download(playlist: str):
    logger.info(f"Downloading Spotify playlist {playlist} using spotdl...")
    spotdl = SpotDL()
    spotdl.download(playlist)
