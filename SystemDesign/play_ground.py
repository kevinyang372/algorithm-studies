import concurrent.futures
import time
import collections
from itertools import chain
import random

class HTMLParser:
    def __init__(self):
        self.d = {
            'google.com': ['google.com/topics', 'google.com/maps', 'google.com/search'],
            'google.com/topics': ['google.com/topics/a', 'google.com/topics/b', 'google.com/topics/c'],
            'google.com/search': ['google.com/search/a', 'google.com/search/b']
        }

    def getUrls(self, url):
        print(f"Waiting for {url}")
        time.sleep(3)
        return self.d.get(url, [])


def crawl(parser, start_url):
    explored = set([start_url])
    queue = collections.deque([start_url])

    while queue:
        temp_queue = []
        with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor: 
            result = chain(*executor.map(parser.getUrls, queue))

        temp_queue = [node for node in result if node not in explored]
        explored.update(temp_queue)
        queue = temp_queue

    return explored


if __name__ == "__main__":
    parser = HTMLParser()

    print(crawl(parser, 'google.com'))
