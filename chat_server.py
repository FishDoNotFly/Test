import socket
import select
from threading import *
import sys
#this is crack

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
"""
the first argument AF_INET is the address domain of the socket used when we have an Internet Domain with two hosts
the second argument is the type of socket. SOCK_STREAM data or characters are read in a continuous flow
"""
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
if len(sys.argv) != 3:
    print("Correct usage: script, IP address, port number")

    
    exit()
    
IP_address = str(sys.argv[1])
Port = int(sys.argv[2])

server.bind((IP_address, Port)) 
#binds the server to an entered IP address and at the specified port number client MUST be aware of these parameters :(
server.listen(100)
#listens for 100 active connections can be increased, i think only works for 1 right now
list_of_clients=[]

def clientthread(conn, addr):
    entry = "Welcome to this chatroom!".encode
    conn.send(entry)
    #sends a message to the client whose user object is conn
    while True:
            try:     
                message = conn.recv(2048)
                message.decode()
                if message:
                    print("<" + addr[0] + "> " + message)
                    message_to_send = "<" + addr[0] + "> " + message
                    broadcast(message_to_send,conn)
                    #prints the message and address of the user who just sent the message on the server terminal, command prompt
                else:
                    
                    remove(conn)
                    
            except:
                continue

def broadcast(message,connection):
    for clients in list_of_clients:
        if clients!=connection:
            try:
                clients.send(message)
            except:
                
                clients.close()
                remove(clients)
                

def remove(connection):
    if connection in list_of_clients:
        list_of_clients.remove(connection)


while True:
    conn, addr = server.accept()
    """
    accepts a connection request and stores two parameters    conn which is a socket object for that user client thing   addr which contains the IP address of the client that just connected
    """
    list_of_clients.append(conn)
    print(addr[0] + " connected")
    #maintains a list of clients SO broadcasting a message = EASY to all available people in the server room thing
    #prints the address of the person who just connected
    """
    start_new_thread(clientthread,(conn,addr))
    """
    clientthread(conn, addr)
    #creates and individual thread for every user that connects and DOESNT WORK???

conn.close()
server.close()

