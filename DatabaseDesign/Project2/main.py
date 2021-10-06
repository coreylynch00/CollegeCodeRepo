# SD2-ALynchC
# Name: Corey Lynch
# Class: SD2-A
# Lecturer: Byton Treacy
########################################################################################################################
# Import sqlite3 module
import sqlite3
conn = sqlite3.connect("project.db")

c = conn.cursor()

# Create 1 instance of Customers table
# NOTE: This line of code is only executed once, once the table is created & exists, cannot be executed again.

# c.execute("""CREATE TABLE customers(fName text, lName text, telNo text, carReg text, carMake text, carModel text)""")
# conn.commit()

########################################################################################################################
# Print menu to user and ask for menu choice
print("Please choose an option from the menu:\n")

print("1. Edit table")
print("2. Display table")
print("3. Quit")

try:
    user_input = int(input("\n>>> "))

########################################################################################################################
# If user wants to edit the table | 1 = add data, 2 = delete data
    if user_input == 1:
        # Insert new data to table
        print("\n...EDITING TABLE...")
        print("[1] to insert new data | [2] to delete existing data")
        edit_input = int(input("\n>>> "))
        # If user wants to add new data:
        if edit_input == 1:
            fName = input("First Name: ")
            lName = input("Last Name: ")
            telNo = input("Contact Number: ")
            carReg = input("Vehicle Registration: ")
            carMake = input("Car Manufacturer: ")
            carModel = input("Car Model: ")

            c.execute("""INSERT INTO customers(fName, lName, telNo, carReg, carMake, carModel)
            VALUES (?,?,?,?,?,?)""", (fName, lName, telNo, carReg, carMake, carModel))
            conn.commit()
            print('Data entered successfully.')
            conn.close()

        # Delete data from table
        elif edit_input == 2:
            print("Enter the Vehicle Registration of the entry you would like to delete.")
            delete_by_reg = input(">>> ")
            c.execute("DELETE FROM customers WHERE carReg = (?)", (delete_by_reg,))
            conn.commit()
            print("Data deleted successfully.")
            conn.close()

        # Error Handling
        else:
            print("Error! Please choose option [1] or [2].")

########################################################################################################################
    # If user wants to display table to screen
    elif user_input == 2:
        # Display table
        print("...DISPLAYING TABLE...")
        c.execute("""SELECT * FROM customers""")
        rows = c.fetchall()

        for row in rows:
            print(row)

########################################################################################################################
    # User wants to quit the program
    elif user_input == 3:
        # Quit Program
        print("Thank you. Goodbye.")

########################################################################################################################
    # Error handling
    else:
        print("Error! Please choose an option [1-3].")
except ValueError:
    print("Error! Please choose an option [1-3].")

########################################################################################################################
