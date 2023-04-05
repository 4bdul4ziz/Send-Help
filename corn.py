import os
import datetime



# path to the folder containing the files
path = input("Enter the path to the folder: ")

#give options to enter past dates or current date
print("Enter 1 for current date or 2 for past date")
date = input("Enter your choice: ")

# if current date is selected
if date == "1":
    # get the current date
    today = datetime.date.today()
    # convert the date to string
    today = str(today)
    # split the date string into year, month and day
    year, month, day = today.split("-")
    # create the prefix
    prefix = year + "-" + month + "-" + day + "-"
    # get the list of files in the folder
    files = os.listdir(path)
    # loop through the files
    for file in files:
        # check if the file is a pdf file
        if file.endswith(".pdf") or file.endswith(".PDF"):
            print(file)
            #get new name
            new_name = input("Enter new name for " + file + ": ")
            # rename the file
            os.rename(os.path.join(path, file), os.path.join(path, prefix + new_name + ".pdf"))
        # if the file is not a pdf file, skip it
        else:
            continue

# if past date is selected
elif date == "2":
    # get the past date
    pastDate = input("Enter the past date in YYYY-MM-DD format: ")
    # split the date string into year, month and day
    year, month, day = pastDate.split("-")
    # create the prefix
    prefix = year + "-" + month + "-" + day + "-"
    # get the list of files in the folder
    files = os.listdir(path)
    # loop through the files
    for file in files:
        # check if the file is a pdf file
        if file.endswith(".pdf") or file.endswith(".PDF"):
            print(file)
            #get new name
            new_name = input("Enter new name for " + file + ": ")
            # rename the file
            os.rename(os.path.join(path, file), os.path.join(path, prefix + new_name + ".pdf"))
        else:
            continue

# if the user enters an invalid option
else:
    print("Invalid option")






