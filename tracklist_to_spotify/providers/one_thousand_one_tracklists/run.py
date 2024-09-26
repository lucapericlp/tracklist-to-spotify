import re
from typing import List
import httpx
from bs4 import BeautifulSoup
from loguru import logger
from tenacity import retry

from tracklist_to_spotify.publishers.types import GenericTrackDetails


def extract_meta_names_regex(html_content):
    pattern = r'<meta itemprop="name" content="([^"]*)"'
    matches = re.findall(pattern, html_content)
    return matches


def extract_meta_names_bs4(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')

    meta_names = []

    music_recording_divs = soup.find_all('div', itemtype="http://schema.org/MusicRecording")

    for div in music_recording_divs:
        meta_tags = div.find_all('meta', itemprop="name")
        for meta in meta_tags:
            if 'content' in meta.attrs:
                meta_names.append(meta['content'])

    return meta_names


@retry(
    stop=(lambda attempt: attempt >= 5),
    wait=(lambda attempt: 2 ** attempt),
    reraise=True
)
def get_page(url: str):
    # NOTE: headers are used to avoid captcha'd
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'cache-control': 'no-cache',
        'pragma': 'no-cache',
        'cookie': 'guid=ffb6e76e3ad18',
        'priority': 'u=0, i',
        'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'
    }

    logger.info(f"Fetching page: {url}")
    response = httpx.get(url, headers=headers)
    response.raise_for_status()

    return response.text


def get(url: str) -> List[GenericTrackDetails]:
    html_content = get_page(url)
    meta_names = extract_meta_names_bs4(html_content)
    if len(meta_names) == 0:
        logger.error(f"Failed to extract any tracks from {url}!")
        exit(1)
    logger.info(f"Extracted {len(meta_names)} tracks from {url}")
    # NOTE: this is an implicit contract with the publisher `spotify-import` since we're
    # assuming that there is no special logic related to combining these two fields
    return [{"artist": " ", "title": track} for track in meta_names]
