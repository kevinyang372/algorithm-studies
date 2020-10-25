import threading


rlock = threading.RLock()

def task1():
    global a
    rlock.acquire()
    a += 1
    rlock.release()


def task2():
    global b
    rlock.acquire()
    b += 1
    task1()
    rlock.release()


if __name__ == "__main__":
    a = b = 0
    
    thread_1 = threading.Thread(target=task1)
    thread_2 = threading.Thread(target=task2)

    thread_1.start()
    thread_2.start()

    thread_1.join()
    thread_2.join()

    print(f"Total number of a {a}")
    print(f"Total number of b {b}")