class animal:
    active = True

class dog(animal):
    def speak(self):
        print( "Woof!")

class cat(animal):
    def speak(self):
        print( "Meow!")

class car():
    def speak(self):
        print( "vroom!")
    active = False


animals = [dog(), cat(), car()]

for animal in animals:
    animal.speak()
    print(animal.active)