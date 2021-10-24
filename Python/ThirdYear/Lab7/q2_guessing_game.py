# Lab 7 Q2

# Guessing Game

import random


def gen_random_number():
    return random.randint(0, 100)


def ask_user():
    try:
        number = int(input("Please guess a number between 0 and 100: "))
        return number
    except ValueError:
        print("That is not a valid input!")
        exit(0)


def check_guess(user_guess, random_num):
    if user_guess == random_num:
        return True
    elif user_guess > random_num:
        print("Your guess is too high")
        return False
    else:
        print("Your guess is too low")
        return False


def main():
    correct_guess = False
    num_guesses = 0
    random_num = gen_random_number()

    while correct_guess == False:
        guess = ask_user()
        correct_guess = check_guess(guess, random_num)
        num_guesses += 1

    print("Congratulations. This is the correct guess")
    print("You made a total of ", num_guesses, " guesses")


main()
