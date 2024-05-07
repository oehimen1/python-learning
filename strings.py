course = "Pythons's Course for Beginners"
print(course)
course = 'Python for "Beginners"'
print(course)
course = ''' 
Hi Obehi,

Here is our first email to you.

Thank you,
The support team

'''
print(course)
course = 'Python for Beginners'
print('First letter', course[0]) # getting the first character from the beginning
print('Last letter', course[-1]) #getting the first character from the end
print('Second to last character', course[-2]) #getting the second character form the end
print(course[0:3]) # returns the characters from index 0 to < index 3 (non-inclusive)
print(course[0:]) # return the characters from the beginning to end of the string
print(course[1:])#return the characters of the string exlcuding the first character
print(course[:5]) # returns the characters of the string from 0(assumed)  to < index 5

another = course[:] #a copy of the course string
print(another)

name = 'Jennifer'
print(name[1:-1])

#Formatted Strings: prefixed with an f and use curly braces as placeholders
first = 'John'
last = 'Smith'
message = first + ' [' + last + '] is a coder' # not ideal
msg = f'{first} [{last}] is a coder' #more ideal
print(message)
print(msg)

#String Methods
course = 'Python for Beginners'
print(len(course)) # counts the number of characters in string and 'len' is a function
print(course.upper()) #upper is a method
print(course.lower())
print(course.lower())
print(course.find('t')) # returns the first occurrence of that character and is case-sensitive
print(course.replace('Beginners', 'Absolute Beginners'))

print('Python' in  course) #checking to see if 'Python' is in the course variable and returns a boolean value and is case sensitive

#the difference between 'find' and 'in' is that 'find' return the index of that charcter or sewuence of characters
#and 'in' outputs a boolean value (do we have this or not)