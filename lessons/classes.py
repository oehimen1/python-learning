# Classes used to define new types

#naming classes - PascalNamingConvention
# variable and function- lower case letters and underscore to separate words
class Point:
    # constructors - a function that gets called at the time the object is
    # being created
    def __init__(self, x, y):
        # "self" references the current object
        self.x = x
        self.y = y

    def move(self):
        print("move")
    def draw(self):
        print("draw")


# object - instance of a class
# class - blue print of an object

# point1 = Point()
# point1.x = 10
# point1.y = 20
# print(point1.x)
# point1.draw()

# point2 = Point()
# point2.x = 1
# print(point2.x)

# point = Point(10, 20)
# point.x = 11
# print(point.x)
