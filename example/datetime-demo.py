import calendar

from usepy import useDateTime

if __name__ == '__main__':
    # print(useDateTime.now())
    # print(useDateTime.last(useDateTime.now(), 'month'))
    # print(useDateTime.last(useDateTime.now(), 'today'))
    # print(useDateTime.last(useDateTime.now(), 'year'))
    print(useDateTime.last(useDateTime.now(), 'hour'))
    print(useDateTime.last(useDateTime.now(), 'minute'))
    print(useDateTime.first(useDateTime.now(), 'today'))
    print(useDateTime.format_before(90, 'days'))
