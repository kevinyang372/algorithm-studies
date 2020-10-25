# A similar problem appears in Silberschatz and Galvin's OS book, and variations of this problem exist in the wild.

# A barbershop consists of a waiting room with n chairs, and a barber chair for giving haircuts. If there are no customers to be served, the barber goes to sleep. If a customer enters the barbershop and all chairs are occupied, then the customer leaves the shop. If the barber is busy, but chairs are available, then the customer sits in one of the free chairs. If the barber is asleep, the customer wakes up the barber. Write a program to coordinate the interaction between the barber and the customers.

from threading import Thread, Condition, Lock

import time
import collections

class BarberShop:

    def __init__(self, num_chairs):
        self.chairs = [True] * num_chairs
        self.lock = Lock()

        self.available_barbers = collections.deque()
        self.barber_to_lock = {}
        self.customer_lock = Condition()

    def barber(self, name):
        with self.lock:
            self.available_barbers.append(name)
            self.barber_to_lock[name] = Condition()
            print(f"Barber {name} joins the barber shop")

        self.barber_to_lock[name].acquire()
        while True:
            print(f"Barber {name} goes to sleep.")
            while name in self.available_barbers:
                self.barber_to_lock[name].wait()

            print(f"Barber {name} wakes up and starts working!")
            while name not in self.available_barbers:
                self.barber_to_lock[name].wait()

    def customer_walks_in(self):
        self.customer_lock.acquire()

        if not any(self.chairs):
            print(f"Customer leaves as he/she couldn't find a chair")
            self.customer_lock.release()
            return;

        for i in range(len(self.chairs)):
            if self.chairs[i]:
                chair_id = i
                self.chairs[i] = False
                break

        print(f"Customer took chair {chair_id}")
        
        while not self.available_barbers:
            self.customer_lock.wait()

        barber_name = self.available_barbers.popleft()
        self.barber_to_lock[barber_name].acquire()
        self.barber_to_lock[barber_name].notify()
        self.barber_to_lock[barber_name].release()

        self.customer_lock.release()

        time.sleep(0.1)

        self.customer_lock.acquire()
        self.chairs[chair_id] = True

        self.barber_to_lock[barber_name].acquire()
        print(f"{barber_name} has done one haircut!")
        self.available_barbers.append(barber_name)
        self.barber_to_lock[barber_name].notify()
        self.barber_to_lock[barber_name].release()

        self.customer_lock.notify_all()
        self.customer_lock.release()


if __name__ == "__main__":

    barber_shop = BarberShop(3)

    barber_thread = Thread(target=barber_shop.barber, args=("Mike",))
    barber_thread.setDaemon(True)
    barber_thread.start()

    barber_thread_2 = Thread(target=barber_shop.barber, args=("Andrew",))
    barber_thread_2.setDaemon(True)
    barber_thread_2.start()

    # intially 10 customers enter the barber shop one after the other
    customers = list()
    for _ in range(0, 10):
        customers.append(Thread(target=barber_shop.customer_walks_in))

    for customer in customers:
        customer.start()

    time.sleep(0.5)

    # second wave of 5 customers
    late_customers = list()
    for _ in range(0, 5):
        late_customers.append(Thread(target=barber_shop.customer_walks_in))

    for customer in late_customers:
        customer.start()

    for customer in customers:
        customer.join()

    for customer in late_customers:
        customer.join()
