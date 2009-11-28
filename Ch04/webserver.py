import SimpleHTTPServer, SocketServer, sys

#SET THE PORT VARIABLE TO COMMAND-LINE ARGUMENT
PORT = sys.argv[1]

def RunServer():
    try:
        httphandler = SimpleHTTPServer.SimpleHTTPRequestHandler
    
        httpd = SocketServer.TCPServer(("", int(PORT)), httphandler)
    
        print "Python Web Server, serving at port" + PORT
        httpd.serve_forever()
    
    except (KeyboardInterrupt, SystemExit):
        print "Exiting..."
        sys.exit
    except:
        print "There was a problem starting the webserver at port " + PORT
        
RunServer()

