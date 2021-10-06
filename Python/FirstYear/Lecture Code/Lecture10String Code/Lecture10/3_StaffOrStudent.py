id = str(input("CIT ID > "))

if id.startsWith("RSSS"):
    print("You are a member of staff")
elif id.startsWith("R"):
    print("You are a student")
else:
    print("Invalid CIT ID")