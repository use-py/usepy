def cookie_to_dict(cookies: str) -> dict:
    return {cookie.split('=')[0]: cookie.split('=')[-1] for cookie in cookies.split('; ')}


def headers_to_dict(headers: str) -> dict:
    header_dict = {}
    for line in headers.split('\n'):
        if ':' in line:
            key, value = line.split(':', 1)
            header_dict[key.strip()] = value.strip()
    return header_dict


def data_to_dict(data: str) -> dict:
    return {item.split('=')[0]: item.split('=')[-1] for item in data.split('&')}
