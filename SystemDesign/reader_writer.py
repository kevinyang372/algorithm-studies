import threading
import time

content = {}
number_of_readers = 0

write_lock = threading.Semaphore()
read_lock = threading.Lock()

def reader(key):
    global number_of_readers
    with read_lock:
        number_of_readers += 1
        if number_of_readers == 1:
            write_lock.acquire()

    thread_name = threading.current_thread().name
    print(f"{thread_name} reading {key}")
    time.sleep(0.4)
    print(f"{thread_name} found result {content.get(key, 'key does not exist')}")

    with read_lock:
        number_of_readers -= 1
        if number_of_readers == 0:
            write_lock.release()

def writer(key, value):
    with write_lock:
        thread_name = threading.current_thread().name
        print(f"{thread_name} writing {value} to {key}")
        time.sleep(0.2)
        content[key] = value
        print(f"{thread_name} finished updating!")

if __name__ == "__main__":
    thread2 = threading.Thread(target=writer, args=('sample_key', 'a'))
    thread1 = threading.Thread(target=reader, args=('sample_key',))
    thread3 = threading.Thread(target=reader, args=('sample_key',))
    thread4 = threading.Thread(target=reader, args=('sample_key',))
    thread5 = threading.Thread(target=writer, args=('sample_key', 'b'))
    thread6 = threading.Thread(target=reader, args=('sample_key',))

    threads = [thread1, thread2, thread3, thread4, thread5, thread6]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()