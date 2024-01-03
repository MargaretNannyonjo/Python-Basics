class Animal:
    def __init__(self, make_sound):
        self.__make_sound = make_sound
    def get_make_sound(self):
        return self.__make_sound

class Dog (Animal):
    def animal_sound(self):
    return self.__make_sound()
