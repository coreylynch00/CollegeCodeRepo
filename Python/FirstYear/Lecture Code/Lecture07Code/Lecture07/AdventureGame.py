menu = "There's a giant bear here eating a cheese cake.  "
menu += "What do you do?"
menu += "\n1. Take the cake."
menu += "\n2. Scream at the bear.\n>"

bear = input(menu)

if bear == "1":
    print("The bear eats your face off.  Oops!")
elif bear == "2":
    print("The bear eats your legs off.  Oops!")
else:
    print("Well, doing " + str(bear)
          + " is a good idea.....bear runs away.")

