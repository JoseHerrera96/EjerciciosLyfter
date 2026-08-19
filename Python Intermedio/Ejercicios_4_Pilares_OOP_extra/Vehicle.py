class Vehicle:
    def __init__(self, brand, year):
        self._brand = brand
        self._year = year

    def get_info(self):
        return f"{self._brand} year {self._year}"

class Car(Vehicle):
    def __init__(self, brand, model, year, color, fuel_type):
        super().__init__(brand, year)
        self._color = color
        self._model = model
        self._fuel_type = fuel_type

    def get_info(self):
        return f"{super().get_info()} color {self._color}, model {self._model}, fuel_type {self._fuel_type}."

class Motocycle(Vehicle):
    def __init__(self, brand, model, year, color, tank_capacity, type):
        super().__init__(brand, year)
        self._color = color
        self._model = model
        self._tank_capacity = tank_capacity
        self._type = type

    def get_info(self):
        return f"{super().get_info()} color {self._color}, model {self._model}, tank_capacity {self._tank_capacity}, type {self._type}."