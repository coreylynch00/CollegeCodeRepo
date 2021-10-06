# Author: Cliona McGuane
# Demonstration of appending to a file
with open("famousfive.txt", 'a') as more_data:
    print("Timmy the dog", file=more_data)

