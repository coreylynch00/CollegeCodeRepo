'''
Demonstrates reading from a file.
Copying the file by reading the whole file as a string then writing that string
to an output file, whose name is chosen by the user.
'''
print("Read all file...")
with open("tempstrings.txt") as new_file:
    file_data = new_file.read()

name_of_file = input("What is the name of the file?")
with open(name_of_file, 'w') as output:
    output.write(file_data)
