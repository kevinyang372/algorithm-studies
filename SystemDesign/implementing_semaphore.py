# Python does provide its own implementation of Semaphore and BoundedSemaphore, however, we want to implement a semaphore with a slight twist.

# Briefly, a semaphore is a construct that allows some threads to access a fixed set of resources in parallel. Always think of a semaphore as having a fixed number of permits to give out. Once all the permits are given out, requesting threads, need to wait for a permit to be returned before proceeding forward.

# Your task is to implement a semaphore which takes in its constructor the maximum number of permits allowed and is also initialized with the same number of permits. Additionally, if all the permits have been given out, the semaphore blocks threads attempting to acquire it.

from threading import Condition

class Semaphore:
    """Simulate Semaphore in Python."""

    def __init__(self, max_permits=10, initial_permit=1):
        """Initiate a semaphore object."""
        self.max_permits = max_permits
        self.current_permit = initial_permit
        self.lock = Condition()

    def acquire(self):
        """Acquire a permit. Block if the current permit is zero."""
        self.lock.acquire()

        # wait when the current permit number is zero
        while self.current_permit == 0:
            self.lock.wait()

        self.current_permit -= 1

        # notify potential release that one permit has been acquired
        self.lock.notify_all()
        self.lock.release()

    def release(self):
        """Release a permit. Block if the current permit is over the max number of permits."""
        self.lock.acquire()

        # wait when the current permit number is equal to the max number of permits
        while self.current_permit == self.max_permit:
            self.lock.wait()

        self.current_permit += 1

        # notify potential acquire that one permit has been released
        self.lock.notify_all()
        self.lock.release()

