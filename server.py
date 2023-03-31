import socket
import threading
import time 

HOST = '192.168.56.1'   # Getting the IP of the server
PORT = 5050  # Port to listen on (non-privileged ports are > 1023)
FORMAT = 'utf-8'  # Define the encoding format of messages from client-HOST
ADDR = (HOST, PORT)  # Creating a tuple of IP+PORTf for connection

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Creating a socket object
server_socket.bind(ADDR)  # Binding the socket to the IP+PORT

def handle_client(conn, addr): # Handling the client connection
    print(f"[NEW CONNECTION] {addr} connected.")
    
    connected = True
    while connected:
        msg_length = conn.recv(64).decode(FORMAT)  # Receiving the length of the message
        if msg_length:  # If the length of the message is not empty
            msg_length = int(msg_length)  # Converting the length of the message to an integer
            msg = conn.recv(msg_length).decode(FORMAT)  # Receiving the message
        
            if msg == "DISCONNECT":  # If the message is DISCONNECT
                connected = False  # The client is disconnected
                print(f"[{addr}] Disconnected.")  # Printing the message
            else:
                print(f"[{addr}] {msg}")  # Printing the message 
                conn.send("Msg received".encode(FORMAT))  # Sending a message to the client

           
    conn.close()  # Closing the connection

def start():
    server_socket.listen()  # Listening for connections
    print(f"[LISTENING] Server is listening on {HOST}") # 
    while True:
        conn, addr = server_socket.accept()  # Accepting the connection
        thread = threading.Thread(target=handle_client, args=(conn, addr))  # Creating a thread for each client
        thread.start()  # Starting the thread
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")  # Printing the number of active connections
    

print("[STARTING] server is starting...")
start()

