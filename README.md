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

### via clone
```
git clone https://github.com/lucapericlp/tracklist-to-spotify.git && cd tracklist-to-spotify
uv sync
uv run import_tracklist --resource_id https://trackid.net/audiostreams/artmann-verknipt-festival-2022 --username lucaperic.lp --playlist "Artmann Verknipt Festival 2022"
```

