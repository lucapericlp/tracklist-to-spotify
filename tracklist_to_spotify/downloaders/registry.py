import enum
from tracklist_to_spotify.downloaders import spotdl

class Downloaders(enum.Enum):
    spotdl = "spotdl"

DOWNLOADERS_REGISTRY = {
    Downloaders.spotdl: spotdl.download
}
