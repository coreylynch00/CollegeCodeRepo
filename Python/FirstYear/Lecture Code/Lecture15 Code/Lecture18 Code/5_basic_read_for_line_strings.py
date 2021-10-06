'''
Demonstrate using for loop to iterate through a file
line by line.

Makes a copy of a file but the copy is all uppercase letters.
'''

with open("tempstrings.txt") as newfile:
    for line in newfile:
        print(line.rstrip())


