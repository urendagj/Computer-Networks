#Server Side
import sys
import socket
import select

#References:
#https://www.bogotobogo.com/python/python_network_programming_tcp_server_client_chat_server_chat_client_select.php
#https://pythonprogramming.net/server-chatroom-sockets-tutorial-python-3/
#https://www.bogotobogo.com/python/python_network_programming_tcp_server_client_chat_server_chat_client_select.php

#Create the local host vairable
Host = '127.0.0.1'

#Initialize the port
Port = 5434

#Make a variable for the print statements
count = 0

#create an instance of a socket server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    #bind our socket to localhost with our port
    s.bind((Host,Port))

    #Print first print statement as shown in the assignment
    print("Server listening on: localhost on port:",Port)

    #start listening for incoming connections
    s.listen(2)

    #accept incoming connection
    connnection, address = s.accept()

    #Print the connection
    print("Connected by ",address)

    #Print the current status
    print("Waiting for message...")

  

    while True:

        #Continuously get data, packet data sizes of 1024 will not be accepted
        msgrecv = connnection.recv(1024).decode()

        #If we recieved the exit token then we end the connection
        if msgrecv.lower() == "/q":
            break

        #If data was not recieved, then we break out
        if len(msgrecv) <= 0:
            break

        #Print out data from user
        print(msgrecv)
        
        #Display the prompts only once
        if count != 1:
            #Display the command to terminate the chatroom
            print("Type /q to quit")
            print("Enter a message to send...")
            count += 1

        msgsend = input('>')
        
        #Send data to the client
        connnection.send(msgsend.encode())

    #Close the connection
    connnection.close()
        