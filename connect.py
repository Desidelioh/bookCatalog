import sqlite3 as sql #imported the sqlite3 module

dataCon = sql.connect("Python_Project/Library.db") #created database

dataCursor = dataCon.cursor() #Created cursor object and executed method to perform sql queries