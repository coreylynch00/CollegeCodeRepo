# Corey Lynch - SD2A - Task 1

# Sample List = “farshad”, “ghassemi?d”, “madam”, “?radar?”, “duration”, “con?tained”

# Create empty list
my_list = []

# Take user input to determine size of list
n = int(input("How many elements in the list: "))

# Loop user input based on size of list
for i in range(0, n):
    item = str(input("Enter a string: "))

    # Append user string to list
    my_list.append(item)

# Function for checking if string contains question mark
def question_mark_check(my_list):
    print("\nQuestion Mark Check:")
    # Loop through list, if list contains specified character, print message with the list string 
    for item in my_list:
        if "?" in item:
            print(item + " contains a question mark!")

    print("\n")
    # Loop through list, if list DOES NOT contain specified character, print message with the list string 
    for item in my_list:
        if "?" not in item:
            print(item + " does not contain a question mark!")

# Function for checking frequency of character in strings within list
def character_check(my_list):
    print("\nCharacter Check:")
    # Create empty character dictionary to store occurances of chars
    char_freq = {}
    # For loop to loop through each item in the list
    for i in my_list:
        # Nested for loop to loop though each character of each string within the list
        for c in i:
            # If char is in String, increment count by 1
            if c in char_freq:
                char_freq[c] += 1
            # If char is not in String, do not increment count
            else:
                char_freq[c] = 1
    # For loop to get char and count from char_freq dictionary
    for char, count in char_freq.items():
        # Format the print statement to make the result of the dictionary legible
        print("Character {} Appears {} Times.".format(char, count))

# Call functions
question_mark_check(my_list)
character_check(my_list)

