from tracklist_to_spotify.publishers.spotify_import import publish


PUBLISHERS_REGISTRY = {
    "spotify_import": publish
}
