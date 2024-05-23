#While Loops

i = 1
while i <= 5 :
    print('*' * i)
    i = i + 1
print("Done")
print('-' * 15)

#For Loops - iterate over items of a collection

for item in range(10): # gives 0, 1,2, 3, 4, 5, 6... 9
    print(item)
print('-' * 15)

for item in range(5, 10): # gives 5, 6, 7, 8, 9
    print(item)
print('-' * 15)

for item in range(5, 10, 2): # gives 5,7,9
    print(item)
print('-' * 15)

prices = [10, 20, 30]
total = 0
for item in prices:
    total += item
print(f"Total: ${total}")
print('-' * 15)

#Nested Loops - adding one loop inside another loop
for x in range(4):
    for y in range(3):
        print(f'({x}, {y})')

print('-' * 15)
numbers = [5, 2, 5, 2, 2]
for x in numbers:
    output = ''
    for y in range(x):
        output += '*'
    print(output)

