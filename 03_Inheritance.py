
#Create a base class Animal that represents a generic animal.
#It should include attributes like name and sound.
#Create two subclasses: Dog and Cat, which inherit from Animal.
#Override the make_sound() method in each subclass to print a specific sound.
#Also, implement __str__() to return a meaningful description of the animal.

class Animal:
    def __init__(self, name, sound):
        self.sound = sound
        self.name = name

    def make_sound(self):
        print(f'{self.name} makes a {self.sound} sound.')

    def __str__(self):
        return f'This is {self.name}, a lovely animal.'

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name, sound = 'woof')

    def make_sound(self):
        print(f'{self.name} says: Woof! Woof!')

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name, sound = 'meow')

    def make_sound(self):
        print(f'{self.name} says: Meow~')

dog1 = Dog('Buddy')
cat1 = Cat('Luna')

print(dog1)
dog1.make_sound()

print(cat1)
cat1.make_sound()