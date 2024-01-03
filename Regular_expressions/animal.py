class Animal:
    def __init__(self, species):
        self.species = species

    def describe(self):
        return f"I am an {self.species}"


class Mammal(Animal):
    def __init__(self, species, sound):
        super().__init__(species)
        self.sound = sound

    def make_sound(self):
        return f"I make a {self.sound} sound"


class Cat(Mammal):
    def __init__(self, species, sound, breed):
        super().__init__(species, sound)
        self.breed = breed

    def describe(self):
        return f"I am a {self.breed} cat"


# Creating instances and demonstrating usage
animal = Animal("unknown")
print(animal.describe())  # Output: I am an unknown

mammal = Mammal("unknown", "noise")
print(mammal.describe())  # Output: I am an unknown
print(mammal.make_sound())  # Output: I make a noise sound

cat = Cat("Felis catus", "meow", "Siamese")
print(cat.describe())  # Output: I am a Siamese cat
print(cat.make_sound())  # Output: I make a meow sound

