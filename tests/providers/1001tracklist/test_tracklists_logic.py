from pathlib import Path

from tracklist_to_spotify.providers.one_thousand_one_tracklists.run import extract_meta_names_bs4
from tracklist_to_spotify.providers.one_thousand_one_tracklists.run import extract_meta_names_regex


def test_html_extraction_regex():
    matches = extract_meta_names_regex(Path("tests/providers/1001tracklist/sample_response.html").read_text())
    assert len(matches) == 19

def test_html_extraction_bs4():
    matches = extract_meta_names_bs4(Path("tests/providers/1001tracklist/sample_response.html").read_text())
    assert len(matches) == 15
