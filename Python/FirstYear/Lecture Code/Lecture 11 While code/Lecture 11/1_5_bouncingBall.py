FINAL_BOUNCE = 0.001
print("This program computers the number and height "
      "of the rebounds of a dropped ball")
bounceCount = 0
height = float(input("What is the starting height?"))
while height >= FINAL_BOUNCE:
    height /= 2
    bounceCount += 1
    print(f"Rebound #{bounceCount:<4d}:{height:10.6f}m")
