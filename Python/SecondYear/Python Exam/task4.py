# Corey Lynch - Final Exam 
# Did not have time to get the loop working
# Also did not understand about the sequence parameter. Not sure what the purpose of it was so left out.
# Ran out of time for the bash questions, my time management was extremely poor and spent far too much time on task 3, sorry for this.

# Function that modifies a string passed in depending on the criteria of the string
def input_function(string):
    # Get the length of the string 
    string_len = len(sentence.split())
    print("\nNumber of words in sentence: ", string_len)

    # If string length is less than 5, capitalize the first letter of each word
    if string_len < 5:
        print("\n", string.title())

    # If string length is greater than or equal to 5, only capitalize the first letter of the first word
    if string_len >= 5:
        cap_string = string.capitalize()
        print("\nThere were more than 5 words in your sentence. Only the first letter was capitalized.")
        print("\n", cap_string)

# Initialize the loop variable
#active = True

#While active:
#While loop will execute while active is = true, as soon as active is != true, it will break out of the loop
# Get user input (string)
sentence = input("Input a sentence: ")

#Get the length of the string again for checking
sentence_len = len(sentence.split())

# If the inputted string is less than or equal to 2, give an error
if sentence_len <= 2:
    print("The sentence must be more than 2 words.")

else:
    input_function(sentence)

#active no longer = true, therefore will break out of the while loop
#active = False