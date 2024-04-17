names = []
phone_numbers = []

num = int(input("Enter the number of contacts want to add: "))

for i in range(num):
    name = input("Enter Name: ")
    phone_number = int(input("Enter Phone Number: "))

    names.append(name)
    phone_numbers.append(phone_number)

print("\tname------>Phone Number")

for i in range(num):
    print(f'\t{names[i]}------>{phone_numbers[i]}')

s = input("Enter the Name to search: ")
if s in names:
    index = names.index(s)
    name = names[index]
    phone_number = phone_numbers[index]

    print(f"Name:{name} , Phone Number:{phone_number}")
else:
    print("Name not found")