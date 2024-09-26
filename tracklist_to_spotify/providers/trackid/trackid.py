import httpx
from loguru import logger
from tenacity import retry

from tracklist_to_spotify.providers.trackid.types import Response as TrackIdResult
from tracklist_to_spotify.publishers.types import GenericTrackDetails

HOST_URI = "https://trackid.net:8001/api/public/audiostreams/"


@retry(
    stop=(lambda attempt: attempt >= 5),
    wait=(lambda attempt: 2 ** attempt),
    reraise=True,
)
def fetch_result(resource: str) -> TrackIdResult:
    response = httpx.get(HOST_URI + resource)
    return response.json()


def extract_tracklist(result: TrackIdResult) -> list[GenericTrackDetails]:
    if "result" not in result:
        logger.error(f"Failed to get a tracklist from `trackid.net`! Did you provide a valid resource ID?")
        exit(1)
    return [
        {"artist": track["artist"], "title": track["title"]}
        for detection_process in result["result"]["detectionProcesses"]
        for track in detection_process["detectionProcessMusicTracks"]
    ]


def maybe_extract_resource_id(resource_id: str) -> str:
    if resource_id.startswith(("https://trackid.net", "http://trackid.net", "trackid.net")):
        return resource_id.split("/")[-1]
    return resource_id


def get(resource_id: str) -> list[GenericTrackDetails]:
    logger.info(f"Fetching tracklist for resource {resource_id}")
    resource_id = maybe_extract_resource_id(resource_id)
    result = fetch_result(resource_id)
    logger.info("Extracting...")
    tracklist = extract_tracklist(result)
    logger.info(f"Extracted {len(tracklist)} tracks for {resource_id}")
    return tracklist
