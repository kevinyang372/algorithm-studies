# Imagine at the end of a political conference, republicans and democrats are trying to leave the venue and ordering Uber rides at the same time. However, to make sure no fight breaks out in an Uber ride, the software developers at Uber come up with an algorithm whereby either an Uber ride can have all democrats or republicans or two Democrats and two Republicans. All other combinations can result in a fist-fight.

# Your task as the Uber developer is to model the ride requestors as threads. Once an acceptable combination of riders is possible, threads are allowed to proceed to ride. Each thread invokes the method seated() when selected by the system for the next ride. When all the threads are seated, any one of the four threads can invoke the method drive() to inform the driver to start the ride.
from threading import Thread, Condition, Lock, current_thread
import random

class UberSeatingProblem:

    def __init__(self):
        self.completed_rides = set()
        self.rides = {}
        self.rid = 0

        self.seating_lock = Lock()

    def satisfy_condition(self, demo, repl):
        return not ((demo == 3 and repl != 0) or (repl == 3 and demo != 0))

    def seat(self, ride_id):
        lock = self.rides[ride_id][2]

        lock.acquire()
        while self.rides[ride_id][0] + self.rides[ride_id][1] < 4:
            lock.wait()

        if ride_id not in self.completed_rides:
            self.completed_rides.add(ride_id)
            self.drive(ride_id)

        lock.notify_all()
        lock.release()

    def drive(self, ride_id):
        print(f"Ride {ride_id} departed with {self.rides[ride_id][0]} republicans and {self.rides[ride_id][1]} democrats")

    def seat_democrat(self):
        self.seating_lock.acquire()
        print(f"Seating democrat from {current_thread().name} with state {self.rides}")
        for ride in self.rides:
            if ride not in self.completed_rides and self.satisfy_condition(self.rides[ride][0], self.rides[ride][1] + 1):
                print(f"{current_thread().name} found ride {ride} with {self.rides[ride]} satisfies the condition")
                self.rides[ride][1] += 1
                self.seating_lock.release()
                self.seat(ride)
                break
        else:
            print(f"{current_thread().name} couldn't find a ride. Creating a new one...")
            self.rides[self.rid] = [0, 1, Condition()]
            self.seating_lock.release()
            self.seat(self.rid)
            self.rid += 1

    def seat_republican(self):
        self.seating_lock.acquire()
        print(f"Seating republican from {current_thread().name} with state {self.rides}")
        for ride in self.rides:
            if ride not in self.completed_rides and self.satisfy_condition(self.rides[ride][0] + 1, self.rides[ride][1]):
                print(f"{current_thread().name} found ride {ride} with {self.rides[ride]} satisfies the condition")
                self.rides[ride][0] += 1
                self.seating_lock.release()
                self.seat(ride)
                break
        else:
            print(f"{current_thread().name} couldn't find a ride. Creating a new one...")
            ride = self.rid
            self.rides[ride] = [1, 0, Condition()]
            self.rid += 1
            self.seating_lock.release()
            self.seat(ride)



def controlled_simulation():
    problem = UberSeatingProblem()
    dems = 10
    repubs = 10
    
    total = dems + repubs
    print("Total {0} dems and {1} repubs\n".format(dems, repubs))

    riders = list()

    while total != 0:
        toss = random.randint(0, 1)
        if toss == 1 and dems != 0:
            riders.append(Thread(target=problem.seat_democrat))
            dems -= 1
            total -= 1
        elif toss == 0 and repubs != 0:
            riders.append(Thread(target=problem.seat_republican))
            repubs -= 1
            total -= 1

    for rider in riders:
        rider.start()

    for rider in riders:
        rider.join()


if __name__ == "__main__":
    controlled_simulation()