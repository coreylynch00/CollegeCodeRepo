# Lab 9 Q10

# Repeatedly enter names and ensure that names cannot be altered or updated later

name_list = []

for i in range(3):
    name = input("Please enter your name: ")
    name_list.append(name)

name_tuple = tuple(name_list)
print(type(name_list))
print(name_list)
print(type(name_tuple))
print(name_tuple)
