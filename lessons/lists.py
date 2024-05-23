# Lists
names = ['John', 'Bob', 'Mosh', 'Sarah', 'Mary']
print(names)
print(names[0])
print(names[2])
print(names[-1]) # returns Mary
print(names[-2]) # return Sarah
print(names[2:]) # return elements Mosh, Sarah, and Mary
print(names[2:4]) # returns Mosh and Sarah
names[0] = 'Jon'
print(names)

print('*' * 15)
numbers = [2,6,1,4,7,5,9,0,3,8]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(f'Max number in list is: {max}')

print('*' * 15)
#2D Lists - each item in the list is another list
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[0][1])
matrix[0][1] = 20
print(matrix[0][1])

for row in matrix:
    for item in row:
        print(item)

print('*' * 15)
#List Methods
numbers = [5, 2, 1, 7, 4]
# numbers.append(20) # added to end at the list
numbers.insert(0, 10)
print(numbers)
numbers.remove(10)
print(numbers)
# numbers.clear()
# print(numbers)
numbers.pop()
print(numbers)
print(numbers.index(5)) #returns the first occurence of this item
print(50 in numbers)
print(numbers.count(5))
numbers.sort()
print(numbers) # puts in ascending order
numbers.reverse()
print(numbers)
numbers.sort()
numbers2 = numbers.copy()
numbers.append(10)
print(numbers)
print(numbers2)

print('*' * 15)
# program to remove duplicates in a list
list = [2, 2, 4, 6, 3, 4, 6, 1]
uniques = []
for item in list:
    if item not in uniques:
        uniques.append(item)
print(uniques)


