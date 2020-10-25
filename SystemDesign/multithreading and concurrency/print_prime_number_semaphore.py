import threading
import time


prime_number = 0
exit_flag = False
consumer = threading.Semaphore(0)
producer = threading.Semaphore(0)



def print_prime_number():
    global prime_number

    while not exit_flag:

        consumer.acquire()

        if not exit_flag:
            print(f"Found prime number {prime_number}")
            prime_number = None

        producer.release()

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
    global prime_number

    i = 0

    while not exit_flag:

        print(f"Checking {i}")
        if is_prime(i):
            prime_number = i
            consumer.release()
            producer.acquire()
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

    for _ in range(3):
        consumer.release()

    find_thread.join()
    print_thread_1.join()
    print_thread_2.join()
    print_thread_3.join()