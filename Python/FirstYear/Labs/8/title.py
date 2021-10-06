# Corey Lynch 14/11/19

email = input("Please enter your email address.")
number_of_people = int(input("Enter the number of people in the group."))

try:
    with open(email + ".txt", "w") as output_file:

        for i in range(number_of_people):
            name = input("Enter your name.")

            while True:
                try:
                    print("Choose your title.")
                    print("\t1. Mr.")
                    print("\t2. Ms")
                    print("\t3. Mrs")
                    print("\t4. Other")

                    title_choice = int(input(">>>"))

                    if 1 <= title_choice <= 4:
                        break
                except ValueError:
                    print("You must enter a number between 1 and 4")

            if title_choice == 1:
                title = "Mr."
            elif title_choice == 2:
                title = "Ms."
            elif title_choice == 3:
                title = "Mrs."
            else:
                title = input("Please enter user title.")

            print(title, name, file=output_file)

except IOError:
    print("Error")
