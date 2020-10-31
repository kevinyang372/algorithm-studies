# Imagine you have an application where you have multiple readers and a single writer. You are asked to design a lock which lets multiple readers read at the same time, but only one writer write at a time.

from threading import Thread, Condition, current_thread
import random
import time

class ReadersWriteLock:

    def __init__(self):
        self.cond = Condition()
        self.read_count = 0

        self.write_in_progress = False

    def acquire_read_lock(self):
        self.cond.acquire()

        while self.write_in_progress:
            self.cond.wait()

        self.read_count += 1
        self.cond.release()

    def release_read_lock(self):
        self.cond.acquire()
        self.read_count -= 1

        if self.read_count == 0:
            self.cond.notify_all()

        self.cond.release()

    def acquire_write_lock(self):
        self.cond.acquire()

        while self.read_count > 0 or self.write_in_progress:
            self.cond.wait()

        self.write_in_progress = True
        self.cond.release()

    def release_write_lock(self):
        self.cond.acquire()
        self.write_in_progress = False
        self.cond.notify_all()
        self.cond.release()

def writer_thread(lock):
    while 1:
        lock.acquire_write_lock()
        print("\n{0} writing at {1} and current readers = {2}".format(current_thread().getName(), time.time(),
                                                                      lock.read_count), flush=True)
        write_for = random.randint(1, 5)
        time.sleep(write_for)
        print("\n{0} releasing at {1} and current readers = {2}".format(current_thread().getName(), time.time(),
                                                                        lock.read_count),
              flush=True)
        lock.release_write_lock()
        time.sleep(1)


def reader_thread(lock):
    while 1:
        lock.acquire_read_lock()
        print("\n{0} reading at {1} and write in progress = {2}".format(current_thread().getName(), time.time(),
                                                                        lock.write_in_progress), flush=True)
        read_for = random.randint(1, 2)
        time.sleep(read_for)
        print("\n{0} releasing at {1} and write in progress = {2}".format(current_thread().getName(), time.time(),
                                                                          lock.write_in_progress), flush=True)
        lock.release_read_lock()
        time.sleep(1)


if __name__ == "__main__":

    lock = ReadersWriteLock()

    writer1 = Thread(target=writer_thread, args=(lock,), name="writer-1", daemon=True)
    writer2 = Thread(target=writer_thread, args=(lock,), name="writer-2", daemon=True)

    writer1.start()

    readers = list()
    for i in range(0, 3):
        readers.append(Thread(target=reader_thread, args=(lock,), name="reader-{0}".format(i + 1), daemon=True))

    for reader in readers:
        reader.start()

    writer2.start()

    time.sleep(15)
