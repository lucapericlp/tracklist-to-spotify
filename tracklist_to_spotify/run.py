from loguru import logger
import tyro

from tracklist_to_spotify.providers.registry import PROVIDERS_REGISTRY, Providers
from tracklist_to_spotify.publishers.registry import PUBLISHERS_REGISTRY, Publishers

def run(
    resource: str,
    username: str,
    playlist: str,
    provider: Providers = Providers.trackid,
    publisher: Publishers = Publishers.spotify,
):
    provider_get = PROVIDERS_REGISTRY[provider]
    publisher_publish = PUBLISHERS_REGISTRY[publisher]
    tracklist = provider_get(resource)
    publisher_publish(tracklist, username, playlist)
    logger.info("Completed!")


def main():
    tyro.cli(run)


if __name__ == "__main__":
    main()
