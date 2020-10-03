from threading import Condition, Thread

class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        
        self.call_lock = Condition()
        self.state = 0
        
        
    # printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(self.n):
            with self.call_lock:
                while self.state: self.call_lock.wait()
                printNumber(0)

                if i % 2:
                    self.state = 1
                else:
                    self.state = 2

                self.call_lock.notify_all()
            
        
    def even(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(2, self.n + 1, 2):
            with self.call_lock:
                while self.state != 1: self.call_lock.wait()

                printNumber(i)
                self.state = 0
                self.call_lock.notify_all()
        
        
    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n + 1, 2):
            with self.call_lock:
                while self.state != 2: self.call_lock.wait()

                printNumber(i)
                self.state = 0
                self.call_lock.notify_all()


if __name__ == "__main__":
    printNumber = lambda x: print(x)
    zero_even_odd_obj = ZeroEvenOdd(10)

    thread_1 = Thread(target=zero_even_odd_obj.zero, args=(printNumber,))
    thread_2 = Thread(target=zero_even_odd_obj.even, args=(printNumber,))
    thread_3 = Thread(target=zero_even_odd_obj.odd, args=(printNumber,))

    thread_1.start()
    thread_2.start()
    thread_3.start()

    thread_1.join()
    thread_2.join()
    thread_3.join()
