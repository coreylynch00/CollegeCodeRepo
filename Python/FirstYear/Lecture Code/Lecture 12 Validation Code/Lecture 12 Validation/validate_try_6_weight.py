while True:
    try:
        weight = float(input("Weight (kg) >>> "))
        if weight > 0:
            break
    except ValueError:
        print("Numbers only please!")

print("Processing...")
