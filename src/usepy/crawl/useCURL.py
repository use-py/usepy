"""

curl 'http://testing.baidu.com:9090/api/user/profile' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'Accept-Language: zh-cn' \
  -H 'Authorization: 0a96d4f1-375b-4846-85a2-5731a1a2b3ac' \
  -H 'Cache-Control: no-cache' \
  -H 'Connection: keep-alive' \
  -H 'Origin: http://localhost:4000' \
  -H 'Pragma: no-cache' \
  -H 'Referer: http://localhost:4000/' \
  -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.76' \
  --compressed \
  --insecure

"""
import argparse
import re
import shlex
from collections import OrderedDict
from typing import Optional, Dict, Generator, Tuple

from usepy import useCookieToDict


def normalize_newlines(multiline_text):
    return multiline_text.replace(" \\\n", " ").replace("^", "")


class useCURL:

    def __init__(self, curl_command):
        tokens = shlex.split(normalize_newlines(curl_command))
        self.args = self._parse_args(tokens)

    @staticmethod
    def _parse_args(tokens):
        parser = argparse.ArgumentParser()
        parser.add_argument('command')
        parser.add_argument('url')
        parser.add_argument('-d', '--data')
        parser.add_argument('-b', '--data-binary', '--data-raw', default=None)
        parser.add_argument('-X', default='')
        parser.add_argument('-H', '--header', action='append', default=[])
        parser.add_argument('--compressed', action='store_true')
        parser.add_argument('-k', '--insecure', action='store_true')
        parser.add_argument('--user', '-u', default=())
        parser.add_argument('-i', '--include', action='store_true')
        parser.add_argument('-s', '--silent', action='store_true')
        return parser.parse_args(tokens)

    @property
    def url(self) -> str:
        return self.args.url

    @property
    def method(self) -> str:
        _method = self.args.X.lower() if self.args.X else ('post' if self.data else 'get')
        return _method.upper()

    @property
    def data(self) -> Optional[str]:
        return self.args.data or self.args.data_binary

    @property
    def auth(self) -> Optional[tuple]:
        if self.args.user:
            return tuple(self.args.user.split(':'))
        return None

    @property
    def verify(self) -> bool:
        return self.args.insecure

    @property
    def compressed(self) -> bool:
        return self.args.compressed

    def _get_headers_kv(self) -> Generator[Tuple[str, str], None, None]:
        for header in self.args.header:
            if header.startswith(':'):
                occurrence = [m.start() for m in re.finditer(':', header)]
                key, value = header[:occurrence[1]], header[occurrence[1] + 1:]
            else:
                key, value = header.split(":", 1)
            yield key, value.strip()

    @property
    def headers(self) -> Optional[Dict]:
        _headers = OrderedDict()
        for key, value in self._get_headers_kv():
            # skip cookie
            if key.lower().strip("$") == 'cookie':
                continue
            _headers[key] = value
        return dict(_headers) if _headers else None

    @property
    def cookies(self) -> Optional[Dict]:
        for key, value in self._get_headers_kv():
            if key.lower().strip("$") == 'cookie':
                return useCookieToDict(value)
        return None
