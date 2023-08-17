from connect import * # import the connect.py module 

dataCursor.execute(""" 
CREATE TABLE "books" (
	"BookID"	INTEGER NOT NULL UNIQUE,
	"Title"		TEXT,
	"Author"	TEXT,
	"Genre"		TEXT,
    "Country"	TEXT,
    "yearReleased"	INTEGER,          
    PRIMARY KEY("BookID" AUTOINCREMENT)           
)""")


