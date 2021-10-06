# Author: Cliona McGuane

# Open file for writing
# closes automatically
with open("famousfive.txt", 'w') as output:
    print("Julian", file=output)
    print("Dick", file=output)
    print("Anne", file=output)
    print("Georgina (George)", file=output)

