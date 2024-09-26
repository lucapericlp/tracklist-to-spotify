import enum
from tracklist_to_spotify.publishers.spotify_import import publish

class Publishers(enum.Enum):
    spotify = "spotify_import"

PUBLISHERS_REGISTRY = {
    Publishers.spotify: publish
}
