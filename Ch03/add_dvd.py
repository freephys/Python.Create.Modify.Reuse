#!/usr/bin/env python

import MySQLdb, random, os

#RUN THE SQL STATEMENT TO INSERT RECORD INTO DATABASE
def SQLAddDVD(Title, Star, Costar, Year, Genre):
    SQL = 'INSERT INTO DVD values ("%s", "%s", "%s", "%s", "%s")' % \
          (Title, Star, Costar, Year, Genre)
    try:
        db = MySQLdb.connect("localhost", "root", "zanzibar", "DVDCOLLECTION")
        c = db.cursor()
        c.execute(SQL)
        db.commit()
        c.close()
        db.close()
        raw_input("Record added - press enter to continue:  ")
    except:
        print "THERE WAS A PROBLEM ADDING THE RECORD"
        raw_input("Press Enter to continue:  ")

#TAKE USER INPUT AND RUN FUNCTION TO INSERT INTO DATABASE
def AddDVD():
    print "==============================="
    print "ADD A DVD TO THE DATABASE:"
    print "==============================="
    Title = raw_input("Enter the DVD title:  ")
    Star = raw_input("Enter the name of the movie's star:  ")
    Costar = raw_input("Enter the name of the movie's costar:  ")
    Year = raw_input("Enter the year the movie was released:  ")
    Genre = raw_input("Enter the genre:\n - 1 for Drama, 2 for horror, \
3 for comedy, 4 for romance:  ")
    if Genre == "1":
        Genre = "Drama"
    elif Genre == "2":
        Genre = "Horror"
    elif Genre == "3":
        Genre = "Comedy"
    elif Genre == "4":
        Genre = "Romance"
    else:
        print "ERROR ADDING RECORD!"
        raw_input("Press Enter to return to the menu:  ")
        return

    SQLAddDVD(Title, Star, Costar, Year, Genre)
