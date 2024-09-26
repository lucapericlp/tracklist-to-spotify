from tempfile import NamedTemporaryFile

from loguru import logger
import pandas as pd

from tracklist_to_spotify.publishers.spotify_import.run import SpotifyImport
from tracklist_to_spotify.publishers.spotify_import.types import TrackDetails


def publish(tracks: list[TrackDetails], username: str, playlist: str):
    logger.info(f"Publishing {len(tracks)} tracks to Spotify playlist {playlist} for user {username}")
    with NamedTemporaryFile("w", suffix=".csv") as f:
        pd.DataFrame(tracks).to_csv(f)
        f.flush()
        spotify_import = SpotifyImport(username, "playlist", f.name, playlist)
        spotify_import.run()
