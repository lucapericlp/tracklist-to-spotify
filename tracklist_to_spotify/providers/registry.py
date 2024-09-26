from tracklist_to_spotify.providers import trackid

PROVIDERS_REGISTRY = {
    "trackid": trackid.get
}
