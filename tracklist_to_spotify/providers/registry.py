import enum
from tracklist_to_spotify.providers import one_thousand_one_tracklists, trackid

class Providers(enum.Enum):
    trackid = "trackid"
    one_thousand_one_tracklists = "1001tracklists"

PROVIDERS_REGISTRY = {
    Providers.trackid: trackid.get,
    Providers.one_thousand_one_tracklists: one_thousand_one_tracklists.get,
}
