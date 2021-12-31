class Animal():
    def __init__(self):
        print("Animal")

    def whoAmI(self):
        print("animal")

    def eat(self):
        print("eating")


class Dog(Animal):
    def __init__(self):
        # Animal.__init__(self)
        print("Dog Created")

    def bark(self):
        print("woof")

    def eat(self):
        print("Dog Eating")


d = Dog()

# an = Animal()
# an.whoAmI()
# an.eat()

d.whoAmI()
d.eat()
d.bark()


# Special Methods

class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return "Title: {}, Author: {}, Pages: {} ".format(self.title, self.author, self.pages)

    def __len__(self):
        return self.pages

    def __del__(self):
        print("a book is destroyed!")


b = Book("Python", "jose", 200)
print(b)
print(len(b))
