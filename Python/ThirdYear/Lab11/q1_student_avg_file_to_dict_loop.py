# Lab 11 Q1 A

# Read data from file and calculate average grade, store in dict and loop menu

def calc_avg():
    my_dict = dict()
    file = open("studentData", "r")
    for line in file:
        data = line.split()
        avg = (int(data[1])+int(data[2])+int(data[3]))/3
        name = data[0]
        my_dict[name] = avg

    cont = "y"
    while cont == "y":
        key = input("Enter student name: ")
        key = key.capitalize()
        if key in my_dict:
            print(my_dict[key])
        else:
            print("That person does not exist!")
        cont = input("Do you want to search for another? [y/n]: ")


calc_avg()