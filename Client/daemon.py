import socket
import urllib2

host = '139.59.82.146'
port = 10022
buf = 1024

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect((host, port))
clientsocket.send("a")

#to send data
# print "Sending 'test1\\n'"
# clientsocket.send('test1\n')
# print "success"

# result = ""
# while 1:
# 	data = clientsocket.recv(1024)
# 	if not data:
# 		break;
# 	result = result + data

# print result


while 1:
	data = clientsocket.recv(1024)
	if data == "a":
		request = urllib2.urlopen("http://localhost/")
		content = request.read()
		print content
		result = "HTTP/1.0 " + str(request.code) + " OK"
		result = result + str(request.info())
		# print request.info()
		# for item in request.info():
		#     result = result + "\n" + item 
		result = result + "\n" + content
		print result
		clientsocket.send(result)