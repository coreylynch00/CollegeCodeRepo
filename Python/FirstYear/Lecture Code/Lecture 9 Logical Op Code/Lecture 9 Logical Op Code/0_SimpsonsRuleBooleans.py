number = int(input("What is the number?"))

positive = number > 0   # True if positive - otherwise False
even = number % 2 == 0  # True if divisible by 2 with no
                        # remainder i.e. even - otherwise False

if even and positive:
    print("This number is acceptable - programming proceeding....")
    print("Program would now go on to do more stuff....")
else:
    print("This number is unacceptable - programming terminating....")