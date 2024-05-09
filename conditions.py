#if statements
is_hot = False
is_cold = False

if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's a cold day")
    print("Wear warm clothes")
else:
    print("It's a lovey day")

print("Enjoy your day")

house_price = 1000000
print(f"The price of this house is {house_price}")
has_good_credit = True
if has_good_credit:
    down_payment = 0.1 * house_price
else:
    down_payment = 0.2 * house_price
print(f"Your down payment is: ${down_payment}")

# Logical Operators
print('-' * 20)
has_good_credit = True
has_high_income = False
has_criminal_record = False

if has_high_income and has_good_credit:
    print("Eligible for loan")

if has_high_income or has_good_credit:
    print("Eligible for loan")

if has_good_credit and not has_criminal_record:
    print("Eligible for loan")

# AND: both conditions need to be true
# OR: at least one conditon should be true
# NOT: inverts any boolean value given


#Comparison Operators
print('-' * 20)

temperature = 40
if temperature > 30:
    print("It's a hot day")
else:
    print("It's not a hot day")

# '=' is an assignment statement'; '==' is a comparison statement producing a boolean value

name = input("What is your name? ")
if len(name) < 3:
    print("Name must be at least 3 characters")
elif len(name) > 50:
    print("Name must be a a maximum of 50 characters")
else:
    print("Name looks good!")