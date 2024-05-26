# Functions - a container for a few lines of code that performs a specific task
# Examples - print() or input()
# def - define (a new function)

# greet_user() - cant do this; you must define your function first before using it; order matters
# def greet_user():  # how you should right your functions
#     print('Hi There')
#     print('Welcome aboard')
#
#
# print('Start')
# greet_user()
# print("Finish")

# Parameters
# def greet_user(first_name, last_name):  # how you should right your functions
#     print(f'Hi {first_name} {last_name}!')
#     print('Welcome aboard')
#
#
# print('Start')
# # greet_user() - will return a TypeError as there's a missing parameter
# greet_user("Obehi", "Ehimen") #"Obehi" is an argument that is passed to the name parameter
# print("Finish")

print('-' * 20)

# Keyword Arguments
def greet_user(first_name, last_name):  # how you should right your functions
    print(f'Hi {first_name} {last_name}!')
    print('Welcome aboard')


print('Start')
# greet_user() - will return a TypeError as there's a missing parameter
greet_user("Obehi", "Ehimen")  # "Obehi" is an argument that is passed to the name parameter
greet_user("Ehimen", "Obehi")  # WRONG - positional arguments; order matters
greet_user(last_name="Ehimen", first_name="Obehi") # Keyword arguments-parameter name followed by its value;
                                                   # order doesnt matter; not used that much of the time
# calc_cost(total = 50, shipping = 5, discount=0.1)
print("Finish")

#For the most part use positional arguments
#But if youre dealing with functions that take numeric values, use keyword arguments to make it more readable
# Keyword arguments should come after positional arguments, especially when mixing different arguments

print('-' * 20)
#Return Statement
def square(number):
    return number * number
    # print(number * number)
    # returns  None by default

# result = square(3)
print(square(3))