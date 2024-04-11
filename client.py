import socket
import select
import sys

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
if len(sys.argv) != 3:
    print ("Correct usage: script, IP address, port number")
    exit()
IP_address = str(sys.argv[1])
Port = int(sys.argv[2])
server.connect((IP_address, Port))
"""
welcome = "Connection complete"
test=message.encode() JUST DONT WORK
message = welcome
server.send(message)
"""
while True:
    sockets_list = [sys.stdin, server]
    #read_sockets,write_socket, error_socket = select.select(sockets_list, [], [])
    read_sockets,write_socket, error_socket = sockets_list, [], []
    for socks in read_sockets:
        if socks == server:

            message = socks.recv(2048)
            message.decode()
            print (message)
        else:
            message = sys.stdin.readline()

            sys.stdout.write("<You>")
            sys.stdout.write(message)
            
            message = message.encode()
            server.send(message)
            
            #sys.stdout.flush()
server.close()
