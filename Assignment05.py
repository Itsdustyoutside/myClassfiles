# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# Dstrop,2.21.2020,Created  script
# added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = None # An object that represents a file
strFile = 'ToDoList.txt'
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A dictionary that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strTask = "" # A capture for the users task
strPriority = "" # A capture for the users priority



# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python Dictionaries rows like Lab 5.2
# TODO: Add Code Here

#dicRow1 = {"Task":'Sweep' , "Priority": 'High'}
#dicRow2 = {"Task": 'Mop', 'Priority': 'Low'}
#lstTable = [dicRow1, dicRow2]

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user

while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks

    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        objFile = open(strFile, 'r')
        for row in objFile:
            lstRow = row.split(',')
            dicRow = {'Task':lstRow[0], 'Priority':lstRow[1].strip('\n')}
            lstTable.append(dicRow)
        objFile.close()
        for objRow in lstTable:
            print(objRow)


    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        # TODO: Add Code Here
        strTask = input("Enter a task: ")
        strPriority = input("Enter a priority: ")
        dicRow = {"Task": strTask, "Priority": strPriority.strip()}
        lstTable.append(dicRow)
        for objRow in lstTable:
            print(objRow)
        continue

    # Step 5 - Remove a new item to the list/Table
    elif (strChoice.strip() == '3'):
        # TODO: Add Code Here
        objFile = open('C:\_Pythonclass\Assignment05\ToDoList.txt', 'r')
        lstTable.remove(dicRow)
        print('You have deleted the last task you entered!')
        continue

    # Step 6 - Save tasks to the ToDoList.txt file
    elif (strChoice.strip() == '4'):
        # TODO: Add Code Here
        objFile = open('C:\_Pythonclass\Assignment05\ToDoList.txt', 'a')
        objFile.write(strTask + ',' + strPriority)
        objFile.close()
        print('Your entry has been saved')
        continue

    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        print('To exit press Enter')
        break  # and Exit the program
