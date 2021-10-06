file = open("names.txt")

for name in file:
    print(name.rstrip())

file.close()