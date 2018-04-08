import httplib
import socket
import re
import urllib2
from thread import *
import sys
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"



lista = []
lista.append("10022@damn")

socks = []
domains = []
conns = []
for item in lista:
    host = ''
    port = int(item.split("@")[0])
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((host,port))
    sock.listen(1)
    conn, addr = sock.accept()
    socks.append(sock)
    conns.append(conn)
    domains.append(item.split("@")[1])

@app.route('/damn')
def server():
    #output the request @ 1234
    #receive the output @ 1234
    text = "damn"
    for i in range(len(domains)):
        if text == domains[i]:
            conns[i].send("a")
            return conn.recv(4096)

    return 'did not work'



if __name__ == '__main__':
    app.run( host='0.0.0.0')
