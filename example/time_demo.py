from datetime import datetime

from usepy.time import useTime

assert useTime.parse('2020-01-01 00:00:00') == datetime(2020, 1, 1, 0, 0)
