import time
from random import randint
import os
import sys


def log(func):

    def wrapper(self, water_lvl=None):
        start = time.time()
        if water_lvl is None:
            ret = func(self)
        else:
            ret = func(self, water_lvl)
        end = time.time() - start
        end = end if end >= 1 else end * 1000
        name = " " + func.__name__.capitalize()
        f = open("machine.log", "a")
        str_log = f"({os.environ['USER']})Running:{name: <20}"\
                  + f"[ exec-time = {end:.3f}"\
                  + f" {'ms' if end < 1 else 's'} ]\n"
        f.write(str_log)
        f.close()
        return ret

    return wrapper


class CoffeeMachine():

    water_level = 100

    @log
    def start_machine(self):
        if self.water_level > 20:
            return True
        else:
            print("Please add water!")
            return False

    @log
    def boil_water(self):
        return "boiling..."

    @log
    def make_coffee(self):
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.1)
                self.water_level -= 1
            print(self.boil_water())
            print("Coffee is ready!")

    @log
    def add_water(self, water_level):
        time.sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")


if __name__ == "__main__":
    machine = CoffeeMachine()
    for i in range(0, 5):
        machine.make_coffee()

    machine.make_coffee()
    machine.add_water(70)
