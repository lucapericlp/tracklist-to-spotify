import json
from pathlib import Path
from tracklist_to_spotify.providers.trackid.trackid import get

def test_trackid_get(mocker):
    sample_response = Path("tests/providers/trackid/sample_response.json").read_text()
    mock = mocker.Mock(json=lambda: json.loads(sample_response))
    mocker.patch(
        "httpx.get",
        return_value=mock
    )

    result = get("fake_resource_id")
    assert len(result) == 30
