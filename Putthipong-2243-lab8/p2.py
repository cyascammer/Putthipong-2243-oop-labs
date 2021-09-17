'''
Putthipong Phukhansung
633040224-3
Problem 2
'''


class Vehicle:
    def __init__(self, name, speed, mileage):
        self.name = name
        self.speed = speed
        self.mileage = mileage

    def set_speed(self, speed):
        self.new_speed = speed

class Car(Vehicle):
    def __init__(self, name, speed, mileage, num_doors):
        self.numdoors = num_doors
        super().__init__(name, speed, mileage)

    def __str__(self):
        return (f"Name: {self.name} speed: {self.speed} mileage: {self.mileage} num doors: {self.numdoors}")

class Bus(Vehicle):
    def __init__(self, name, speed, mileage, capacity):
        self.capacity = capacity
        super().__init__(name, speed, mileage)

    def __str__(self):
        return (f"Name: {self.name} speed: {self.speed} mileage: {self.mileage} capacity: {self.capacity}")


if __name__ == '__main__':
    car = Car("Toyota Vios", 90, 150000, 4)
    bus = Bus("School Volvo", 12, 200000, 100)
    print(car)
    print(bus)
    bus.set_speed(30)
    print(bus)