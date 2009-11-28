#!/usr/bin/env python

import sys
import check_versions, csv_report

HOST = sys.argv[1]
USER = "jars"
PASSWORD = "jars"

def check_arguments():
    if len(sys.argv) < 3:
        print """ Insufficient arguments:  suggested use -
        python version_checker.py <ip address> "<applications to check>"
        
        NOTES:
        1.  Replace <ip address> with the ip address you want to check.
        2.  Replace <applications to check> with any combination of the following
        applications (in quotes):
                java
                python
                perl
                
        EXAMPLE:
        
        python version_checker.py 1.1.1.1 "python java"
        
        This command will check the versions of Python and Java on computer with ip
        address 1.1.1.1."""
        sys.exit(1)
    

def get_versions():
    print "HOST - ", HOST
    if "java" in sys.argv[2]:
        java_version = check_versions.check_java(HOST, USER, PASSWORD)
        csv_report.write_csv_log(HOST, "Java", java_version)
        print "Java version = ", java_version
    if "python" in sys.argv[2]:
        python_version = check_versions.check_python(HOST, USER, PASSWORD)
        csv_report.write_csv_log(HOST, "Python", python_version)
        print "Python version = ", python_version
    if "perl" in sys.argv[2]:
        perl_version = check_versions.check_perl(HOST, USER, PASSWORD)
        csv_report.write_csv_log(HOST, "Perl", perl_version)
        print "Perl version = ", perl_version

check_arguments()
get_versions()


