angle = int(input("What is the angle?"))

if angle >= 0 and angle < 90:
    print("First quadrant")
elif angle > 90 and angle < 180:
    print("Second quadrant")
elif angle >= 180 and angle < 270:
    print("Third quadrant")
elif angle >= 270 and angle < 360:
    print("Fourth quadrant")
else:
    print("Invalid angle")