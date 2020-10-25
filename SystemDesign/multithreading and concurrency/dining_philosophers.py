import threading


chopstick_a = threading.Lock()
chopstick_b = threading.Lock()
chopstick_c = threading.Lock()

total_sushi = 500


def eat_sushi(name, first_chopstick, second_chopstick):
    global total_sushi
    while total_sushi > 0:
        first_chopstick.acquire()
        second_chopstick.acquire()

        if total_sushi > 0:
            total_sushi -= 1
            print(f"{name} ate one sushi! Remaining sushi {total_sushi}")

        second_chopstick.release()
        first_chopstick.release()


if __name__ == "__main__":

    philosopher_1 = threading.Thread(target=eat_sushi, args=("philosopher_1", chopstick_a, chopstick_b))
    philosopher_2 = threading.Thread(target=eat_sushi, args=("philosopher_2", chopstick_b, chopstick_c))
    philosopher_3 = threading.Thread(target=eat_sushi, args=("philosopher_3", chopstick_c, chopstick_a))

    philosopher_1.start()
    philosopher_2.start()
    philosopher_3.start()

    philosopher_1.join()
    philosopher_2.join()
    philosopher_3.join()