# Author: Cliona McGuane

# Open file for writing
output = open("famousfive.txt", 'w')
print("Julian", file=output)
print("Dick", file=output)
print("Anne", file=output)
print("Georgina (George)", file=output)
output.close()
