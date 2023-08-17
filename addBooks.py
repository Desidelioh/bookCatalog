from connect import * # import the connect.py module 
import readBooks # import the readBooks.py module 
import time # import the time module

#subroutine/function
def insert():
    books = [] # create an empty list
    # ask for user input
    title = input("Enter book title: ")
    author = input("Enter author's full name: ")
    genre = input("Enter book genre: ")
    country = input("Enter country of origin: ")
    year = int(input("Enter year of publication: "))

    #save the user input into the variables of the books list
    books.extend([title, author, genre, country, year])

    #insert data saved in the books list into the books table
    dataCursor.execute("INSERT INTO books(Title, Author, Genre, Country, yearReleased) VALUES (?,?,?,?,?)", books)
    #save the changes to library database permanently
    dataCon.commit()

    print(f"{title} has been inserted into books")

    #invoke the sleep method to delay execution 
    time.sleep(3)

    #invoke the read subroutine/function from the readBooks module
    readBooks.read()

if __name__=="__main__":
    insert()

