from usepy import useHeaderToDict


def test_header_to_dict():
    header_str = """sec-ch-ua: "Not?A_Brand";v="8", "Chromium";v="108", "Microsoft Edge";v="108"
    sec-ch-ua-platform: "macOS"
    user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"""
    assert useHeaderToDict(header_str) == {
        "sec-ch-ua": '"Not?A_Brand";v="8", "Chromium";v="108", "Microsoft Edge";v="108"',
        "sec-ch-ua-platform": '"macOS"',
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
    }
