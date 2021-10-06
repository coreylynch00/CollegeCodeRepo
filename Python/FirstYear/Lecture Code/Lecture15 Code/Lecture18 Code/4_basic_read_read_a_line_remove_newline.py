'''
Purpose: Reading a line at a time from the file
Extra: Removes the '\n' character
'''

with open("tempstrings.txt") as newfile:
    filedata = newfile.readline().rstrip()
    print(filedata)
    filedata = newfile.readline().rstrip()
    print(filedata)
    filedata = newfile.readline().rstrip()
    print(filedata)
