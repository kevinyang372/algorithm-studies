# Design and implement a thread-safe class that allows registration of callback methods that are executed after a user specified time interval in seconds has elapsed.

from threading import Condition, Lock

import heapq
import time

class ThreadedSafeCallback:

    def __init__(self):
        self.execution_queue = []
        self.cond = Condition()

    def add_action(self, action):
        action.exec_at = action.exec_after_secs + time.time()

        self.cond.acquire()
        heapq.heappush(self.execution_queue, action)
        self.cond.notify_all()
        self.cond.release()

    def start(self):
        while True:
            self.cond.acquire()
            while len(self.execution_queue) == 0:
                self.cond.wait()

            while len(self.execution_queue) != 0:
                action_time = self.execution_queue[0].time
                sleep_for = time.time() - action_time

                if sleep_for <= 0:
                    break

                self.cond.wait(sleep_for)

            if self.execution_queue:
                action = heapq.heappop(self.execution_queue)
                action.func()

            self.cond.release()


def DeferredAction:

    def __init__(self, func, time, name):
        self.func = func
        self.exec_after_secs = time
        self.name = name

    def __it__(self, obj):
        return self.exec_at < obj.exec_at
