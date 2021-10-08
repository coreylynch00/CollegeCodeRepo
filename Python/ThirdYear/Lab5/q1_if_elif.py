# Lab 5 Q1

# Calculate area of 2 rectangles and compare

length1 = int(input("Enter the length 1: "))
width1 = int(input("Enter the width 1: "))
length2 = int(input("Enter the length 2: "))
width2 = int(input("Enter the width 2: "))


def calc_area(len, wid):
    area = len * wid
    return area


area1 = calc_area(length1, width1)
area2 = calc_area(length2, width2)

if area1 == area2:
    print(f"Areas are the same! Area1: {area1:.2f}cm, Area2: {area2:.2f}cm")
elif area1 > area2:
    print(f"Areas1 is greater! Area1: {area1:.2f}cm, Area2: {area2:.2f}cm")
else:
    print(f"Areas2 is greater! Area1: {area1:.2f}cm, Area2: {area2:.2f}cm")
