# Not actually a lab question, just did it for fun!

# Determine if number is a prime number

user_num = int(input("Enter a numerical value: "))
flag = False


def prime_number(num):
    # prime numbers are greater than 1
    if num > 1:
        # check for factors
        for i in range(2, num):
            if (num % i) == 0:
                print(num, "is not a prime number")
                print(i, "times", num // i, "is", num)
                break
        else:
            print(num, "is a prime number")

    # if input number is less than
    # or equal to 1, it is not prime
    else:
        print(num, "is not a prime number")


prime_number(user_num)