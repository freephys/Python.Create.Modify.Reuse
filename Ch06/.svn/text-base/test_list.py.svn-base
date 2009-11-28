#!/usr/bin/env python

import os, glob

def list_tests():
    os.chdir("test_runs")
    filelist = glob.glob("*.xml")
    
    print """
    ================================
    LIST TEST RUNS
    ================================
    """
    for f in filelist:
        item = f.strip('.xml')
        print "\t" + item
    print """
    ================================
    """
    os.chdir("..")
    raw_input("Press [Enter] to continue:  ")
