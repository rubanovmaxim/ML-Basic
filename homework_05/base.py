"""
Доработайте класс `Vehicle`
"""

from abc import ABC

from homework_05.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):
    def __init__(self,weight = 1600, fuel = 60, fuel_consumption = 9.5):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.started = False

    def start(self):
        if self.started == False:
            if self.fuel > 0:
                self.started = True
            else:
                raise LowFuelError("Топливо на нуле, не могу стартовать")

    def move(self, distance):
        if self.fuel >= distance / self.fuel_consumption:
            self.fuel -= distance / self.fuel_consumption
        else:
            raise NotEnoughFuel("Недостаточно топлива")
