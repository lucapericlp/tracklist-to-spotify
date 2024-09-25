import tyro

from tracklist_to_spotify.publishers.spotify_import import publish as spotify_publish
from tracklist_to_spotify.providers.trackid import get as trackid_get


def run(resource_id: str):
    tracklist = trackid_get(resource_id)
    spotify_publish(tracklist)

if __name__ == "__main__":
    tyro.cli(run)
