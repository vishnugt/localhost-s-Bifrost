import httplib
import socket
import re
import urllib2

# Standard socket stuff:
host = '' # do we need socket.gethostname() ?
port = 9002
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host, port))
sock.listen(1) # don't queue up any requests


# Loop forever, listening for requests:
while True:
    try:
        csock, caddr = sock.accept()
        print "Connection from: " + `caddr`
        req = csock.recv(1024) # get the request, 1kB max
        print req
        request = urllib2.urlopen("http://files.melii.club")
        content = request.read()
        print content
        result = "HTTP/1.0 " + str(request.code) + " OK"
        result = result + str(request.info())
        # print request.info()
        # for item in request.info():
        #     result = result + "\n" + item 
        result = result + "\n" + content
        print result
        csock.sendall(result)

    # Look in the first line of the request for a move command
    # A move command should be e.g. 'http://server/move?a=90'
#     csock.sendall("""HTTP/1.0 200 OK
# Content-Type: text/html

# <html>
# <head>
# <title>Success</title>
# </head>
# <body>
# Boo!
# </body>
# </html>
# """)
    finally:
        csock.close()

        
        
