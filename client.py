import socket
import threading
import time

HOST = '192.168.56.1'  # Getting the IP of the server
PORT = 5050  # Port to listen on (non-privileged ports are > 1023)
FORMAT = 'utf-8'  # Define the encoding format of messages from client-HOST
ADDR = (HOST, PORT)  # Creating a tuple of IP+PORTf for connection

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Creating a socket object
client_socket.connect(ADDR)  # Connecting to the server

def send(msg):  # Function for sending messages to the server
    message = msg.encode(FORMAT)  # Encoding the message to bytes format
    msg_length = len(message)  # Getting the length of the message
    send_length = str(msg_length).encode(FORMAT)  # Encoding the length of the message to bytes format
    send_length += b' ' * (64 - len(send_length))  # Adding spaces to the length of the message to make it 64 bytes long
    client_socket.send(send_length)  # Sending the length of the message to the server
    client_socket.send(message)  # Sending the message to the server
    print(client_socket.recv(2048).decode(FORMAT))  # Receiving the message from the server

send("Hello World!")  # Sending the message to the server
send("DISCONNECT")