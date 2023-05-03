from usepy import useCURL


def test_curl():
    test_curl_command = """
        curl 'https://www.baidu.com/' \
          -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9' \
          -H 'Accept-Language: zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6' \
          -H 'Cache-Control: no-cache' \
          -H 'Connection: keep-alive' \
          -H 'Cookie: BIDUPSID=xxxxxxxx' \
          -H 'Pragma: no-cache' \
          -H 'Referer: https://www.baidu.com/' \
          -H 'Sec-Fetch-Dest: document' \
          -H 'Sec-Fetch-Mode: navigate' \
          -H 'Sec-Fetch-Site: same-origin' \
          -H 'Sec-Fetch-User: ?1' \
          -H 'Upgrade-Insecure-Requests: 1' \
          -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.76' \
          -H 'sec-ch-ua: "Not?A_Brand";v="8", "Chromium";v="108", "Microsoft Edge";v="108"' \
          -H 'sec-ch-ua-mobile: ?0' \
          -H 'sec-ch-ua-platform: "macOS"' \
          --compressed
          """
    curl = useCURL(test_curl_command)
    assert curl.url == 'https://www.baidu.com/'
    assert curl.method == 'GET'
    assert not curl.data
    assert len(curl.headers.keys()) == 15
    assert len(curl.cookies.keys()) == 1
