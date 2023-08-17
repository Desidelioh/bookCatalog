from connect import *
import readBooks
import time

#subroutine/function
def update():
    #use primary key to update a record
    idRecord = input("Enter the BookID of the record to be updated: ")
    
    #field to be updated: Title, Author, Genre, Country, yearReleased
    recordName = input("Enter the field name (Title, Author, Genre, Country or yearReleased) to be updated: ")

    #user input of the value for the field to be updated
    recordValue = input(f"Enter the value for {recordName} field: ")

    #add single quotes to mirror the data format
    recordValue = "'" + recordValue + "'"

    #update the record in books table
    dataCursor.execute(f"UPDATE books SET {recordName} = {recordValue} WHERE BookID = {idRecord} ")
    #save changes to the database table permanently
    dataCon.commit()

    print(f"Record {idRecord}: {recordValue} has been updated in the books table")

    #invoke the sleep method to delay execution 
    time.sleep(3)

    #invoke the read subroutine/function from the readBooks module
    readBooks.read()

    
if __name__=="__main__":
    update()



