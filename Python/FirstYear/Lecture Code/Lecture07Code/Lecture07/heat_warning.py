celsius = float(input("What is the Celsius temperature? "))
fahrenheit = 9 / 5 * celsius + 32
print("The temperature is", fahrenheit, "degrees fahrenheit.")
if fahrenheit >= 90:
    print("It's really hot out there, be careful!")
    print("Turn off the heat")
if fahrenheit <= 30:
    print("Brrrrr. Be sure to dress warmly")
    print("Turn up the heat")
