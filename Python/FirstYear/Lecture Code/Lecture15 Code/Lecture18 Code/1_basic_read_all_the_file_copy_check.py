'''
Demonstrates reading from a file.
Copying as before.
Extra: Ensuring the file does not already exists before we write
       to it and destroy it.
'''
import os

print("Read all file...")
with open("tempstrings.txt") as new_file:
    file_data = new_file.read()

name_of_file = input("What is the name of the file?")

while os.path.exists(name_of_file):
    print(name_of_file, "already exists.")
    name_of_file = input("What is the name of the file?")

with open(name_of_file, 'w') as output:
    output.write(file_data)

