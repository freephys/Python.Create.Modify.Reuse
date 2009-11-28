#!/usr/bin/env python

import MySQLdb, os

#RUN THE SQL STATEMENT TO QUERY THE DATABASE
def SQLLookupDVD(searchby, searchtext):
    SQL = "SELECT * FROM DVD WHERE %s = %s" % (searchby, searchtext)
    try:
        db = MySQLdb.connect("localhost", "root", "zanzibar", "DVDCOLLECTION")
        c = db.cursor()
        c.execute(SQL)
        output = c.fetchall()
        c.close()
        db.close()
    except:
        print "THERE WAS A PROBLEM ACCESSING THE DATABASE"
        raw_input("Press Enter to continue:  ")
        return        
    os.system('cls')
    print "==============================="
    print "DVD SEARCH RESULTS:"
    print "==============================="
    if not output:
        print "NO RECORDS FOUND"
        print "==============================="
    for entry in output:
        print "Title:\t", entry[0]
        print "Star:\t", entry[1]
        print "Costar:\t", entry[2]
        print "Year:\t", entry[3]
        print "Genre:\t", entry[4]
        print "==============================="        
    raw_input("\n\nPress enter to continue:  ")

#TAKE USER INPUT AND RUN FUNCTION TO QUERY THE DATABASE
def LookupDVD():
    print """
    ===============================
    DVD LOOKUP:
    ===============================
    Enter the criteria to look up by:
    1 - Movie title
    2 - Star
    3 - Costar
    4 - Year released
    5 - Genre"""

    choice = raw_input("\nType a number and press enter:  ")    

    searchby = ""
    searchtext = ""
    if choice == "1":
        searchby = "DVD_TITLE"
        searchtext = raw_input("Enter the DVD title to search for:  ")
        searchtext = "\"%s\"" % (searchtext)
    elif choice == "2":
        searchby = "DVD_STAR_NAME"
        searchtext = raw_input("Enter the DVD star name to search for:  ")
        searchtext = "\"%s\"" % (searchtext)
    elif choice == "3":
        searchby = "DVD_COSTAR_NAME"
        searchtext = raw_input("Enter the DVD costar name to search for:  ")
        searchtext = "\"%s\"" % (searchtext)
    elif choice == "4":
        searchby = "DVD_YEAR"
        searchtext = raw_input("Enter the DVD release year to search for:  ")
        searchtext = "\"%s\"" % (searchtext)
    elif choice == "5":
        searchby = "DVD_GENRE"
        print """
        Enter the genre to search for:
        1 - Drama
        2 - Horror
        3 - Comedy
        4 - Romance
        """
        entrychoice = raw_input("\t")
        if entrychoice == "1":
            searchtext = "\"Drama\""
        elif entrychoice == "2":
            searchtext = "\"Horror\""
        elif entrychoice == "3":
            searchtext = "\"Comedy\""
        elif entrychoice == "4":
            searchtext = "\"Romance\""
    else:
        print "ERROR IN CHOICE!"
        raw_input("Press Enter to return to the menu:  ")
        return
    
    SQLLookupDVD(searchby, searchtext)
