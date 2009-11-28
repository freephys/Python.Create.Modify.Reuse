#!/usr/bin/env python

import MySQLdb, csv, os

#FUNCTION TO WRITE ENTIRE DVD LIST TO CSV
def WriteCSV():
    
    SQL = "SELECT * FROM DVD"
        
    try:
        db = MySQLdb.connect("localhost", "root", "zanzibar", "DVDCOLLECTION")
        c = db.cursor()
        c.execute(SQL)
        output = c.fetchall()
        c.close()
        db.close()
    except:
        print "THERE WAS A PROBLEM ACCESSING THE DATABASE!"
        raw_input("Press Enter to return to the menu:  ")
        return
    
    try:
        os.system('cls')
        print "==============================="
        print "EXPORT DATABASE TO CSV:"
        print "==============================="
        filename = raw_input("Enter base filename (will be given a .csv extension):  ")
        filename = filename + ".csv"
        writer = csv.writer(open(filename, "wb"))
        writer.writerow(("TITLE", "STAR NAME", "COSTAR NAME", "YEAR", "GENRE"))
        writer.writerows(output)
        print filename, " successfully written, press Enter to continue:  "
        raw_input("")
        return
    except:
        print "ERROR WRITING FILE!"
        raw_input("Press Enter to return to the menu:  ")
