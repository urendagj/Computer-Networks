import socket
import sys

#Article refernced: https://www.geeksforgeeks.org/socket-programming-python/
#create a socket instance. AF_INET referes to ipv4, and SOCK_STREAM refers to the TCP protocol.

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Connecting to a server:
s.connect(("gaia.cs.umass.edu", 80))
#send a request
#code referenced: https://www.geeks3d.com/hacklab/20190110/python-3-simple-http-request-with-the-socket-module/
request = "GET /wireshark-labs/INTRO-wireshark-file1.html HTTP/1.1\r\nHost:gaia.cs.umass.edu\r\n\r\n"
s.send(request.encode())

#recieve infromation
response = s.recv(4096)
print("Request: GET /wireshark-labs/INTRO-wireshark-file1.html HTTP/1.1\r\nHost:gaia.cs.umass.edu\r\n\r\n")
print("[RECV] - length:",len(response))
print(response.decode('utf-8'))
s.close