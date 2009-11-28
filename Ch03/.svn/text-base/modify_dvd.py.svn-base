#!/usr/bin/env python

import MySQLdb

def ModifyDVD():
    
    print "==============================="
    print "MODIFY A DVD RECORD:"
    print "==============================="
    
    dvdTitle = raw_input("\nEnter the title of the DVD to modify:  ")
    
    SQL_LOOKUP = "SELECT * FROM DVD WHERE DVD_TITLE = \"%s\"" % dvdTitle
    
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
    
    try:    
        print "==============================="
        print "DVD TO MODIFY:"
        print "==============================="
        print "1 - Title:\t", searchResult[0][0]
        print "2 - Star:\t", searchResult[0][1]
        print "3 - Costar:\t", searchResult[0][2]
        print "4 - Year:\t", searchResult[0][3]
        print "5 - Genre:\t", searchResult[0][4]
        print "==============================="
        
        choice = raw_input("Type the number for the field \
        \nyou want to modify and press Enter:  ")
        
        titleChanged = False
        modify = ""
        newvalue = ""
        if choice == "1":
                modify = "DVD_TITLE"
                newvalueTitle = raw_input("Enter the new DVD title name:  ")
                newvalue = "\"%s\"" % newvalueTitle
                titleChanged = True
        elif choice == "2":
            modify = "DVD_STAR_NAME"
            newvalue = raw_input("Enter the new DVD star name:  ")
            newvalue = "\"%s\"" % newvalue
        elif choice == "3":
            modify = "DVD_COSTAR_NAME"
            newvalue = raw_input("Enter the new DVD costar name:  ")
            newvalue = "\"%s\"" % newvalue
        elif choice == "4":
            modify = "DVD_YEAR"
            newvalue = raw_input("Enter the new DVD year of release:  ")
            newvalue = "\"%s\"" % newvalue
        elif choice == "5":
            modify = "DVD_GENRE"
            print "==============================="       
            print "Enter the genre to apply to this DVD:"
            print "1 - Drama"
            print "2 - Horror"
            print "3 - Comedy"
            print "4 - Romance"
            
            entrychoice = raw_input("Type the number for the genre \
            \nyou want to apply and press Enter:  ")
            if entrychoice == "1":
                newvalue = "\"Drama\""
            elif entrychoice == "2":
                newvalue = "\"Horror\""
            elif entrychoice == "3":
                newvalue = "\"Comedy\""
            elif entrychoice == "4":
                newvalue = "\"Romance\""
    
        SQL_UPDATE = "UPDATE DVD SET %s = %s WHERE DVD_TITLE = \"%s\"" \
                     % (modify, newvalue, dvdTitle)
            
        db = MySQLdb.connect("localhost", "root", "zanzibar", "DVDCOLLECTION")
        c = db.cursor()
        c.execute(SQL_UPDATE)
        db.commit()
        
        if titleChanged:
            SQL_LOOKUP = "SELECT * FROM DVD WHERE DVD_TITLE = \"%s\"" % newvalueTitle
            
        c = db.cursor()
        c.execute(SQL_LOOKUP)
        modifyResult = c.fetchall()
        c.close()
        db.close()
    except:
        print "THERE WAS A PROBLEM MODIFYING THE RECORD"
        raw_input("Press Enter to continue:  ")
        return
    
    print "==============================="
    print "MODIFIED RECORD:"
    print "==============================="
    print "1 - Title:\t", modifyResult[0][0]
    print "2 - Star:\t", modifyResult[0][1]
    print "3 - Costar:\t", modifyResult[0][2]
    print "4 - Year:\t", modifyResult[0][3]
    print "5 - Genre\t", modifyResult[0][4]
    print "==============================="
    raw_input("Press enter to continue:  ")
