# Corey Lynch - SD2A - Task 2

# Import random library
import random

# Create empty user list 
user_list = []
# Create boolean variable for while loop
active = True


# Function to remove a random item from a list and return a tuple
def random_list_remove(list, value):

    # Print the original list
    print(f"\n\tTHE ORIGINAL LIST: {list}")

    # For loop to generate the a number of random numbers which matches the users specification
    ##### NOTE: Use _ in the for loop instead of i to eliminate unused variable warning #####
    for _ in range(0, value):
        # Create variable called index to store the random number in the range 1 to 4
        index = random.randint(1, 4)
        # Pop the random number named index from the list
        list.pop(index)
        
        ##### NOTE: I HAVE COMMENTED OUT CODE FOR TESTING BELOW, UNCOMMENT TO SEE RESULT #####
        # Print the result each time it loops
        #print(f"The random number generated: {index}")
        #print(f"The updated list after index {index} is deleted: {list}\n")

    # Convert list to type Tuple and print the result
    print(f"\n\tTHE RESULT TUPLE: {tuple(list)}\n")

# While loop to loop menu if input is invalid
while active:
    # Take user input to determine size of list
    n = int(input("How many elements would you like in the list? (At least 12 items): "))

    # Check to ensure the users list is at least 12 items
    if (n < 12):
        print("The list must have at least 12 items")
        continue

    # For loop to keep asking user to input an item until list = 12
    ##### NOTE: Use "_" in the for loop instead of "i" to eliminate unused variable warning #####
    for _ in range(0, n):
        item = str(input("Enter a list item: "))
        
        # Append the new item to user_list
        user_list.append(item)

    # New boolean variables for nested while loop
    active1 = True
    # Nested while loop to loop menu if input is invalid
    while active1: 
        # User input to determine how many random numbers they would like to generate
        user_value = int(input("How many random numbers would you like to generate? (In range 2-6): "))

        # Check to ensure user input is not less that 2
        if (user_value in range(2, 7)):
            
            # If all user inputs are valid then call the function
            random_list_remove(user_list, user_value)

        else:
            print("Range must be between 2 and 6!")
            continue

# Break out of the while loop
        active1 = False
    active = False

