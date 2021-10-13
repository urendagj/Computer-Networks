from segment import Segment


# #################################################################################################################### #
# RDTLayer                                                                                                             #
#                                                                                                                      #
# Description:                                                                                                         #
# The reliable data transfer (RDT) layer is used as a communication layer to resolve issues over an unreliable         #
# channel.                                                                                                             #
#                                                                                                                      #
#                                                                                                                      #
# Notes:                                                                                                               #
# This file is meant to be changed.                                                                                    #
#                                                                                                                      #
#                                                                                                                      #
# #################################################################################################################### #


class RDTLayer(object):
    # ################################################################################################################ #
    # Class Scope Variables                                                                                            #
    #                                                                                                                  #
    #                                                                                                                  #
    #                                                                                                                  #
    #                                                                                                                  #
    #                                                                                                                  #
    # ################################################################################################################ #
    DATA_LENGTH = 4 # in characters                     # The length of the string data that will be sent per packet...
    FLOW_CONTROL_WIN_SIZE = 15 # in characters          # Receive window size for flow-control
    sendChannel = None
    receiveChannel = None
    dataToSend = ''
    currentIteration = 0                                # Use this for segment 'timeouts'
    seqnum = 0
    strindx = 0
    client_received  = ''
    server_received = ''
    acknum = 0
    countSegmentTimeouts = 0
    tempsegments = []
    tempReceivedSegments = []
    # Add items as needed

    # ################################################################################################################ #
    # __init__()                                                                                                       #
    #                                                                                                                  #
    #                                                                                                                  #
    #                                                                                                                  #
    #                                                                                                                  #
    #                                                                                                                  #
    # ################################################################################################################ #
    def __init__(self):
        self.sendChannel = None
        self.receiveChannel = None
        self.dataToSend = ''
        self.currentIteration = 0
        # Add items as needed

    # ################################################################################################################ #
    # setSendChannel()                                                                                                 #
    #                                                                                                                  #
    # Description:                                                                                                     #
    # Called by main to set the unreliable sending lower-layer channel                                                 #
    #                                                                                                                  #
    #                                                                                                                  #
    # ################################################################################################################ #
    def setSendChannel(self, channel):
        self.sendChannel = channel

    # ################################################################################################################ #
    # setReceiveChannel()                                                                                              #
    #                                                                                                                  #
    # Description:                                                                                                     #
    # Called by main to set the unreliable receiving lower-layer channel                                               #
    #                                                                                                                  #
    #                                                                                                                  #
    # ################################################################################################################ #
    def setReceiveChannel(self, channel):
        self.receiveChannel = channel

    # ################################################################################################################ #
    # setDataToSend()                                                                                                  #
    #                                                                                                                  #
    # Description:                                                                                                     #
    # Called by main to set the string data to send                                                                    #
    #                                                                                                                  #
    #                                                                                                                  #
    # ################################################################################################################ #
    def setDataToSend(self,data):
        self.dataToSend = data


    # ################################################################################################################ #
    # getDataReceived()                                                                                                #
    #                                                                                                                  #
    # Description:                                                                                                     #
    # Called by main to get the currently received and buffered string data, in order                                  #
    #                                                                                                                  #
    #                                                                                                                  #
    # ################################################################################################################ #
    def getDataReceived(self):
        # ############################################################################################################ #
        # Identify the data that has been received...

        # ############################################################################################################ #
        return self.server_received #self.contents["server_recieved"]

    # ################################################################################################################ #
    # processData()                                                                                                    #
    #                                                                                                                  #
    # Description:                                                                                                     #
    # "timeslice". Called by main once per iteration                                                                   #
    #                                                                                                                  #
    #                                                                                                                  #
    # ################################################################################################################ #
    def processData(self):
        self.currentIteration += 1
        self.processSend()
        self.processReceiveAndSendRespond()

    # ################################################################################################################ #
    # processSend()                                                                                                    #
    #                                                                                                                  #
    # Description:                                                                                                     #
    # Manages Segment sending tasks                                                                                    #
    #                                                                                                                  #
    #                                                                                                                  #
    # ################################################################################################################ #
    def processSend(self):
        sent = 0

        sequence_number = self.acknum
        # ############################################################################################################ #
        print('processSend(): Complete this...')
        while True:
            segmentSend = Segment()
            #Split up the string into 4 char chunks, and store each itteration into the payload
            segmentSend.payload = self.dataToSend[sequence_number: sequence_number + self.DATA_LENGTH]

            if not segmentSend.payload:
                break
            #Add our parsed data segments into what we have currently recieved
            self.client_received = self.client_received + segmentSend.payload
            #Update our segments
            self.seqnum += 4
            #Display sending segment
            segmentSend.setData(sequence_number,segmentSend.payload)
            print("Sending segment: ", segmentSend.to_string())
            #Use the unreliable sendChannel to send the segment
            self.sendChannel.send(segmentSend)
            ################################
            sent = sent + 4
            sequence_number += 4
            if sent + 4 > self.FLOW_CONTROL_WIN_SIZE:
                break
            



            
        # You should pipeline segments to fit the flow-control window
        # The flow-control window is the constant RDTLayer.FLOW_CONTROL_WIN_SIZE
        # The maximum data that you can send in a segment is RDTLayer.DATA_LENGTH
        # These constants are given in # characters

        # Somewhere in here you will be creating data segments to send.
        # The data is just part of the entire string that you are trying to send.
        # The seqnum is the sequence number for the segment (in character number, not bytes)



        # ############################################################################################################ #


      

    # ################################################################################################################ #
    # processReceive()                                                                                                 #
    #                                                                                                                  #
    # Description:                                                                                                     #
    # Manages Segment receive tasks                                                                                    #
    #                                                                                                                  #
    #                                                                                                                  #
    # ################################################################################################################ #
    def processReceiveAndSendRespond(self):
        segmentAck = Segment()                  # Segment acknowledging packet(s) received

    
        listIncomingSegments = self.receiveChannel.receive()
        #Check to see if we have data inside of our array
        if listIncomingSegments:
            #To sort I referenced this: https://stackoverflow.com/questions/403421/how-to-sort-a-list-of-objects-based-on-an-attribute-of-the-objects
            listIncomingSegments.sort(key=lambda self: self.seqnum, reverse= False)
            for i in range(len(listIncomingSegments)):
                segmentAck.payload = listIncomingSegments[i].payload
                #Check to see if we have timeouts
                if listIncomingSegments[i].acknum != listIncomingSegments[i].seqnum:
                    self.countSegmentTimeouts += 1
                #Ack message
                if listIncomingSegments[i].seqnum == -1:
                    #check to see if segment is new, if it is then add it
                    if listIncomingSegments[i].acknum > self.acknum:
                        self.acknum = listIncomingSegments[i].acknum
                #Ack segment
                else:
                    #Check to see if our current segment is as intended
                    if listIncomingSegments[i].seqnum == self.acknum:
                        #Check bit errors and make sure segments are valid
                        if listIncomingSegments[i].checkChecksum():
                            self.acknum += 4
                            #Get the data given from client to give as server output
                            self.server_received = self.server_received + listIncomingSegments[i].payload
                    #reset the Ack val    
                    else:
                        segmentAck.setAck(self.acknum)

                       # Display response segment
                    segmentAck.setAck(self.acknum)
           
                    print("Sending ack: ", segmentAck.to_string())

                    # Use the unreliable sendChannel to send the ack packet
                    self.sendChannel.send(segmentAck)    

            




        # ############################################################################################################ #
        # What segments have been received?
        # How will you get them back in order?
        # This is where a majority of your logic will be implemented
     
        
       




        # ############################################################################################################ #
        # How do you respond to what you have received?
        # How can you tell data segments apart from ack segemnts?
        #print('processReceive(): Complete this...')

        # Somewhere in here you will be setting the contents of the ack segments to send.
        # The goal is to employ cumulative ack, just like TCP does...
        


        # ############################################################################################################ #
     
