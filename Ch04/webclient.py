from urllib2 import urlopen
import socket, sys, time, datetime

socket.setdefaulttimeout(15)

def CheckExternalSites(sites):
    logfile = open ("logfile.txt", "a")
    logtime = time.strftime("\n%a, %d %b %Y %H:%M:%S")
    print logtime
    logfile.write(logtime + "\n")
    
    for site in sites:
        try:
            start = time.time()
            data = urlopen("http://" + site)
            stuff = data.read()
            end = time.time()
            difference = end - start
            output = "Site %s took %2.2f seconds to load" %( site, difference )
            logfile.write(output + "\n")
            print output
        except:
            errno, errstr = sys.exc_info()[:2]
            if errno == socket.timeout:
                timeouterror = "there was a timeout"
                logfile.write(timeouterror + "\n\n")
                print timeouterror + "\n"
                raw_input("Press Enter to Continue:  ")
                return
            else:
                genericerror = "Error connecting to site %s" % (site)
                logfile.write(genericerror + "\n\n")
                print genericerror + "\n"
                raw_input("Press Enter to Continue:  ")
                return
    print "\n"
    logfile.write("\n")
    logfile.close()
    raw_input("Press Enter to Continue:  ")
                
def CheckInternalWebServers(serverlist, port):
    logfile = open ("logfile.txt", "a")
    logtime = time.strftime("\n%a, %d %b %Y %H:%M:%S")
    print logtime
    logfile.write(logtime + "\n")
    
    textfile = "textfile.txt"
    binaryfile = "binaryfile.exe"
    for server in serverlist:
        try:
            start = time.time()
            serveroutput =  server + ":"
            logfile.write(serveroutput + "\n")
            print serveroutput
            for file in textfile, binaryfile:
                data = urlopen("http://%s:%s/%s") % (server, port, file)
                stuff = data.read()
                end = time.time()
                difference = end - start
                print file, " took %2.2f seconds to load" %( difference )
                logfile.write("%s took %2.2f seconds to load" %( file, difference ) + "\n")
        except:
            errno, errstr = sys.exc_info()[:2]
            if errno == socket.timeout:
                timeouterror = "there was a timeout"
                logfile.write(timeouterror + "\n\n")
                print timeouterror
                logfile.close()
                raw_input("Press Enter to continue:  ")
                return
            else:
                genericerror = "Error connecting to server " + server
                logfile.write(genericerror + "\n\n")
                print genericerror
                raw_input("Press Enter to Continue:  ")
                return
    print "\n"
    logfile.write("\n")
    logfile.close()
    raw_input("Press Enter to Continue:  ")

