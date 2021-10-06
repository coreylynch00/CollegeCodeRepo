availableData = int(input("How much data did you purchase?"))
warningLevel = int(input("When would you like to trigger a warning?"))

while availableData > warningLevel:
    usageToday = int(input("How much data did you use today?"))
    availableData -= usageToday
    print("You have " + str(availableData) + "MB left.")

if availableData < 0:
    print("OOPS - you used up your data before I could warning you")
else:
    print("WARNING - you are about to reach your usage limit")