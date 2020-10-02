import threading

def modify_value():
    global a
    for _ in range(10_000_000):
        a += 1


if __name__ == '__main__':
    a = 0

    thread_1 = threading.Thread(target=modify_value)
    thread_2 = threading.Thread(target=modify_value)

    thread_1.start()
    thread_2.start()

    thread_1.join()
    thread_2.join()

    print(f"Final result of the calculation is {a}")