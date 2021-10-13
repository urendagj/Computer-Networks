import socket
import sys

#Code referenced: https://zetcode.com/python/socket/#:~:text=The%20recv()%20method%20receives,returns%20an%20empty%20byte%20string.

#create a server port that is greater than 1023
port = 4500

#create a variable to store the HOST 
Host = '127.0.0.1'
#create an instance of a socket server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    #bind our socket to localhost with our port
    s.bind((Host,port))
    print("Connected by:", Host, port, '\n')

    #given data
    data = "HTTP/1.1 200 OK\r\n"\
    "Content-Type: text/html; charset=UTF-8\r\n\r\n"\
    "<html>Congratulations! You've downloaded the first Wireshark lab file!</html>\r\n"

    #start listening for incoming connections
    s.listen()
    print("The server on port", port,"is listening.")

    while True:
        #accept incoming connection
        connnection, address = s.accept()
        #recieve content
        contents = connnection.recv(1024)
        # print as single string
        print("Recieved:", str(contents), '\n')
        send_msg = data
        connnection.send(send_msg.encode())
        # formatting to follow sample output
        print("Sending>>>>>>>>>>>>\n",data,"\n","<<<<<<<<<<<\n")
        s.close()
        # as shown in sample output return after first request
        break