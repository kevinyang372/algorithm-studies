import collections
import threading
import time


class blockingQueue:

    def __init__(self, max_size):
        self.max_size = max_size
        self.queue = collections.deque()

        self.produce_lock = threading.Condition()
        self.consume_lock = threading.Condition()

    def push(self, item):
        self.produce_lock.acquire()

        while len(self.queue) == self.max_size:
            self.produce_lock.wait()

        self.queue.append(item)
        self.produce_lock.release()

        self.consume_lock.acquire()
        self.consume_lock.notify_all()
        self.consume_lock.release()

    def get(self):
        self.consume_lock.acquire()

        while len(self.queue) == 0:
            self.consume_lock.wait()

        val = self.queue.popleft()
        self.consume_lock.release()

        self.produce_lock.acquire()
        self.produce_lock.notify_all()
        self.produce_lock.release()
        return val


def thread_produce(queue):
    for i in range(5):
        queue.push(i)
        print(f"{threading.current_thread().name} pushed {i} to the queue")
        time.sleep(2)

def thread_consume(queue):
    for _ in range(5):
        val = queue.get()
        print(f"{threading.current_thread().name} got {val} from the queue")
        time.sleep(1)


if __name__ == "__main__":
    queue = blockingQueue(3)
    thread_produce_1 = threading.Thread(target=thread_produce, args=(queue,))
    thread_produce_2 = threading.Thread(target=thread_produce, args=(queue,))
    thread_produce_3 = threading.Thread(target=thread_produce, args=(queue,))

    thread_consume_1 = threading.Thread(target=thread_consume, args=(queue,))
    thread_consume_2 = threading.Thread(target=thread_consume, args=(queue,))

    threads = [thread_produce_1, thread_produce_2, thread_produce_3, thread_consume_1, thread_consume_2]
    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

