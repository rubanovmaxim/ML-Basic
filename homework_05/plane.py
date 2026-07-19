"""
Создайте класс `Plane`, наследник `Vehicle`
"""
from homework_05.base import Vehicle
from homework_05.exceptions import CargoOverload

class Plane(Vehicle):
    def __init__(self, weight, fuel, fuel_consumption, cargo = 0, max_cargo = 1000):
        super().__init__(weight, fuel, fuel_consumption)
        self.cargo = cargo
        self.max_cargo = max_cargo

    def load_cargo(self,loaded_cargo):
        if self.cargo + loaded_cargo > self.max_cargo:
            raise CargoOverload("Машина не может перевезти такой тяжелый груз")
        else:
            self.cargo += loaded_cargo
    def remove_all_cargo(self):
        c = self.cargo
        self.cargo = 0
        return c;