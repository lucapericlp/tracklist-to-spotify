# Tracklist to Spotify
Supported tracklist providers:
1. trackid.net

## Usage
### Setup Spotify API
1. Create a Spotify Developer account
2. Create a new app
3. Copy the client id and client secret
4. `mv env.sample .env`
5. Fill in the client id and client secret in the .env file
6. Ensure the redirect URI in Spotify app dashboard is set to `http://localhost:8080`

### via pipx
You must have [pipx installed](https://github.com/pypa/pipx?tab=readme-ov-file#install-pipx).

```bash
export SPOTIPY_CLIENT_ID=your_client_id
export SPOTIPY_CLIENT_SECRET=your_client_secret
export SPOTIPY_REDIRECT_URI=http://localhost:8080/
pipx install git+https://github.com/lucapericlp/tracklist-to-spotify.git
pipx run \
    import_tracklist \
    --resource_id "https://trackid.net/audiostreams/estella-boersma-stone-techno-2024-arte-concert" \
    --username <spotify_username> \
    --playlist "Estella Boersma - Stone Techno 2024 - ARTE Concert"
```

### via clone
```
git clone https://github.com/lucapericlp/tracklist-to-spotify.git && cd tracklist-to-spotify
uv sync
uv run import_tracklist --resource_id https://trackid.net/audiostreams/artmann-verknipt-festival-2022 --username <username> --playlist "Artmann Verknipt Festival 2022"
```

