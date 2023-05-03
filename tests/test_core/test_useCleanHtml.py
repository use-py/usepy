from usepy import useCleanHtml


def test_clean_html():
    test_html = """<div class="test"><p>test</p></div>"""
    assert useCleanHtml(test_html) == "test"
    test_html2 = """<div class="test"><p>test</p><p>test2</p></div>"""
    assert useCleanHtml(test_html2, white_tags=["p"]) == "<p>test</p><p>test2</p>"
