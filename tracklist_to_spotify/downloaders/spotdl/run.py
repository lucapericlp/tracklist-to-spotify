from typing import List

from dotenv import load_dotenv, dotenv_values
from loguru import logger
from spotipy import SpotifyOAuth
from spotdl import Spotdl
import spotipy


def scoped(scopes: List[str]):
    return ' '.join(scopes)

class SpotDL:

    def __init__(self):
        load_dotenv()
        envs = dotenv_values()
        scope = scoped(['playlist-read-private'])
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, open_browser=False))
        self.spotdl = Spotdl(client_id=envs['SPOTIPY_CLIENT_ID'], client_secret=envs['SPOTIPY_CLIENT_SECRET'])


    def _search_user_playlist_by_name(self, name_to_search):
        batch_size = 50
        offset = 0
        playlist = []
        while True:
            response = self.sp.current_user_playlists(limit=batch_size, offset=offset)
            if not response['next'] or not response['items']:
                break
            playlists = response['items']
            playlist.append([p for p in playlists if p['name'] == name_to_search])
            playlist = playlist[0] if playlist else None
            offset += batch_size
        return playlist

    def _get_playlist_url_from_name(self, playlist_name):
        playlist = self._search_user_playlist_by_name(playlist_name)
        return playlist['external_urls']['spotify']

    def download(self, playlist) -> int:
        songs_downloaded = 0
        try:
            url = self._get_playlist_url_from_name(playlist)
            logger.info(f"Downloading Spotify playlist: {url}")
            songs = self.spotdl.search([url])
            results = self.spotdl.download_songs(songs)
            songs_downloaded = len(results)
            logger.info(f"Download complete. Have fun mixing!")
        except Exception as e:
            logger.error(f"Error downloading Spotify playlist: {e}")
        return songs_downloaded