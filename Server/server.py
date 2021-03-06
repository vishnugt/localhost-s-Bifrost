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
    return "Welcome to ngStone!"



lista = []
socks = []
domains = []
conns = []

def update():
    for item in lista:
        host = ''
        port = int(item.split("@")[0])
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print "Waiting on " + item.split("@")[0] + "for the domain " + item.split("@")[1]
        sock.bind((host,port))
        sock.listen(1)
        conn, addr = sock.accept()
        socks.append(sock)
        conns.append(conn)
        domains.append(item.split("@")[1])

def get_free_tcp_port():
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp.bind(('', 0))
    addr, port = tcp.getsockname()
    tcp.close()
    return port


@app.route('/<string:text>')
def server(text):
    #output the request @ 1234
    #receive the output @ 1234
    for i in range(len(domains)):
        if text == domains[i]:
            conns[i].send("a")
            return conns[i].recv(4096)

    if "addThis" in text:
        newDomain = text.split("@")[1]
        newPort = str(get_free_tcp_port())
        lista.append(newPort + "@"+ newDomain)
        return newPort

    if "refresh" in text:
        update()
        return "everyone connected"

    return 'invalid server'



if __name__ == '__main__':
    app.run( host='0.0.0.0')
