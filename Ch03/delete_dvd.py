#!/usr/bin/env python

import MySQLdb, os

#RUN THE SQL STATEMENT TO DELETE THE SELECTED RECORD
def SQLDeleteDVD(dvdToDelete):
    try:
        SQL_DELETE = "DELETE DVD FROM DVD WHERE DVD_TITLE = \"%s\"" % dvdToDelete
        db = MySQLdb.connect("localhost", "root", "zanzibar", "DVDCOLLECTION")
        c = db.cursor()
        c.execute(SQL_DELETE)
        db.commit()
        c.close()
        db.close()
        raw_input("Item deleted, press enter to continue:  ")
    except:
        print "THERE WAS A PROBLEM DELETING THE RECORD"
        raw_input("Press Enter to continue:  ") 


#TAKE USER INPUT AND RUN FUNCTION TO DELETE THE SELECTED RECORD
def DeleteDVD():
    
    os.system('cls')
    print "==============================="
    print "DELETE A DVD RECORD:"
    print "==============================="
    
    dvdToDelete = raw_input("\nEnter the title of the DVD to delete:\t")
    SQL_LOOKUP = "SELECT * FROM DVD WHERE DVD_TITLE = \"%s\"" % dvdToDelete

    try:
        db = MySQLdb.connect("localhost", "root", "zanzibar", "DVDCOLLECTION")
        c = db.cursor()
        c.execute(SQL_LOOKUP)
        searchResult = c.fetchall()
        if searchResult[0] == ():    
            raise
    except:
        print "THERE WAS A PROBLEM ACCESSING THE RECORD IN THE DATABASE!"
        raw_input("Press Enter to continue:  ")
        return
        
    print "==============================="
    print "DVD TO DELETE:"
    print "==============================="
    print "Title:\t", searchResult[0][0]
    print "Star:\t", searchResult[0][1]
    print "Costar:\t", searchResult[0][2]
    print "Year released:\t", searchResult[0][3]
    print "Genre:\t:", searchResult[0][4]
    print "==============================="
    print '''
    Are you sure you want to delete?  Enter a choice and press enter
    (Y/y = yes, Anything else = No)
    '''
    choice = raw_input("\t")
    
    if (choice == "Y" or choice == "y"):
        SQLDeleteDVD(dvdToDelete)
    else:
        c.close()
        db.close()
        raw_input("Item NOT deleted, press enter to continue:  ")
