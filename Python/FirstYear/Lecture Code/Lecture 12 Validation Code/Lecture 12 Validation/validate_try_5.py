while True:
    try:
        exam = float(input("Exam result [0-100] >>> "))
        if 0 <= exam <= 100:
            break
    except ValueError:
        print("Numbers only please!")

print("Processing...")
