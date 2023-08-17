from connect import *
import readBooks
import time

#subroutine/function
def dataLoad():
    #load script books.sql 
    with open(r"Python_Project\books.sql") as sqlFile:
        transferData = sqlFile.read()
        dataCursor.executescript(transferData)
        dataCon.commit()

        time.sleep(3)
        readBooks.read()
    
if __name__=="__main__":
    dataLoad()