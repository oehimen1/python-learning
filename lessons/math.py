import math
# 10 is an integers
# 10.123 is a float (has a decimal point)

print('Addition ', 10+3)
print('Subtraction ', 10-3)
print('Multiplication ', 10*3)
print('Division 1 ', 10/3) # can produce a floating number
print('Division 2 ', 10//3) # rounds to an integer
print('Modulus ', 10%3)
print('Exponent or Power ', 10**3) # 10^3

#Augemented Assingment Operator
x = 10
x += 3 # x = x + 3
print(x)
x -= 6
print(x)

#Operator Precedence
x = 10 + 3 * 2  # 16 - the mutiplication has a higher precedence
print(x)
x = 10 + 3 * 2 ** 2  # 2**2 is executed first
print(x)
x = (2 + 3) * 10 - 3  # (2+3) is executed first
print(x)

# Order of operations
# parenthesis
# exponentiation 2 ** 3
# muliplication or division
# addition or subtraction


#Math Functions
x = 2.9
print(round(x))
print(abs(-2.9))
# May need to import the Math module for more advanced math functions
print(math.ceil(2.9))
print(math.floor(2.9))
# https://docs.python.org/3/library/math.html
print(math.pow(4, 5))
print(math.sqrt(81))
print(math.radians(90))


