weight = int(input("Please enter your weight: "))
lb_or_kg = input("(L)bs or (K)g: ")

if lb_or_kg.upper() == 'L':
    weight = weight * 0.45
    print(f"You are {weight} kg")
elif lb_or_kg.upper() == 'K':
    weight = weight // 0.45
    print(f"You are {weight} lb")