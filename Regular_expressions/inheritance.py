ass Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
class Car (Vehicle):
    def fuel_type(self):
        return "petrol"
