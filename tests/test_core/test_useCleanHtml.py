import pytest

from usepy import useCleanHtml
from usepy.core.useCleanHtml import TagStripper


def test_clean_html():
    test_html = """<div class="test"><p>test</p></div>"""
    assert useCleanHtml(test_html) == "test"
    test_html2 = """<div class="test"><p>test</p><p>test2</p></div>"""
    assert useCleanHtml(test_html2, white_tags=["p"]) == "<p>test</p><p>test2</p>"


@pytest.fixture
def tag_stripper():
    html_text = "<h1>Title</h1>"
    white_tags = ['h1']
    ts = TagStripper(white_tags)
    ts.feed(html_text)
    yield ts
    ts.close()


def test_close_method(tag_stripper):
    extracted_data = tag_stripper.get_data()
    assert extracted_data == "<h1>Title</h1>"
    tag_stripper.close()
    assert tag_stripper.get_data() == ""
