customer = {
    "Name": "Diksha Sharma",
    "age": 24,
    "is_verified": True
}
print(customer["age"])
print(customer.get("birthdate"))
print(customer.get("birthdate", "March 18 2001"))

customer["Gender"]="Female"
print(customer["Gender"])


phone = input("Phone: ")
digits_mapping = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four"
}
output = " "
for character in phone:
    output += digits_mapping.get(character, "!") + " "
print(output)    