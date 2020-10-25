import threading
import time


found_prime = False
prime_number = 0
exit_flag = False
condition = threading.Condition()


def print_prime_number():
    global found_prime
    global prime_number

    while not exit_flag:

        condition.acquire()
        while not found_prime and not exit_flag:
            condition.wait()

        if not exit_flag:
            print(f"Found prime number {prime_number}")
            found_prime = False
            condition.notify_all()

        condition.release()

    print(f"Exiting printer thread {threading.current_thread().name}")

def is_prime(num):
    if num == 2 or num == 3:
        return True

    div = 2

    while div <= num / 2:
        if num % div == 0:
            return False
        div += 1

    return True

def find_prime_number():
    global found_prime
    global prime_number

    i = 0

    while not exit_flag:

        print(f"Checking {i}")
        if is_prime(i):
            condition.acquire()
            found_prime = True
            prime_number = i
            condition.notify_all()
            condition.release()

        condition.acquire()
        while found_prime and not exit_flag:
            condition.wait()
        condition.release()

        i += 1
        time.sleep(0.1)

    print(f"Exiting finder thread {threading.current_thread().name}")

if __name__ == "__main__":

    find_thread = threading.Thread(target=find_prime_number)

    print_thread_1 = threading.Thread(target=print_prime_number)
    print_thread_2 = threading.Thread(target=print_prime_number)
    print_thread_3 = threading.Thread(target=print_prime_number)

    find_thread.start()
    print_thread_1.start()
    print_thread_2.start()
    print_thread_3.start()

    time.sleep(3)
    exit_flag = True

    condition.acquire()
    condition.notify_all()
    condition.release()

    find_thread.join()
    print_thread_1.join()
    print_thread_2.join()
    print_thread_3.join()