mport math
class Shape:
    def calculate_area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
      self.length = length
      self.width = width

    def calculate_area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2

rectangle = Rectangle(5, 10)
circle = Circle(7)

print("Area of Rectangle:", rectangle.calculate_area())  # Output: Area of Rectangle: 50
print("Area of Circle:", circle.calculate_area())      # Output: Area of Circle: 153.93804002589985
