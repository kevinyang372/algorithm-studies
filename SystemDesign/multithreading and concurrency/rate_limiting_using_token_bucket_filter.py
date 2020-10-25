# Imagine you have a bucket that gets filled with tokens at the rate of 1 token per second. The bucket can hold a maximum of N tokens. Implement a thread-safe class that lets threads get a token when one is available. If no token is available, then the token-requesting threads should block.

# The class should expose an API called get_token() that various threads can call to get a token.

from threading import current_thread, Thread, Condition
import random
import time

class RateLimitFilter:

    def __init__(self, maximum_token):
        self.maximum_token = maximum_token
        self.current_token = 0
        self.c = Condition()

    def add_token(self):
        with self.c:
            if self.current_token < self.maximum_token:
                self.current_token += 1
                self.c.notify_all()

    def get_token(self):
        self.c.acquire()
        while self.current_token == 0:
            self.c.wait()
        self.current_token -= 1
        self.c.release()

def fill_token(rate_limiter):
    while True:
        rate_limiter.add_token()
        print(f"{current_thread().name} adds one token")
        time.sleep(1)

def take_token(rate_limiter):
    for _ in range(5):
        time.sleep(random.random() * 3)
        rate_limiter.get_token()
        print(f"{current_thread().name} gets one token")

if __name__ == "__main__":
    rate_limiter = RateLimitFilter(3)

    thread_1 = Thread(target=fill_token, args=(rate_limiter,))
    thread_1.daemon = True

    thread_1.start()

    thread_2 = Thread(target=take_token, args=(rate_limiter,))
    thread_3 = Thread(target=take_token, args=(rate_limiter,))
    thread_4 = Thread(target=take_token, args=(rate_limiter,))

    threads = [thread_2, thread_3, thread_4]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

