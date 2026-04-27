class Vehicle:
    pass

class Bus(Vehicle):
    pass

b = Bus()

if isinstance(b,Vehicle):
    print("True")
else:
    print("False")