# Corey Lynch - SD2A - Task 4

# Import required modules
import os
import subprocess
import zipfile
import shutil

# Get current working directory and print it before the user takes any actions
path = os.getcwd()
print(f"\n> Current Working Directory: {path}")

# User input folder name they would like to create
folder_name = input("\nPlease enter the name of a folder: ")

# Create the subfolder names which are automatically created for the user
sub_folders = ["working", "backup"]
sub_sub_folders = ["pics", "docs", "movie"]
sub_sub_sub_folders = ["school", "party"]
files = ["CORONAVIRUS.txt", "DANGEROUS.txt", "KEEPSAFE.txt", "STAYHOME.txt", "HYGIENE.txt"]

# Function to create a folder structure starting with the provided user folder
def create_folder(folder):
    # Create the user specified folder
    try:
        # Allows dir to be made even if a dir of the same name exists - overwrites previous dir
        if not os.path.exists(folder):
            os.mkdir(folder)
    # Error handling
    except OSError:
        print(f"\n- Could not create directory {folder} in {path}")
    else:
        print(f"\n+ Successfully created directory {folder} in {path}")
    
    # Change directory to be inside the new user folder
    os.chdir(f"{path}\\{folder}")
    # Create a new path variable to store new directory and print to screen
    new_path = os.getcwd()
    print(f"\n\t> New Current Directory: {new_path}")

    # Create the "working" and "backup" folder within the user folder
    try:
        # For loop to loop through the list of folder names in the list sub_folders
        for folders in sub_folders:
            # Allows dir to be made even if a dir of the same name exists - overwrites previous dir
            if not os.path.exists(folders):
                os.mkdir(os.path.join(new_path, folders))
    # Error handling
    except OSError:
        print(f"\n- Could not create sub folders {sub_folders} in {new_path}")
    else:
        print(f"\n+ Successfully created sub folders {sub_folders} in {new_path}")
    
    # Change directory again to be inside the "working" folder
    os.chdir(f"{new_path}\\working")
    # Update the variable "new_path" with the new path
    new_path = os.getcwd()
    print(f"\n\t> New Working Directory: {new_path}")

    # Create new sub folders "docs", "pics", "movie" within "working" directory
    try:
        # For loop to loop through the list of folder names in the list sub_sub_folders
        for folders in sub_sub_folders:
            # Allows dir to be made even if a dir of the same name exists - overwrites previous dir
            if not os.path.exists(folders):
                os.mkdir(os.path.join(new_path, folders))
    # Error handling
    except OSError:
        print(f"\n- Could not create sub folders {sub_sub_folders} in {new_path}")
    else:
        print(f"\n+ Successfully created sub folders {sub_sub_folders} in {new_path}")
    
    # Change dir again to be inside the "docs" folder
    os.chdir(f"{new_path}\\docs")
    # Update the variable "new_path" with the new path
    new_path = os.getcwd()
    print(f"\n\t> New Working Directory: {new_path}")

    # Create new sub folders "school", "party" in current dir
    try:
        # For loop to loop through the list of folder names in the list "sub_sub_sub_folders"
        for folders in sub_sub_sub_folders:
             # Allows dir to be made even if a dir of the same name exists - overwrites previous dir
            if not os.path.exists(folders):
                os.mkdir(os.path.join(new_path, folders))
    # Error handling
    except OSError:
         print(f"\n- Could not create sub folders {sub_sub_sub_folders} in {new_path}")
    else:
         print(f"\n+ Successfully created sub folders {sub_sub_sub_folders} in {new_path}")
    
    # Create 5 .txt files, the names of the .txt files are stored in a list named "files"
    try: 
        # For loop to loop through the list of file names in the list "files"
        for file in files:
             # Allows file to be made even if a file of the same name exists - overwrites previous file
            if not os.path.exists(file):
                # Open the each file in the list
                f = open(file, "w+")
                # For loop to iterate through each line of the file and print the file line number to each file (increment by 1 after each line)
                for i in range(10):
                    f.write("This is line %d\r\n" %(i+1))
                # Close connection to files
                f.close()
    except OSError:
        print(f"\n- Could not create files {files} in {new_path}")
    else:
         print(f"\n+ Successfully created files {files} in {new_path}\n")

    # Print all items in current directory - proof files are all upper case with .txt (lower)
    items = os.listdir(new_path)
    print(f"> Original Items in DIR: {items}")

    # Write to single file - CORONAVIRUS.txt
    # Open file and specify mode 
    f = open("CORONAVIRUS.txt", "w")
    # Write to file
    f.write("Coronaviruses are a group of related RNA viruses that cause diseases in mammals and birds. In humans and birds, \
        they cause respiratory tract infections that can range from mild to lethal. ")
    # Close file conneciton
    f.close()

    # Append to single file - STAYHOME.txt
    # Open file and specify mode
    f = open("STAYHOME.txt", "a")
    # Write to file
    f.write("We're all in this together. Stay strong and stay home.")
    # Close file connection
    f.close()

# Function to rename files in "docs" folder
def rename_files(): 
    # Store the current directory in a variable named "path"
    path = os.getcwd()
    
    #For loop to loop through the list of file names
    for file in files:
        # Nested for loop to loop through files in the directory
        for file in os.listdir(path):
            # Rename the files to lowercase
            os.rename(path + "\\" + file, path + "\\" + file.lower())
            # Use the subprocess module to rename the .txt file extensions to .TXT
            subprocess.call('ren *.txt *.TXT', shell=True)
    
    # Print all renamed items in dir - proof all renamed to lower case with .TXT (upper)
    items = os.listdir(path)
    print(f"> Renamed Items in DIR: {items}\n")



# Function to backup "docs" folder - first create a zipped "backup" folder in "docs", then move the "backup" folder to the "backup" directory
def backup_files():

    new_path = os.getcwd()
    
    # Zip file name
    filename="docs_backup.zip"

    # Create zipfile object by opening file
    zip_object = zipfile.ZipFile(filename, "w", compression=zipfile.ZIP_DEFLATED)

    # Add "docs" files to the zip file
    zip_object.write("coronavirus.TXT")
    zip_object.write("dangerous.TXT")
    zip_object.write("hygiene.TXT")
    zip_object.write("keepsafe.TXT")
    zip_object.write("stayhome.TXT")
    zip_object.write("school")
    zip_object.write("party")

    # Close file object connection
    zip_object.close()

    # Move the zipped folder from "docs" folder to "backup" folder using the shutil module
    try:
        shutil.move(f"{new_path}\\docs_backup.zip", f"{path}\\{folder_name}\\backup")
    # Error handling
    except FileNotFoundError:
        print("Could not locate that file.")

    # Print out all items in the "docs" directory
    docs_items = os.listdir(new_path)
    print(f"> Items in the Folder 'docs': {docs_items}")

    # Change directory to the "backup" directory
    backup_dir = os.chdir(f"{path}\\{folder_name}\\backup\\")
    # Print out all the items within the "backup" directory
    backup_items = os.listdir(backup_dir)
    print(f"> Items in the Folder 'backup': {backup_items}")


# Call functions
create_folder(folder_name)
rename_files()
backup_files()
