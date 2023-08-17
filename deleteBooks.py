from connect import *
import readBooks
import time

#subroutine/function
def delete():
    #use primary key to delete a record
    idRecord = input("Enter the BookID of the record to be deleted: ")

    dataCursor.execute(f"DELETE FROM Books WHERE BookID = {idRecord}")
    dataCon.commit()

    print(f"Record {idRecord} has been deleted from the books table")

    #invoke the sleep method to delay execution 
    time.sleep(3)

    #invoke the read subroutine/function from the readBooks module
    readBooks.read()

    
if __name__=="__main__":
    delete()