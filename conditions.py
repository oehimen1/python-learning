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