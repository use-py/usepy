def main():
    rds = Redis(host='localhost', port=6379, db=0)
    bf = useBloomFilter(
        client=rds
    )
    bf.add('hello')
    bf.add('world')
    print(bf.exists('hello'))
    print(bf.exists('world'))
    print(bf.exists('python'))
    print(bf.exists(''))


if __name__ == '__main__':
    from redis import Redis
    from usepy import useBloomFilter

    main()
