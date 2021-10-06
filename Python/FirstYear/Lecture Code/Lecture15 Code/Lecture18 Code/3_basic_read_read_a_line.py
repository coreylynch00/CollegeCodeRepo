'''
Purpose: Reading a line at a time from the file
Returns a line including the '\n' character
'''
with open("tempstrings.txt") as newfile:
    filedata = newfile.readline()
    print(filedata)
    filedata = newfile.readline()
    print(filedata)
    filedata = newfile.readline()
    print(filedata)

