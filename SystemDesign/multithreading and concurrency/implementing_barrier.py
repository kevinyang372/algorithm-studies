from threading import Condition, Thread, current_thread
import time


class Barrier:

    def __init__(self, num_thread):
        self.max_thread = num_thread
        self.reached_thread_count = 0
        self.release_thread_count = 0

        self.lock = Condition()

    def wait(self):
        self.lock.acquire()

        while self.reached_thread_count == self.max_thread:
            self.lock.wait()

        self.reached_thread_count += 1

        if self.reached_thread_count == self.max_thread:
            self.release_thread_count = self.max_thread
            self.lock.notify_all()
        else:
            while self.release_thread_count == 0:
                self.lock.wait()

        self.release_thread_count -= 1

        if self.release_thread_count == 0:
            self.reached_thread_count = 0
            self.lock.notify_all()

        print("{0} released".format(current_thread().getName()), flush=True)
        self.lock.release()


def thread_process(sleep_for):
    time.sleep(sleep_for)
    print("Thread {0} reached the barrier".format(current_thread().getName()), flush=True)
    barrier.wait()

    time.sleep(sleep_for)
    print("Thread {0} reached the barrier".format(current_thread().getName()))
    barrier.wait()

    time.sleep(sleep_for)
    print("Thread {0} reached the barrier".format(current_thread().getName()))
    barrier.wait()


if __name__ == "__main__":
    barrier = Barrier(3)

    t1 = Thread(target=thread_process, args=(0,))
    t2 = Thread(target=thread_process, args=(0.5,))
    t3 = Thread(target=thread_process, args=(1.5,))

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()