#=======================================#
#SNAPSHOT.PY                            #
#DIRECTORY/FILE SYSTEM SNAPSHOT PROGRAM #
#BY JAMES O. KNOWLTON, COPYRIGHT 2007   #
#=======================================#


import sys, snapshothelper, os


#MENU
def menu():
    os.system('cls')
    print '''
    DIRECTORY/FILE COMPARISON TOOL
    ====================================
    Please type a number and press enter:
    
    1.  Create a snapshot
    2.  List snapshot files
    3.  Compare snapshots
    4.  Help
    5.  Exit
    '''
    choice = raw_input("\t")
    return choice

#MENU DECISION STRUCTURE
choice = ""
while choice != "5":
    choice = menu()
    if choice == "1":
        os.system('cls')
        print '''CREATE SNAPSHOT
        ===================================='''
        directory = raw_input \
                    ("Enter the directory name to create a snapshot of:  ")
        filename = raw_input \
                   ("Enter the name of the snapshot file to create:  ")
        snapshothelper.createSnapshot(directory, filename)    
    elif choice == "2":
        os.system('cls')
        print '''
        LIST SNAPSHOT FILES
        ====================================
        Enter the file extension for your snapshot files
        (for example, 'snp' if your files end in '.snp'):
        '''
        extension = raw_input("\t\t")
        snapshothelper.listSnapshots(extension)
    elif choice == "3":
        os.system('cls')
        print '''
        COMPARE SNAPSHOTS
        ====================================
        '''
        snap1 = raw_input("Enter the filename of snapshot 1:  ")
        snap2 = raw_input("Enter the filename of snapshot 2:  ")
        snapshothelper.compareSnapshots(snap1, snap2)
    elif choice == "4":
        snapshothelper.showHelp()
    else:
        if choice != "5":
            snapshothelper.invalidChoice()
        
        








    
