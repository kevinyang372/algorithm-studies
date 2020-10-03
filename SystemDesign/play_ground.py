from threading import Thread, Semaphore, Barrier

class H2O:
    def __init__(self):
        self.hydrogen_lock = Semaphore(2)
        self.oxygen_lock = Semaphore(1)
        self.barrier = Barrier(3)


    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        self.hydrogen_lock.acquire()
        self.barrier.wait()
        # releaseHydrogen() outputs "H". Do not change or remove this line.
        releaseHydrogen()
        self.hydrogen_lock.release()


    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        self.oxygen_lock.acquire()
        self.barrier.wait()
        # releaseOxygen() outputs "O". Do not change or remove this line.
        releaseOxygen()
        self.oxygen_lock.release()


if __name__ == "__main__":
    threads = []
    h2o_obj = H2O()

    def releaseOxygen():
        print("O")

    def releaseHydrogen():
        print("H")

    input_string = "OHOOHOHHHHOHHOHHHH"

    for s in input_string:
        if s == "O":
            threads.append(Thread(target=h2o_obj.oxygen, args=(releaseOxygen,)))
        else:
            threads.append(Thread(target=h2o_obj.hydrogen, args=(releaseHydrogen,)))
    
    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()
