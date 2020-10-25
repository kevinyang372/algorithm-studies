import threading
import time


total_item = 0
lock = threading.Lock()

def task():
    global total_item

    thread_name = threading.current_thread().getName()
    item_to_add = 0

    while total_item < 20:
        if item_to_add and lock.acquire(blocking=False):
            total_item += item_to_add
            print(f"{thread_name} added {item_to_add} to the total items")
            item_to_add = 0

            time.sleep(0.3)
            lock.release()
        else:
            item_to_add += 1
            time.sleep(0.1)


if __name__ == "__main__":
    thread_1 = threading.Thread(target=task)
    thread_2 = threading.Thread(target=task)

    thread_1.start()
    thread_2.start()

    thread_1.join()
    thread_2.join()