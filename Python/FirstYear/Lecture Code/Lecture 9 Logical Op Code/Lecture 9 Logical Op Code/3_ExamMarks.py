mark = int(input("What mark did you get? "))

if mark >= 0 and mark < 40:
    print("Fail")
elif mark >= 40 and mark < 70:
    print("Competent")
elif mark >= 70 and mark <= 100:
    print("Outstanding")
else:
    print("Invalid mark entered")
