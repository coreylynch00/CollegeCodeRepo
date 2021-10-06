angle = int(input("What is the angle?"))

angle %= 360

if 0 <= angle < 90:
    print("First quadrant")
elif 90 <= angle < 180:
    print("Second quadrant")
elif 180 <= angle < 270:
    print("Third quadrant")
else:
    print("Fourth quadrant")