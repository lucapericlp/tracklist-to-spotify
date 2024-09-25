import os
from tempfile import NamedTemporaryFile

import pandas as pd

from tracklist_to_spotify.publishers.spotify_import.run import SpotifyImport
from tracklist_to_spotify.publishers.spotify_import.types import TrackDetails


def get_import_destination_details():
    return {
        "username": os.environ["SPOTIFY_USERNAME"],
        "playlist": os.environ["SPOTIFY_PLAYLIST"]
    }


def publish(tracks: list[TrackDetails]):
    args = get_import_destination_details()
    with NamedTemporaryFile("w", suffix=".csv") as f:
        pd.DataFrame(tracks).to_csv(f)
        f.flush()
        spotify_import = SpotifyImport(args["username"], "playlist", f.name, args["playlist"])
        spotify_import.run()
