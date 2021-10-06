directions = ('north', 'south', 'east', 'west')

direction = input("In which direction would you like to travel? ").lower()

while direction not in directions:
    direction = input("Invalid Option: In which direction would you like to travel? ").lower()

print("And off we go!")