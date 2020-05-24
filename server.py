"""
author: Noe Vasquez Godinez
date: 24 - 05 - 2020
email: noe-x@outlook.com
web: noevg.github.io

about:
    This software create a TCP server to working communication
    between various clients, use threading to handle varios clients.

    -This software is necesary install from pip:
     -> pip install pyfiglet

    -This software it's programed with python 3.X

"""
""" System modules """
import os
import sys

""" Print the ascii art """
import pyfiglet

""" Socket TCP/IP modules """
from socket import AF_INET, socket, SOCK_STREAM

""" threading modules """
from threading import Thread

""" Setup server values """
HOST = ''           # IP Server
PORT = 60001        # Port Server
BUFFER_SIZE = 1024  # Size buffer comunnicantion
ADDR = (HOST, PORT) # Tuple with values
SERVER = socket(AF_INET, SOCK_STREAM) # Socket to server
SERVER.bind(ADDR)   # Set ip and port
SIZE_CLIENTS = 10   # Define size clientes to listen

"""Dictionary to allowed the all clients (socket) """
clients = {}

def shownInfo():
    """This function shown information about software and author"""
    os.system('cls' if os.name == 'nt' else 'clear')
    ascii_banner = pyfiglet.figlet_format("Server TCP/IP")
    print(ascii_banner)
    print("----------------------------------")
    print("_--|Author: Noé Vásquez Godínez")
    print("_--|Web: noevg.github.io")
    print("_--|The OS: ",os.name)
    if os.name == 'nt':
        print("_--|Buuuuu! you like Windows MS :( ")
    else:
        print("_--|Great! you like UNIX systems, \n\t I hope it's GNU/Linux... :) ")
    print("----------------------------------")

def broadcast(message,ipClient=''):
    """This function send message to all clients"""
    for sock in clients:
        sock.send( bytes(ipClient+" -> ", "utf8")+message)


def handleClient(client):
    """This function attend each client"""
    while True:
        message = client.recv(BUFFER_SIZE)
        if not message:
            client.close()
            break
        else:
            broadcast(message,clients[client][0])
    print("exit client!")
    return


def server(clients):
    """Connections clients"""
    print("Server run ...")
    try:
        while True:
            client, client_address = SERVER.accept()
            print("Client: %s:%s has connected." % client_address)
            client.send(bytes("OK\n", "utf8"))
            clients[client] = client_address
            Thread(target=handleClient, args=(client,)).start()
    except KeyboardInterrupt:
        sys.exit()
    return
def runServer():
    """Start the server"""
    shownInfo()
    SERVER.listen(SIZE_CLIENTS)
    server(clients)
    SERVER.close()

def main():
    runServer()
if __name__ == "__main__":
    main()
