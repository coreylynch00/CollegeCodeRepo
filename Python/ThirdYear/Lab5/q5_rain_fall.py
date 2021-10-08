# Lab 5 Q6

# Loop user input for rainfall and display stats

user_count = int(input("How many months of data would you like to enter: "))

rainfall_list = []

for i in range(user_count):
    rainfall = float(input(f"Enter the rainfall for Month {i+1}: "))
    rainfall_list.append(rainfall)

average = sum(rainfall_list) / len(rainfall_list)
highest = max(rainfall_list)
lowest = min(rainfall_list)

print(f"\n{rainfall_list}")

print(f"\nHighest rainfall: {highest:.2f}")
print(f"Lowest rainfall: {lowest:.2f}")
print(f"Average rainfall: {average:.2f}")
