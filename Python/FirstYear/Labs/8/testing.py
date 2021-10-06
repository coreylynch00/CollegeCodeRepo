# Corey Lynch 14/11/19

try:
    with open("testing.txt", "w") as output_file:
        try:
            DIVISION_SYMBOL = chr(247)
            x = float(input("Numerator >>>"))
            y = float(input("Denominator >>>"))
            division = x / y
            print(f"{x:.2f} {DIVISION_SYMBOL} {y:.2f} = {division:.4f}")
            print(f"{x:.2f} {DIVISION_SYMBOL} {y:.2f} = {division:.4f}", file=output_file)

        except ValueError:
            print("You must input a number.")
        except ZeroDivisionError:
            print("You cannot divide by 0.")
except IOError:
    print("Error")
