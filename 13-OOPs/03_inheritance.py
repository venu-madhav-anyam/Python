class Vehicle:
    def move(self):
        print("Vehicle is moving")
class Bus(Vehicle):
    def bus_move(self):
        print("Bus is moving")

b = Bus()
b.move()