#!/usr/bin/env python3

import socket

# Creating ssh server from scratch
def main():
 
 # Creating IP and TCP socket
 server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

 # At the socket level
 # Enable socket reuse of local address
 server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
 # listening on all interfaces and use port 2222
 server_socket.bind(('',2222))
 server_socket.listen(223)

 # Establish a connection with anything thats on queue
 client_socket, client_addr = server_socket.accept()
 print(f"Connection from {client_addr[0]}:{client_addr[1]}")
 client_socket.send(b"Hello\n")
 print(client_socket.recv(256).decode())

if __name__ == "__main__":
  main()