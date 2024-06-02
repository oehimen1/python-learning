
class Person:
    # constructors - a function that gets called at the time the object is
    # being created
    def __init__(self, name): # "self" references the current object
        self.name = name

    def talk(self):
        print(f"Hi, I am {self.name}")


person1 = Person("Abigail")
person1.talk()

bob = Person("Bob Smith")
bob.talk()