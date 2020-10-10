from threading import Thread, Condition
import time

class UnisexBathroomProblem:
    def __init__(self, max_limit=3):
        self.max_limit = max_limit
        self.emps_in_bathroom = 0
        self.sex = None

        self.lock = Condition()

    def use_bathroom(self, name):
        print(f"{name} using bathroom")
        time.sleep(1)
        print(f"{name} finished using bathroom. Current count: {self.emps_in_bathroom}")

    def male_use_bathroom(self, name):
        self.lock.acquire()

        while (self.sex and self.sex != "M") or self.emps_in_bathroom == self.max_limit:
            self.lock.wait()

        self.sex = "M"
        self.emps_in_bathroom += 1
        self.lock.notify_all()
        self.lock.release()

        self.use_bathroom(name)

        self.lock.acquire()
        self.emps_in_bathroom -= 1
        if self.emps_in_bathroom == 0:
            self.sex = None
        self.lock.notify_all()
        self.lock.release()

    def female_use_bathroom(self, name):
        self.lock.acquire()

        while (self.sex and self.sex != "F") or self.emps_in_bathroom == self.max_limit:
            self.lock.wait()

        self.sex = "F"
        self.emps_in_bathroom += 1
        self.lock.notify_all()
        self.lock.release()

        self.use_bathroom(name)

        self.lock.acquire()
        self.emps_in_bathroom -= 1
        if self.emps_in_bathroom == 0:
            self.sex = None
        self.lock.notify_all()
        self.lock.release()



if __name__ == "__main__":
    problem = UnisexBathroomProblem()

    female1 = Thread(target=problem.female_use_bathroom, args=("Lisa",))
    male1 = Thread(target=problem.female_use_bathroom, args=("Alice",))
    male2 = Thread(target=problem.male_use_bathroom, args=("Bob",))
    female2 = Thread(target=problem.female_use_bathroom, args=("Natasha",))
    male3 = Thread(target=problem.male_use_bathroom, args=("Anil",))
    male4 = Thread(target=problem.male_use_bathroom, args=("Wentao",))
    male5 = Thread(target=problem.male_use_bathroom, args=("Nikhil",))
    male6 = Thread(target=problem.male_use_bathroom, args=("Paul",))
    male7 = Thread(target=problem.male_use_bathroom, args=("Klemond",))
    male8 = Thread(target=problem.male_use_bathroom, args=("Bill",))
    male9 = Thread(target=problem.male_use_bathroom, args=("Zak",))

    female1.start()
    male1.start()
    male2.start()
    time.sleep(1)
    female2.start()
    male3.start()
    male4.start()
    male5.start()
    male6.start()
    male7.start()
    male8.start()
    male9.start()
        

    female1.join()
    female2.join()
    male1.join()
    male2.join()
    male3.join()
    male4.join()
    male5.join()
    male6.join()
    male7.join()
    male8.join()
    male9.join()


    print("Employees in bathroom at the end {0}".format(problem.emps_in_bathroom))