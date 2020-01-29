from gevent import monkey;monkey.patch_all()
from gevent.pool import Pool
import gevent
import time
import requests


def get_url(url):
    print("GET :", url)
    response = requests.get(url)
    if response.status_codes == 200:
        print("%d bytes received from %s" % (len(response.text), url))


def main(pools=2):

    start_time = time.time()

    pool = Pool(pools)
    for i in range(pools):
        pool.spawn(get_url, 'https://www.baidu.com')

    gevent.joinall(pool)
    end_time = time.time()
    print(end_time - start_time)


if __name__ == '__main__':
    main()
