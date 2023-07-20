from urllib import parse


class useURL:
    """

    from usepy import useURL

    url = useURL("https://www.google.com/search?q=usepy&ie=utf-8")

    | url.scheme | url.query | url.query_dict | url.path |
    |------------|-----------|----------------|----------|
    | https      | q=usepy&ie=utf-8 | {'q': 'usepy', 'ie': 'utf-8'} | /search |

    url = useURL("https://www.google.com/search?s=usepy&s=usepy2&ie=utf-8")

    | url.scheme | url.netloc | url.query_dict | url.path |
    |------------|-----------|----------------|----------|
    | https      | www.google.com | {'s': ['usepy', 'usepy2'], 'ie': 'utf-8'} | /search |

    """
    __slots__ = ('_url', '_parsed', 'query', 'path', 'scheme',
                 'netloc', 'params', 'fragment', 'username', 'password',
                 'hostname', 'port')

    def __init__(self, url):
        self._url = url
        self._parsed = parse.urlparse(url)

    def __getattr__(self, item):
        return getattr(self._parsed, item)

    @property
    def query_dict(self) -> dict:
        """
        获取query参数，返回字典
        :return: dict
        """
        qs = parse.parse_qs(self.query)
        return {k: v[0] if len(v) == 1 else v for k, v in qs.items()}

    @property
    def decode(self) -> str:
        """
        解码url
        :return: str
        """
        return parse.unquote(self._url)
