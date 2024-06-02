# age = int(input('Age: '))
# print(age)
# exit code 0 - program executed successfully, there were no errors; didnt crash
# exit code 1 - program executed unsucessfully; it crashed
 #this should be expected as a developer

#Try-except blocks are used to handle exceptions
# that are raised in our programs. As a developer you should
# anticipate these exceptions
try:
    age = int(input('Age: ')) # will throw an exception if input invalid
    income = 20000
    risk = income/age
    print(age)
except ZeroDivisionError:
    print('Age cannot be zero')
except ValueError: # will catch the exception and print out message
    print('Invalid value')
