import time
import threading


class Thread1(threading.Thread):
    def __init__(self):
        super().__init__()

    def run(self):
        for _ in range(5):
            time.sleep(0.5)
            print("Processing with child thread")
        print("Finished processing in child thread")


if __name__ == "__main__":
    child_thread = Thread1()
    child_thread.start()

    print("Processing with main thread")
    time.sleep(0.5)

    # join method waits for the child thread to finish
    child_thread.join()
    print("Both threads have completed")