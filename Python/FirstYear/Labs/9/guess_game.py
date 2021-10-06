# Corey Lynch 21/11/2019

import random

random_number = random.randint(1, 2)
user_guess = int(input("Guess a number between 1 and 2 - "))

if user_guess == random_number:
    print(f"You have guessed correctly! The number was {random_number}")
else:
    print(f"You have guessed incorrectly! The number was {random_number}.")
