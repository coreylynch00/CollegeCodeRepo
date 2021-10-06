ok = False

while not ok:
    exam = float(input("Exam result [0-100] >>> "))
    if 0 <= exam <= 100:
        ok = True
