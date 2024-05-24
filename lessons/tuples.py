# Tuples - similar to lists, but you cant modify them and are immutable(you can't mutate or change them)
numbers = (1, 2, 3)
# number[0] = 10 #gives an error
#It's better to use a tuple if you have items in your list that you dont want to change
print(numbers[0])
print('*' * 20)

#Unpacking
coordinates = (1, 2, 3)
# coordinates[0] * coordinates[1] * coordinates[2]

#Long version
# x = coordinates[0]
# y = coordinates[1]
# z = coordinates[2]

#Short hand version
x, y, z = coordinates
print(y)