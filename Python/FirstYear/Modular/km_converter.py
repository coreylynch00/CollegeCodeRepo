speed = int(input("Input a speed in MP/H: "))

def speed_converter(spd):
    kmh = speed * 1.6
    print("KMH:")
    print(f"{kmh:.2f}")
    return spd

speed1 = speed_converter(speed)