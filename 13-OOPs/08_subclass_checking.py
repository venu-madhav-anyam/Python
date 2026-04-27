class Vehicle:
    pass
class Bus(Vehicle):
    pass

if issubclass(Bus,Vehicle):
    print("True")
else:
    print("False")