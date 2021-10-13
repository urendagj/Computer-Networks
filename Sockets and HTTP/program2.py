import socket
import sys

#Article refernced: https://zetcode.com/python/socket/#:~:text=The%20recv()%20method%20receives,returns%20an%20empty%20byte%20string.
#create a socket instance. AF_INET referes to ipv4, and SOCK_STREAM refers to the TCP protocol.
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    #Connecting to a server:
    s.connect(("gaia.cs.umass.edu", 80))
    #send a request
    #code referenced: https://www.geeks3d.com/hacklab/20190110/python-3-simple-http-request-with-the-socket-module/
    request = "GET /wireshark-labs/HTTP-wireshark-file3.html HTTP/1.1\r\nHost:gaia.cs.umass.edu\r\n\r\n"
    s.sendall(request.encode())

    #recieve infromation
    contents = ""
    length = 0
    while True:
        response = s.recv(4096)
        #if there is no longer information in response, then we break out 
        #if not response:
            #break
        contents = contents + response.decode('UTF-8')
        length = length + len(response)
        if not response:
             print("GET /wireshark-labs/HTTP-wireshark-file3.html HTTP/1.1\r\nHost:gaia.cs.umass.edu\r\n\r\n")
             print("[RECV] - length:", length)
             print(contents)
             break
          
    s.close