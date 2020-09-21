#!/usr/bin/python

import threading
import time

# inherit from threading module
class Thread1(threading.Thread):
    def __init__(self, thread_id, name, counter):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.name = name
        self.counter = counter

    def run(self):
        print(f"Starting {self.name}")
        # acquire lock and make sure no other thread can interfere with data
        threadLock.acquire()
        for i in range(self.counter):
            print(f"Running {self.name}")
            time.sleep(1)
        # release lock after completing process
        threadLock.release()
        print(f"Exiting {self.name}")

class Thread2(threading.Thread):
    def __init__(self, thread_id, name, counter):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.name = name
        self.counter = counter

    def run(self):
        # check if thread is locked and immediately release it
        threadLock.acquire()
        threadLock.release()
        print(f"Starting {self.name}")
        for i in range(self.counter):
            print(f"Running {self.name}")
            time.sleep(1)
        print(f"Exiting {self.name}")


threadLock = threading.Lock()

thread1 = Thread1(1, "thread_1", 5)
thread2 = Thread2(2, "thread_2", 5)
thread3 = Thread2(3, "thread_3", 5)

thread1.start()
thread2.start()
thread3.start()