#!/usr/bin/env python

import sys
import telnetlib

def check_java(host, user, password):
    java_version = ""
    tn = telnetlib.Telnet(host)
    tn.read_until("login: ")
    tn.write(user + "\n")
    
    if password:
        tn.read_until("Password: ")
        tn.write(password + "\n")
    
    tn.write("java -version\n")
    tn.write("exit\n")
    result = tn.read_all()
    result_list = result.split("\n")
    
    for line in result_list:
        if line.startswith("java version"):
            java_version = line[14:21].strip("\"")            
    
    return java_version


def check_python(host, user, password):
    python_version = ""
    tn = telnetlib.Telnet(host)

    tn.read_until("login: ")
    tn.write(user + "\n")
    if password:
        tn.read_until("Password: ")
        tn.write(password + "\n")
    
    tn.write("python -V\n")
    tn.write("exit\n")
    result = tn.read_all()
    result_list = result.split("\n")
    
    for line in result_list:
        if line.startswith("Python "):
            python_version = line[7:]
    
    return python_version
            


def check_perl(host, user, password):
    perl_version = ""
    tn = telnetlib.Telnet(host)
    tn.read_until("login: ")
    tn.write(user + "\n")
    if password:
        tn.read_until("Password: ")
        tn.write(password + "\n")
    
    tn.write("perl -version\n")
    tn.write("exit\n")
    
    result = tn.read_all()
    result_list = result.split("\n")
    for line in result_list:
        if line.startswith("This is perl"):
            perl_version = line[15:20] 
    return perl_version

