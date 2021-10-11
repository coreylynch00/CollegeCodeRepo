# Lab 5 Q6

# Generate fibonacci sequence

fibonacci_numbers = [0, 1]
for i in range(2, 40):
    fibonacci_numbers.append(fibonacci_numbers[i-1]+fibonacci_numbers[i-2])

index = int(input("Enter the sequence number you would like to display: "))
print(fibonacci_numbers[index-1])
