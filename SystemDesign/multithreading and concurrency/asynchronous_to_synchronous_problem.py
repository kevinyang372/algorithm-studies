# This is an actual interview question asked at Netflix.

# Imagine we have an AsyncExecutor class that performs some useful task asynchronously via the method execute(). In addition, the method accepts a function object that acts as a callback and gets invoked after the asynchronous execution is done. The definition for the involved classes is below. The asynchronous work is simulated using sleep. A passed-in call is invoked to let the invoker take any desired action after the asynchronous processing is complete.

# Executor Class
# class AsyncExecutor:
 
#     def work(self, callback):
#         # simulate asynchronous work
#         time.sleep(5)
#         # let the invoker take action in a callback
#         callback()
 
#     def execute_async(self, callback):
#         Thread(target=self.work, args=(callback,)).start()
 
 
# An example run would be as follows:

# from threading import Thread
# import time


# class AsyncExecutor:

#     def work(self, callback):
#         time.sleep(5)
#         callback()

#     def execute_async(self, callback):
#         Thread(target=self.work, args=(callback,)).start()


# def say_hi():
#     print("Hi")


# if __name__ == "__main__":
#     exec = AsyncExecutor()
#     exec.execute_async(say_hi)

#     print("main thread exiting")

# Note how the main thread exits before the asynchronous execution is completed. The message "Hi" is printed after the main thread has exited.

# Your task is to make the execution synchronous without changing the original classes (imagine that you are given the binaries and not the source code) so that the main thread waits till the asynchronous execution is complete. In other words, the highlighted line#23 only executes once the asynchronous task is complete.

from threading import Thread, Semaphore
import time

class AsyncExecutor:

    def work(self, callback):
        time.sleep(5)
        callback()

    def execute_async(self, callback):
        Thread(target=self.work, args=(callback,)).start()


class SyncExecutor(AsyncExecutor):

    def __init__(self):
        self.lock = Semaphore(0)

    def work(self, callback):
        super().work(callback)
        self.lock.release()

    def execute_sync(self, callback):
        Thread(target=self.work, args=(callback,)).start()
        self.lock.acquire()


def say_hi():
    print("Hi")


if __name__ == "__main__":
    exec = SyncExecutor()
    exec.execute_sync(say_hi)

    print("main thread exiting")