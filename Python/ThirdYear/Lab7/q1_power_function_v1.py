# Lab 7 Q1

# Calculate power of base number from user input

# def power_v1():
#    base = int(input("Enter a base number: "))
#    power = int(input("Enter a power number: "))
#    ans = base ** power
#    print(f"The value {base} raised to the power of {power} is {ans}")
# def main():
#    power_v1()
# main()

def power_v1(base, power, ans):
    print("The value of ", base, " raised to the power of ", power, " is: ", ans)


def main():
    base = int(input("Please enter a base number: "))
    power = int(input("Please enter a power: "))
    ans = base ** power

    power_v1(base, power, ans)


main()