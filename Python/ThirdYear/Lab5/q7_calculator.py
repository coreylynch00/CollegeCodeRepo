# Lab 5 Q7

# Calculator

value_one = int(input("Enter a numerical value: "))
value_two = int(input("Enter a numerical value: "))

print("\nWould you like to perform:\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n")

menu_choice = int(input("Enter your choice [1-4] >>> "))

if menu_choice == 1:
    ans = value_one + value_two
    print(f"\nAnswer: {ans}")
elif menu_choice == 2:
    ans = value_one - value_two
    print(f"\nAnswer: {ans}")
elif menu_choice == 3:
    ans = value_one * value_two
    print(f"\nAnswer: {ans}")
elif menu_choice == 4:
    ans = value_one / value_two
    print(f"\nAnswer: {ans}")
else:
    print("That is not a valid option")
