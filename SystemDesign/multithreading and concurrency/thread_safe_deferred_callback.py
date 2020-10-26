# Design and implement a thread-safe class that allows registration of callback methods that are executed after a user specified time interval in seconds has elapsed.

from threading import current_thread, Thread, Condition

import time
import heapq
import random

class ThreadSafeCallback:

    def __init__(self):
        self.queue = []
        self.condition = Condition()

    def add_func(self, func, t):
        with self.condition:
            heapq.heappush(self.queue, (time.time() + t, func))
            self.condition.notify_all()

    def start_queue(self):
        while True:
            self.condition.acquire()
            
            while not self.queue:
                self.condition.wait()

            while self.queue and time.time() < self.queue[0][0]:
                self.condition.wait(self.queue[0][0] - time.time())

            _, f = heapq.heappop(self.queue)
            f()
            self.condition.release()


def say_hello():
    print(f"{current_thread().name} says hello!")

def thread_test(thread_safe_callback):
    thread_safe_callback.add_func(say_hello, random.random() * 3)
    print(f"{current_thread().name} registered")

def start_main_thread(thread_safe_callback):
    thread_safe_callback.start_queue()

if __name__ == "__main__":
    thread_safe_callback = ThreadSafeCallback()

    main_thread = Thread(target=start_main_thread, args=(thread_safe_callback,))
    main_thread.daemon = True
    main_thread.start()

    thread_1 = Thread(target=thread_test, args=(thread_safe_callback,))
    thread_2 = Thread(target=thread_test, args=(thread_safe_callback,))
    thread_3 = Thread(target=thread_test, args=(thread_safe_callback,))

    threads = [thread_1, thread_2, thread_3]
    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    time.sleep(10)