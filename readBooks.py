from connect import * # import the connect.py module 

#subroutine/function
def read():
    #select all records from books table
    dataCursor.execute("SELECT * FROM books")
    #fetch all records from books table
    entries = dataCursor.fetchall()
    #iterate through all the records in the entries variable
    for anEntry in entries:
        print(anEntry)

if __name__=="__main__":
    read()