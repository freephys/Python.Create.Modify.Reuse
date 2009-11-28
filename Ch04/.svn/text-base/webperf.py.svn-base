#!/usr/bin/env python

import webclient
import os

#MAIN MENU
def Menu():
    os.system('cls')
    print """
    ================================
    WEB PERFORMANCE TESTER
    ================================
    1 - Test client connection to external web sites
    2 - Test internal web server performance
    3 - Display log file
    4 - Exit
    ================================
    """
    choice = raw_input("Enter a choice and press enter:  ")
    return choice

#TAKE CHOICE AND LAUNCH MODULE
choice = ""
while choice != "4":    
    choice = Menu()
    if choice == "1":
        os.system('cls')
        sites = []
        siteresponse = raw_input("Enter the websites to check, separated by spaces:  ")
        sites = siteresponse.split
        webclient.checkExternalSites(sites)
    elif choice == "2":
        os.system('cls')
        servers = []
        print """
        Enter the ip addresses of the web servers
        running the Python webserver, seperated by spaces:  """
        serverresponse = raw_input("\t\t")
        servers = serverresponse.split()
        port = raw_input("Enter the port the web server is listening on:  ")
        webclient.checkInternalWebServers(servers, port)
    elif choice == "3":
        os.system('cls')
        modify_dvd.ModifyDVD()
    elif choice == "4":
        delete_dvd.DeleteDVD()
    elif choice == "5":
        csvreport_dvd.WriteCSV()
