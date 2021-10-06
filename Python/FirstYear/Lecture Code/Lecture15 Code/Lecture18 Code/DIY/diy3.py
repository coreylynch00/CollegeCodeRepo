file = open("names.txt")
t = open("T.txt","w")
for name in file:
    if name.startswith("T"):
        t.write(name)

file.close()
t.close()

print("A file named {} was created - please check its contents".format(t.name))
