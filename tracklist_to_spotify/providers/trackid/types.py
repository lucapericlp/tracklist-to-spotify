from typing import TypedDict, List, Optional
from datetime import datetime

class Style(TypedDict):
    id: int
    name: str
    audioStreamCount: Optional[int]

class AccountMusicTrack(TypedDict):
    pass

class DetectionProcessMusicTrack(TypedDict):
    id: int
    musicTrackId: int
    startTime: str
    endTime: str
    artist: str
    title: str
    label: Optional[str]
    labelSlug: Optional[str]
    slug: str
    referenceCount: int
    isNew: bool
    accountMusicTrack: Optional[AccountMusicTrack]

class DetectionProcess(TypedDict):
    id: int
    startDate: str
    endDate: str
    isReprocessing: bool
    detectionProcessMusicTracks: List[DetectionProcessMusicTrack]

class AudioStreamReprocess(TypedDict):
    id: int
    addedOn: str
    detectionProcessId: int

class Result(TypedDict):
    id: int
    url: str
    slug: str
    audioStreamType: int
    externalId: str
    artworkUrl: str
    title: str
    channel: str
    duration: str
    createdOn: str
    addedOn: str
    addedBy: str
    addedById: int
    favouriteCount: int
    likeCount: int
    averageRating: Optional[float]
    processingPriority: int
    favouriteDate: Optional[str]
    styles: List[Style]
    status: int
    detectionProcesses: List[DetectionProcess]
    amendments: List[dict]  # This is an empty list in the provided JSON
    audioStreamReprocesses: List[AudioStreamReprocess]
    accountAudiostream: Optional[dict]  # This is null in the provided JSON
    canReprocess: bool

class Response(TypedDict):
    result: Result
