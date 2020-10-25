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


class ProducerConsumerMonitor:

    def __init__(self):
        self.to_consume = 0
        self.producer_lock = threading.Condition()

    def produce(self):
        for i in range(1, 6):
            self.producer_lock.acquire()

            self.to_consume = i
            print(f"Produced {self.to_consume}")
            self.producer_lock.notify_all()
            self.producer_lock.release()

            time.sleep(2)


    def consume(self):
        for i in range(5):
            self.producer_lock.acquire()
            
            consumed = self.to_consume
            print(f"Consumed {consumed}")
            self.producer_lock.release()
            
            time.sleep(1)

            self.producer_lock.acquire()
            while self.to_consume == consumed and i != 4:
                self.producer_lock.wait()
            self.producer_lock.release()


if __name__ == "__main__":
    pc = ProducerConsumerMonitor()

    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(pc.produce)
        executor.submit(pc.consume)