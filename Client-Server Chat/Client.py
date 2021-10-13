#Client Side
import sys
import socket
import select

#References:
#https://www.bogotobogo.com/python/python_network_programming_tcp_server_client_chat_server_chat_client_select.php
#https://pythonprogramming.net/server-chatroom-sockets-tutorial-python-3/
#https://www.bogotobogo.com/python/python_network_programming_tcp_server_client_chat_server_chat_client_select.php

#Create a variable to store localhost
Host = '127.0.0.1'
#Create a vairable to store a port mumber greater than 1023
Port = 5434

#Create an instance of a socket server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    #Connect to remote host
    try :
        s.connect((Host, Port))
    except :
        print('Unable to connect')
        sys.exit()

    #Display the command to terminate the chatroom
    print("Type /q to quit")

    #Promt the client to send a message to the serve
    print("Enter a message to send...")

  
    while True:

        msgsend = input('>')

        #Send a message to the server
        s.send(msgsend.encode())
        
        #Get the response from the server
        msgrecv = s.recv(1024).decode()

        #If we send or recieve the exit token then we end the connection
        if msgrecv.lower() == "/q" or msgsend.lower() == "/q":
             break
            
        #Display the data recieved from the serverh
        print(msgrecv)


    #End the connection
    s.close()
    