from abc import ABC,abstractmethod

class Vehicle(ABC):
    def __init__(self,regno,make,model,price):
        self.regno = regno
        self.make = make
        self.model = model
        self.price = price

    def __str__(self):
        return f"regno:{self.regno}, make:{self.make}, model:{self.model}, price:{self.price} "

    @abstractmethod
    def calculate_insurance(self):
        pass

class TwoWheeler(Vehicle,ABC):
    def calculate_insurance(self):
        return self.price * 1.05

class FourWheeler(Vehicle, ABC):
    def calculate_insurance(self):
        return self.price * 1.10


if __name__ == "__main__":
    bike = TwoWheeler(123,"Ktm", "DUke", 800000)
    print(bike.__str__())
    print(f"The insurance for {bike.model} is: {bike.calculate_insurance()}\n")

    car = FourWheeler(9987, "MARUTI", "ALto", 100000)
    print(car.__str__())
    print(f"The insurance for {car.model} is: {car.calculate_insurance()}")

