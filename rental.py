class Vehicle:
    def __init__(self, make, model, rentalAmountPerDay):
        self.make =make
        self.model =model
        self.rentalAmountPerDay =rentalAmountPerDay
available_vehicle = Vehicle("Toyota", "Ford", 200)
print("Make:", available_vehicle.make)
print("Model:", available_vehicle.model)
print("Rent per day:", available_vehicle.rentalAmountPerDay)

print()

available_vehicle = Vehicle("Truck", "Pick-up", 800)
print("Make:", available_vehicle.make)
print("Model:", available_vehicle.model)
print("Rent per day:", available_vehicle.rentalAmountPerDay)

print()

available_vehicle = Vehicle("Toyota", "Harrier", 700)
print("Make:", available_vehicle.make)
print("Model:", available_vehicle.model)
print("Rent per day:", available_vehicle.rentalAmountPerDay)
