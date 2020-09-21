#!/usr/bin/python

import queue
import threading
import time

exit_flag = 0

class CustomThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def process_data(self):
        while not exit_flag:
            threadingLock.acquire()
            if not working_queue.empty():
                working_item = working_queue.get()
                threadingLock.release()
                print(f"Thread {self.name} working on {working_item}")
            else:
                threadingLock.release()
            time.sleep(1)

    def run(self):
        print(f"Starting {self.name}")
        self.process_data()
        print(f"Ending {self.name}")


thread_names = ["thread_1", "thread_2", "thread_3", "thread_4"]
data = ["fish", "meat", "mushroom", "potato", "tomato", "banana", "salt", "cabbage"]
working_queue = queue.Queue(10)
threadingLock = threading.Lock()
threads = []

# start threads
for thread_name in thread_names:
    temp_thread = CustomThread(thread_name)
    temp_thread.start()
    threads.append(temp_thread)

# ensure no interference with the data at insertion
threadingLock.acquire()
for item in data:
    working_queue.put(item)
threadingLock.release()

while not working_queue.empty():
    pass

exit_flag = 1

for thread in threads:
    thread.join()