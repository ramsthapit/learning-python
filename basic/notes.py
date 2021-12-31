# local
lambda x: x**2

name = 'this is a global name!'


def greet():
    # name = "sammy"

    def hello():
        print("hello "+name)

    hello()


greet()


class Dog():
    species = "mammal"

    def __init__(self, breed, name):
        self.breed = breed
        self.name = name


myDog = Dog("Lab", "Sammy")
otherdog = Dog("Huskie", "Grammy")
print(type(myDog))
print(myDog.breed)
print(myDog.name)
print(myDog.species)
print(otherdog.breed)


# Circle

class Circle:
    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius

    def area(self):
        return Circle.pi * self.radius ** 2

    def set_radius(self, new_r):
        self.radius = new_r


myc = Circle(3)
myc.set_radius(9)
print(myc.area())
