# Dictionaires - storing information that comes in key value pairs

#each key should be unique
customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}

print(customer["name"])
# print(customer["birthDate"]) #error
# print(customer["Name"]) #error

customer["name"] = "Jack Smith"
print(customer.get("age"))
print(customer.get("birthdate")) #returns None as there an absence of value
print(customer.get("birthdate", "Jan 1 1980")) # reutrns a defalut value of Jan 1, 1980
print(customer["name"])
customer["birthdate"] = "Jan 1 1980"
print(customer["birthdate"])

phone = input("Phone: ")
translation = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five"
}
output = ""
for number in phone:
    found = translation.get(number)
    output += found + " "

print(output)