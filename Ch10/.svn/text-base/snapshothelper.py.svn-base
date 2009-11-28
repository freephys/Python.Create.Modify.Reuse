import os, pickle, difflib, sys, pprint

def createSnapshot(directory, filename):    
    cumulative_directories = []
    cumulative_files = []

    for root, dirs, files in os.walk(directory):
        cumulative_directories = cumulative_directories + dirs
        cumulative_files = cumulative_files + files
        
    try:
        output = open(filename, 'wb')
        pickle.dump(cumulative_directories, output, -1)
        pickle.dump(cumulative_files, output, -1)
        output.close()
    except:
        print "Problems encounted trying to save snapshot file!"
    
    raw_input("Press [Enter] to continue...")
    return

def listSnapshots(extension):
    snaplist = []
    filelist = os.listdir(os.curdir)
    for item in filelist:
        if item.find(extension)!= -1:
            snaplist.append(item)

    print '''
    Snapshot list:
    ========================
    '''
    printlist(snaplist)
    
    raw_input("Press [Enter] to continue...")
    
            

def compareSnapshots(snapfile1, snapfile2):

    try:
        pkl_file = open(snapfile1, 'rb')
        dirs1 = pickle.load(pkl_file)
        files1 = pickle.load(pkl_file)
        pkl_file.close()

        pk2_file = open(snapfile2, 'rb')
        dirs2 = pickle.load(pk2_file)
        files2 = pickle.load(pk2_file)
        pk2_file.close()
    except:
        print "Problems encountered accessing snapshot files!"
        raw_input("\n\nPress [Enter] to continue...")
        return

    result_dirs = list(difflib.unified_diff(dirs1, dirs2))
    result_files = list(difflib.unified_diff(files1, files2))

    added_dirs = []
    removed_dirs = []
    added_files = []
    removed_files = []
    
    for result in result_files:
        if result.find("\n") == -1:
            if result[0] == "+":
                resultadd = result.strip('+')
                added_files.append(resultadd)
            elif result[0] == "-":
                resultsubtract = result.strip('-')
                removed_files.append(resultsubtract)

    for result in result_dirs:
        if result.find("\n") == -1:
            if result[0] == "+":
                resultadd = result.strip('+')
                added_dirs.append(resultadd)
            elif result[0] == "-":
                resultsubtract = result.strip('-')
                removed_dirs.append(resultsubtract)
                
    print "\n\nAdded Directories:\n"
    printList(added_dirs)
    print "\n\nAdded Files:\n"
    printList(added_files)
    print "\n\nRemoved Directories:\n"
    printList(removed_dirs)
    print "\n\nRemoved Files:\n"
    printList(removed_files)
    raw_input("\n\nPress [Enter] to continue...")

def showHelp():
    os.system('cls')
    print '''
    DIRECTORY/FILE COMPARISON TOOL
    ====================================
    Welcome to the directory/file snapshot tool.  This tool
    allows you to create snapshots of a directory/file tree,
    list the snapshots you have created in the current directory,
    and compare two snapshots, listing any directories and files
    added or deleted between the first snapshot and the second.
    
    To run the program follow the following procedure:
    1.  Create a snapshot
    2.  List snapshot files
    3.  Compare snapshots
    4.  Help (this screen)
    5.  Exit
    
    '''
    raw_input("Press [Enter] to continue...")

def invalidChoice():
    print "INVALID CHOICE, TRY AGAIN!"
    raw_input("\n\nPress [Enter] to continue...")
    return
    
    
def printList(list):
    fulllist = ""
    indexnum = 1
    
    if len(list) > 20:
        for item in list:
            print "\t\t" + item,
            if (indexnum)%3 == 0:
                print "\n"
            indexnum = indexnum + 1
    else:
        for item in list:
            print "\t" + item
