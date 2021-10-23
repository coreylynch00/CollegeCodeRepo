# Lab 11 Q1

# Read data from file and calculate average grade

# Open file
file = open("studentData.txt", "r")

# Iterate through each line
for line in file:
    # Split each item into separate strings - (name and 3 grades)
    data = line.split()
    # Get student name - index 0 = name
    name = data[0]
    # Calculate average - index 1 = grade 1, index 2 = grade 2, etc
    avg = (int(data[1])+int(data[2])+int(data[3]))/3
    # Print data
    print(name, avg)

# Close file
file.close()

