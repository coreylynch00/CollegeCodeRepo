# Introducting read(integer)
# 6_basic_read_readlines.py
# Read first 6 characters from the file then the rest of the file

with open("tempstrings.txt") as newfile:
    # read first 6 characters from the file
    filedata = newfile.read(6)
    print("The first 6 characters....")
    print(filedata)

    # Read the rest of the file
    print("\nThe rest of the file....")
    filedata = newfile.read()
    print(filedata)



