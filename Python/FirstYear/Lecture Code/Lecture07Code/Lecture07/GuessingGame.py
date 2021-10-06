import random

MIN = 1
MAX = 10
number = random.randint(MIN, MAX)

guess = int(input("Please guess a number between "
                  + str(MIN) + " and " + str(MAX)))

if guess > number:
    print("Too big!")
elif guess < number:
    print("Too small!")
else:
    print("Yippee!!! You guessed it")