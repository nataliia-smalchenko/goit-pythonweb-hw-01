from abc import ABC, abstractmethod


class Vehicle(ABC):

    def __init__(self, make: str, model: str):
        self.make = make
        self.model = model

    @abstractmethod
    def start_engine(self):
        pass


class Car(Vehicle):
    def start_engine(self):
        print(f"{self.make} {self.model}: Двигун запущено")


class Motorcycle(Vehicle):
    def start_engine(self):
        print(f"{self.make} {self.model}: Мотор заведено")


class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self, make: str, model: str):
        pass

    @abstractmethod
    def create_motorcycle(self, make: str, model: str):
        pass


class USVehicleFactory(VehicleFactory):
    def create_car(self, make, model):
        return Car(make, model + " (US Spec)")

    def create_motorcycle(self, make, model):
        return Motorcycle(make, model + " (US Spec)")


class EUVehicleFactory(VehicleFactory):
    def create_car(self, make, model):
        return Car(make, model + " (EU Spec)")

    def create_motorcycle(self, make, model):
        return Motorcycle(make, model + " (EU Spec)")


# Використання
us_factory = USVehicleFactory()
eu_factory = EUVehicleFactory()

vehicle1 = us_factory.create_car("Toyota", "Corolla")
vehicle1.start_engine()

vehicle2 = eu_factory.create_motorcycle("Harley-Davidson", "Sportster")
vehicle2.start_engine()
