#!/usr/bin/env python3

import socket

# Creating ssh server from scratch
def main():
 
 # Creating ipv and TCP socket
 server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# At the socket level
 server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
 server_socket.bind(('',2222))
 server_socket.listen(223)