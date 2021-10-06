# Corey Lynch - R00154863 - 21/11/2019
########################################################################################################################
user_name = input("Please enter your name: ")
user_name = user_name.capitalize()                                                       # Reassign as .cap
print(f"\nHey {user_name}, choose from one of the options below.")                       # Code for print menu

try:
    main_menu_choice = 5
########################################################################################################################
    while main_menu_choice != 3:
        print("\n1. Add a new hero.")
        print("2. View details of a hero.")
        print("3. Quit program.")
        main_menu_choice = int(input("Enter your choice [1-3]:"))
        if main_menu_choice == 1:                                                              # Code for menu choice 1

            print("\nPlease enter the hero's details below.")

            print("[Hit ENTER now to quit.]")
            hero_name = input("What is the name of the hero you would like to add?")      # Variables & reassign as .cap
            hero_name = hero_name.capitalize()

            hero_power = input("\U0001F4AA What is this hero's superpower?")
            hero_power = hero_power.capitalize()

            hero_alter_ego = input("\U0001F910 What is this hero's alter-ego/AKA?")
            hero_alter_ego = hero_alter_ego.capitalize()

            hero_birth_place = input("\U0001F30D Where is this hero from?")
            hero_birth_place = hero_birth_place.capitalize()

            hero_universe = input("\U0001F4D6 Is this hero from the Marvel or DC universe?")
            hero_universe = hero_universe.capitalize()

            if hero_universe.lower() == "marvel":                                          # Determine new hero file
                with open("marvel.txt", "a") as marvel_file:                               # Print hero to selected file
                    print(hero_name, sep="", file=marvel_file)
            elif hero_universe.lower() == "dc":
                with open("dc.txt", "a") as dc_file:
                    print(hero_name, sep="", file=dc_file)

            with open(hero_name + ".txt", "w") as new_output_file:                       # Writing data to new hero file
                print(f"Name: {hero_name} \nPowers: {hero_power} \nAlter-ego: {hero_alter_ego} \nOrigin:"
                      f" {hero_birth_place}", sep="",  file=new_output_file)
########################################################################################################################
        elif main_menu_choice == 2:                                                             # Code for menu choice 2
            print("\nWhich Superhero Universe would you like to view?")                         # Select which universe
            print("1. DC Comics")
            print("2. Marvel Comics")
            universe_choice = int(input("Enter your choice [1-2]:"))

            if universe_choice == 1:                                                            # If DC selected
                print("\nSelect a hero from the DC Universe...")                                # Print hero's in DC.txt
                with open("dc.txt") as dc_file_connection:
                    for line in dc_file_connection:
                        print(line.rstrip())
                    dc_hero_choice = input("Enter the name of the hero:\n")
                    with open(dc_hero_choice + ".txt", "r") as file_connection:         # Search for file hero_name.txt
                        for line in file_connection:                                    # Print file with hero data
                            print(line.rstrip())

            elif universe_choice == 2:                                                   # If Marvel selected
                print("\nYou have selected Marvel Comics Universe...")                   # Print hero's in Marvel.txt
                with open("marvel.txt") as marvel_file_connection:
                    for line in marvel_file_connection:
                        print(line.rstrip())
                    marvel_hero_choice = input("Enter the name of the hero:\n")
                    with open(marvel_hero_choice + ".txt", "r") as file_connection:     # Search for file hero_name.txt
                        for line in file_connection:                                    # Print file with hero data
                            print(line.rstrip())

            else:                                                                       # Error - input not 1 or 2
                print("You must choose either options [1-2].")
########################################################################################################################
        elif main_menu_choice == 3:                                                     # Code for menu choice 3
            print(f"\nThanks for stopping by {user_name}! \U0001f604 Here are some fun stats to take with you...")

            marvel_total_hero = len(open("marvel.txt").readlines())                       # Calc. total no. of hero's
            dc_total_hero = len(open("dc.txt").readlines())
            all_total_hero = marvel_total_hero + dc_total_hero
            print(f"\nTotal number of hero's in the database: {all_total_hero:>2} hero's")

            marvel_percentage = marvel_total_hero / all_total_hero * 100                   # Calc. and print Marvel %
            print(f"Percentage of which are Marvel hero's: {marvel_percentage:>4.0f}%")

            dc_percentage = dc_total_hero / all_total_hero * 100                           # Calc. and print DC %
            print(f"Percentage of which are DC hero's: {dc_percentage:>8.0f}%")

            with open("marvel.txt", "r") as marvel_file_connection:                        # Calc. longest Marvel name
                marvel_longest_name = ""
                marvel_longest_name = marvel_longest_name.rstrip()
                for line in marvel_file_connection:
                    line = line.rstrip()
                    line_length = len(line)
                    if line_length > len(marvel_longest_name):
                        marvel_longest_name = line

            with open("dc.txt", "r") as dc_file_connection:                                  # Calc. longest DC name
                dc_longest_name = ""
                dc_longest_name = dc_longest_name.rstrip()
                for line in dc_file_connection:
                    line_length = len(line)
                    if line_length > len(dc_longest_name):
                        dc_longest_name = line

            if len(marvel_longest_name) == len(dc_longest_name):                            # Compare Marvel & DC names
                print(f"Longest hero names: {marvel_longest_name} and {dc_longest_name}")   # and print largest/equal
            elif len(marvel_longest_name) > len(dc_longest_name):
                print(f"Longest hero name: {marvel_longest_name}")
            else:
                print(f"Longest hero name: {dc_longest_name}")

            with open("marvel.txt", "r") as marvel_file_connection:                         # Calc. shortest Marvel name
                marvel_shortest_name = ""
                marvel_shortest_name = marvel_shortest_name.rstrip()
                first_marvel_name = True
                for line in marvel_file_connection:
                    line = line.rstrip()
                    line_length = len(line)
                    if line_length < len(marvel_shortest_name) or first_marvel_name:
                        marvel_shortest_name = line
                        first_marvel_name = False

            with open("dc.txt", "r") as dc_file_connection:                                 # Calc. shortest DC name
                dc_shortest_name = ""
                dc_shortest_name = dc_shortest_name.rstrip()
                first_dc_name = True
                for line in dc_file_connection:
                    line = line.rstrip()
                    line_length = len(line)
                    if line_length < len(dc_shortest_name) or first_dc_name:
                        dc_shortest_name = line
                        first_dc_name = False

            if len(marvel_shortest_name) == len(dc_shortest_name):                           # Compare Marvel & DC names
                print(f"Shortest hero names: {marvel_shortest_name} and {dc_shortest_name}")   # and print largest/equal
            elif len(marvel_shortest_name) < len(dc_shortest_name):
                print(f"Shortest hero name: {marvel_shortest_name}")
            else:
                print(f"Shortest hero name: {dc_shortest_name}")
########################################################################################################################
        else:                                                                               # Excepts - error handling
            print("You must choose between options [1-3].")
except ValueError:
    print("You must input an option from the menu [1-3].")
except FileNotFoundError:
    print("This file doesn't seem to exist.")
except IOError:
    print("There seems to have been an error. Please restart the program!")
########################################################################################################################
