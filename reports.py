from connect import * 

def bookID():
    idField = input("Enter the book ID to search for: ")
    dataCursor.execute(f"SELECT * FROM books WHERE BookID = '{idField}' ")
    #fetch all records from books table
    entries = dataCursor.fetchall()
    #iterate through all the records in the entries variable
    for anEntry in entries:
        print(anEntry)

def title():
    titleField = input("Enter the book title to search for: ")
    dataCursor.execute(f"SELECT * FROM books WHERE Title = '{titleField}' ")
    #fetch all records from books table
    entries = dataCursor.fetchall()
    #iterate through all the records in the entries variable
    for anEntry in entries:
        print(anEntry)

def author():
    authorField = input("Enter the name of the author to search for: ")
    dataCursor.execute(f"SELECT * FROM books WHERE Author = '{authorField}' ")
    #fetch all records from books table
    entries = dataCursor.fetchall()
    #iterate through all the records in the entries variable
    for anEntry in entries:
        print(anEntry)

def genre():
    genreField = input("Enter the book genre to search for: ")
    dataCursor.execute(f"SELECT * FROM books WHERE Genre = '{genreField}' ")
    #fetch all records from books table
    entries = dataCursor.fetchall()
    #iterate through all the records in the entries variable
    for anEntry in entries:
        print(anEntry)

def country():
    countryField = input("Enter the country to search for: ")
    dataCursor.execute(f"SELECT * FROM books WHERE Country = '{countryField}' ")
    #fetch all records from books table
    entries = dataCursor.fetchall()
    #iterate through all the records in the entries variable
    for anEntry in entries:
        print(anEntry)

def year():
    yearField = input("Enter the publication year to search for: ")
    dataCursor.execute(f"SELECT * FROM books WHERE yearReleased = '{yearField}' ")
    #fetch all records from books table
    entries = dataCursor.fetchall()
    #iterate through all the records in the entries variable
    for anEntry in entries:
        print(anEntry)

if __name__=="__main__":
    bookID()
    title()
    author()
    genre()
    country()
    year()
