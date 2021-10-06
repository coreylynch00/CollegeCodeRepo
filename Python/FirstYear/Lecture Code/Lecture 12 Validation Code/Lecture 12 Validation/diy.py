NUMBER_OF_AGES = 5
count = 1
sum = 0
while count <= NUMBER_OF_AGES:
    while True:
        try:
            age = int(input("What is your age? "))
            if age >= 0:
                break
        except ValueError:
            print("Integers only please")
    count += 1
    sum += age
average = sum / NUMBER_OF_AGES
print("Average age = {}".format(average))


