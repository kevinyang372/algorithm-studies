import concurrent.futures
import threading
import time


class ProducerConsumer:

    def __init__(self):
        self.to_consume = 0

        self.producer_lock = threading.Lock()
        self.consumer_lock = threading.Lock()

        self.consumer_lock.acquire()

    def produce(self):
        for i in range(1, 6):
            self.producer_lock.acquire()

            self.to_consume = i
            print(f"Produced {self.to_consume}")
            self.consumer_lock.release()

            time.sleep(2)


    def consume(self):
        for i in range(5):
            self.consumer_lock.acquire()
            
            print(f"Consumed {self.to_consume}")
            self.producer_lock.release()
            
            time.sleep(1)


if __name__ == "__main__":
    pc = ProducerConsumer()

    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(pc.produce)
        executor.submit(pc.consume)