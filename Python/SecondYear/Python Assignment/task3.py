# Corey Lynch - SD2A - Task 3

# While loop to loop user input if they do not input an int
while True:
    # Ensure user inputs an int only
    try:
        user_number = int(input("Enter a number: "))
        # If user successfully inputs an int, break out of loop and continue
        break
    # Print error message below if user does not input int
    except:
        print("You must enter a number!")
        
# Reducer function to carry out the arithmetic
def reducer(number):
    # If number reaches the value of 1, the program is finished
    if number == 1:
        print("Complete!")
        return
    # If the modulus of number divided by 2 IS 0, then the number is an even number
    # If this is the case than divise the number by 2
    elif (number % 2) == 0:
        number=number // 2
        print(number)
    # If the modulus of number divided by 2 IS NOT 0, then the number is an odd number
    # If this is the case, the multiply the number by 3 and add 1
    elif (number % 2) != 0:
        number = (number * 3) + 1
        print(number)
    # Call the function within the function for recursion
    reducer(number)
# Call the function
reducer(user_number)
