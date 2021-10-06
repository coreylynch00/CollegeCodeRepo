# Corey Lynch - Final Exam
# Did not have time to get loop working
# Ran out of time for the bash questions, my time management was extremely poor and spent far too much time on this task, sorry for this.

# Create initial dict of PPS and results
people_dict = {
    "r12345" : "Positive",
    "r09876" : "Negative",
    "r34567" : "Positive",
    "r01845" : "Negative",
    "r34587" : "Positive"
}

# Initialize loop variable
#active = True

# User menu option
option = input("\n1. Enter 'PPS' to search or add a PPS result. \n2. Enter 'Sick' to view all positive cases. \n3. Enter 'Healthy' to see negative cases. \n***USE CAPS***>>> ")


#while active:
# If user input = "PPS"
if option == 'PPS':
    pps = str(input("Input a PPS Number: "))
    # If pps number is already in the dictionary, print the pps number and corrosponding result
    if pps in people_dict:
        print("\nPPS Entered: " + pps + "\n" + "Test Result: " + people_dict.get(pps))

    # If pps is not in the dict, ask the user if they would like to add the pps and result
    if pps not in people_dict:
        ans = input("\nThat PPS has not yet been added. Would you like to add a result? y/n: ")
        # If user wants to add, ask for the result for the inputted pps and append both the pps and result to the dict
        if ans == "y":
            result = str(input("What is the test result? "))
            people_dict[pps] = result
            print("The database has been sucessfully updated.")
        # Exit is user selects not to add to dict
        if ans == "n":
            print("OK. Thank You and Goodbye.")
            SystemExit(0)
            #active = False
    print("\n", people_dict)

# If user inputs sick, print all pps that are postive value
if option == 'SICK':
    # for loop to loop through each key and value 
    for key, value in people_dict.items():
        # If a value has a value of positive, print the key and value
        if "Positive" == value:
            # Format the print
            print(key,  " : ", value)
            #active = False

# If user inputs healthy, print all pps that are negative value
if option == 'HEALTHY':
     # for loop to loop through each key and value 
    for key, value in people_dict.items():
        # If a value has a value of negative, print the key and value
        if "Negative" == value:
            # Format the print
            print(key,  " : ", value)
            #active = False

# Exit if user inputs the exit command
if option == 'EXIT':
    print("Stay Safe and Goodbye.")
    #active = False

# Error statement for if a user does not input a valid command
else:
    print("That is not a valid option. Please choose an option from the menu.")
