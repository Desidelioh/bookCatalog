import readBooks, addBooks, updateBooks, deleteBooks, reports
import time

#Function with a return statement
def menuChoices():

    choices = 0 #flag variable
    
    #iteration
    choiceList = ["1","2","3","4","5","6"]

    userChoices = "Books Menu Options\nEnter:\n1. Print\n2. Add\n3. Update\n4. Delete\n5. Reports\n6. Exit"

    while choices not in choiceList:
        print(userChoices)
        choices = input("Enter a number from the Books menu above: ")
        
        #selection
        if choices not in choiceList:
            print(f"{choices} is not a valid entry {time.sleep(3)}")
    return choices

# reports options
def reportOptions():
    options = 0 #flag variable
    
    #iteration
    optionList = ["1","2","3","4","5","6","7"]

    userOptions = "Reports Menu Options\nEnter:\n1. BookID\n2. Title\n3. Author\n4. Genre\n5. Country\n6. Publication Year\n7. Exit"

    while options not in optionList:
        print(userOptions)
        options = input("Enter a number from the Reports menu above: ")
        
        #selection
        if options not in optionList:
            print(f"{options} is not a valid entry {time.sleep(3)}")
    return options


#create aboolean variable
mainProgram = True
while mainProgram:
    #passing the function to a variable
    mainMenu = menuChoices()

    #invoke the respective modules and function for each choice
    if mainMenu == "1":
        readBooks.read()
    elif mainMenu == "2":
        addBooks.insert()
    elif mainMenu == "3":
        updateBooks.update()
    elif mainMenu == "4":
        deleteBooks.delete()
    elif mainMenu == "5":
        #reports.title
        reportsProgram = True
        while reportsProgram:
            reportsMenu = reportOptions()
            if reportsMenu == "1":
                reports.bookID()
                time.sleep(5)
            elif reportsMenu == "2":
                reports.title()
                time.sleep(5)
            elif reportsMenu == "3":
                reports.author()
                time.sleep(5)
            elif reportsMenu == "4":
                reports.genre()
                time.sleep(5)
            elif reportsMenu == "5":
                reports.country()
                time.sleep(5)
            elif reportsMenu == "6":
                reports.year()
                time.sleep(5)
            else:
                #re-assign the reportsProgram with a boolean False value
                reportsProgram = False
                input(f"Press press enter to exit menu {time.sleep(3)}")

    else:
        #re-assign the mainprogram with a boolean False value
        mainProgram = False
    input(f"Please press enter to exit {time.sleep(3)}")





