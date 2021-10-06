mark = int(input("What mark did you get? "))

if 0 <= mark < 40:
    print("Fail")
elif 40 <= mark < 70:
    print("Competent")
elif 70 <= mark <= 100:
    print("Outstanding")
else:
    print("Invalid mark entered")
