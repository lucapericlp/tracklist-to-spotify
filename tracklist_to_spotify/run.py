from typing import Optional
import os
from loguru import logger
import tyro

from tracklist_to_spotify.providers.registry import PROVIDERS_REGISTRY
from tracklist_to_spotify.publishers.registry import PUBLISHERS_REGISTRY
from tracklist_to_spotify.publishers.spotify_import import publish as spotify_publish
from tracklist_to_spotify.providers.trackid import get as trackid_get


def run(
    resource_id: str,
    username: str,
    playlist: str,
    provider: str = "trackid",
    publisher: str = "spotify_import",
):
    provider_get = PROVIDERS_REGISTRY.get(provider)
    if provider_get is None:
        logger.error(f"Provider {provider} not found!")
        exit(1)
    publisher_publish = PUBLISHERS_REGISTRY.get(publisher, spotify_publish)
    if publisher_publish is None:
        logger.error(f"Publisher {publisher} not found!")
        exit(1)
    tracklist = provider_get(resource_id)
    publisher_publish(tracklist, username, playlist)


def main():
    tyro.cli(run)


if __name__ == "__main__":
    main()
