from html.parser import HTMLParser
from contextlib import contextmanager


class TagStripper(HTMLParser):
    def __init__(self, white_tags=None):
        super().__init__()
        self.white_tags = [tag.lower() for tag in white_tags] if white_tags else []
        self.fed = []

    def handle_data(self, d):
        self.fed.append(d)

    def handle_starttag(self, tag, attrs):
        if tag in self.white_tags:
            self.fed.append(f"<{tag}>")

    def handle_endtag(self, tag):
        if tag in self.white_tags:
            self.fed.append(f"</{tag}>")

    def get_data(self):
        return "".join(self.fed)

    def close(self) -> None:
        super().close()
        self.fed.clear()


def useCleanHtml(html: str, white_tags=None) -> str:
    """
    清除HTML标签
    >>> useCleanHtml('<p>This is a paragraph.</p><br><strong>This is bold text.</strong>')
    'This is a paragraph.This is bold text.'
    """
    ts = TagStripper(white_tags=white_tags)
    ts.feed(html)
    data = ts.get_data()
    ts.close()
    return data


@contextmanager
def cleanHtml(html: str, white_tags=None) -> TagStripper:
    ts = TagStripper(white_tags)
    ts.feed(html)
    try:
        yield ts
    finally:
        ts.close()
