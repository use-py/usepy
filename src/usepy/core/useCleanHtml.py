from html.parser import HTMLParser


class TagStripper(HTMLParser):
    def __init__(self, white_tags=None):
        super().__init__()
        self.white_tags = white_tags or []
        self.reset()
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
        return ''.join(self.fed)


def useCleanHtml(html: str, white_tags=None) -> str:
    """
    清除HTML标签
    >>> useCleanHtml('<p>This is a paragraph.</p><br><strong>This is bold text.</strong>')
    'This is a paragraph.This is bold text.'
    """
    ts = TagStripper(white_tags=white_tags)
    ts.feed(html)
    return ts.get_data()
