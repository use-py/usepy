from usepy import useParser, useCURL

if __name__ == '__main__':
    test_curl_command = """
    your curl command
    """
    # curl = useParser.curl(test_curl_command)
    curl = useCURL(test_curl_command)
    print(curl.url)
    print(curl.method)
    print(curl.data, type(curl.data))
    print(curl.headers)
    print(curl.cookies)
