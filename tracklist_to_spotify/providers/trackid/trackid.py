import httpx
from loguru import logger

from tracklist_to_spotify.providers.trackid.types import Response as TrackIdResult
from tracklist_to_spotify.publishers.types import GenericTrackDetails

HOST_URI = "https://trackid.net:8001/api/public/audiostreams/"


def fetch_result(resource: str) -> TrackIdResult:
    response = httpx.get(HOST_URI + resource)
    return response.json()


def extract_tracklist(result: TrackIdResult) -> list[GenericTrackDetails]:
    return [
        {"artist": track["artist"], "title": track["title"]}
        for detection_process in result["result"]["detectionProcesses"]
        for track in detection_process["detectionProcessMusicTracks"]
    ]


def get(resource_id: str) -> list[GenericTrackDetails]:
    logger.info(f"Fetching tracklist for resource {resource_id}")
    result = fetch_result(resource_id)
    logger.info("Extracting...")
    tracklist = extract_tracklist(result)
    logger.info(f"Extracted {len(tracklist)} tracks for {resource_id}")
    return tracklist
