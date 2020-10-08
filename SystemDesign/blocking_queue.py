import collections
import threading
import time


class blockingQueue:

    def __init__(self, max_size):
        self.max_size = max_size
        self.queue = collections.deque()
        self.exit_flag = False

        self.lock = threading.Condition()

    def push(self, item):
        self.lock.acquire()

        while len(self.queue) == self.max_size and not self.exit_flag:
            self.lock.wait()

        if not self.exit_flag:
            self.queue.append(item)
            self.lock.notify_all()
        
        self.lock.release()

    def get(self):
        self.lock.acquire()

        while len(self.queue) == 0 and not self.exit_flag:
            self.lock.wait()

        val = None

        if not self.exit_flag:
            val = self.queue.popleft()
            self.lock.notify_all()

        self.lock.release()
        return val


def thread_produce(queue):
    for i in range(5):
        queue.push(i)
        print(f"{threading.current_thread().name} pushed {i} to the queue")
        time.sleep(2)

def thread_consume(queue):
    for _ in range(5):
        val = queue.get()
        if val is not None:
            print(f"{threading.current_thread().name} got {val} from the queue")
            time.sleep(1)
    queue.exit_flag = True


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

