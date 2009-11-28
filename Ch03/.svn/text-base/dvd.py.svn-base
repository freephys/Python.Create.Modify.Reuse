#!/usr/bin/env python

import os
import add_dvd
import lookup_dvds
import modify_dvd
import delete_dvd
import csvreport_dvd

#MAIN MENU
def Menu():
    os.system('cls')
    print """
    ================================
    DVD DATABASE
    ================================
    1 - Add a DVD to the database
    2 - Search inventory
    3 - Modify DVD record
    4 - Delete DVD record
    5 - Export listing to CSV
    6 - Exit
    ================================
    """
    choice = raw_input("Enter a choice and press enter:  ")
    return choice

#TAKE CHOICE AND LAUNCH MODULE
choice = ""
while choice != "6":    
    choice = Menu()
    if choice == "1":
        os.system('cls')
        add_dvd.AddDVD()
    elif choice == "2":
        os.system('cls')
        lookup_dvds.LookupDVD()
    elif choice == "3":
        os.system('cls')
        modify_dvd.ModifyDVD()
    elif choice == "4":
        delete_dvd.DeleteDVD()
    elif choice == "5":
        csvreport_dvd.WriteCSV()
