'''
Demonstrates reading from a file.
The whole file is read as a single string.
'''
with open("tempstrings.txt", "r") as connection_to_file:
    file_data = connection_to_file.read()

print(file_data)


