#!/usr/bin/python
# -*- coding: utf-8 -*-
 
# The modules required
import sys
import socket

'''
This is a template that can be used in order to get started. 
It takes 3 commandline arguments and calls function send_and_receive_tcp.
in haapa7 you can execute this file with the command: 
python3 CourseWorkTemplate.py <ip> <port> <message> 

Functions send_and_receive_tcp contains some comments.
If you implement what the comments ask for you should be able to create 
a functioning TCP part of the course work with little hassle. 
''' 

host = "195.148.20.105"
port = 10000

def send_and_receive_tcp(address, port, message):
    print("You gave arguments: {} {} {}".format(address, port, message))
    # create TCP socket
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # connect socket to given address and port
    tcp_socket.connect((address, port))
    # python3 sendall() requires bytes like object. encode the message with str.encode() command
    encoded = message.encode()
    # send given message to socket
    tcp_socket.sendall(encoded)
    # receive data from socket
    data = tcp_socket.recv(1024)
    # data you received is in bytes format. turn it to string with .decode() command
    datastring = data.decode()
    # print received data
    print(datastring)
    # close the socket
    tcp_socket.close()
    # Get your CID and UDP port from the message
    CID, UDP = datastring.split(',')
    # Continue to UDP messaging. You might want to give the function some other parameters like the above mentioned cid and port.
    send_and_receive_udp(address, UDP, CID)
    return
 
 
def send_and_receive_udp(address, port, CID):
    try:
        udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        firstmessage = "HELLO from " + CID
        udp_socket.sendto(firstmessage.encode(), (address, port))
        while(True):
            response, serverAddress = udp_socket.recvfrom(1024)
            decodedResponse = response.decode()
            if (decodedResponse.contains('bye')):
                break
            reversed = reverse_words(decodedResponse)
            udp_socket.sendto(reversed.encode(), (address, port))
        udp_socket.close()
    except Exception as e:
        print("Error occurred in UDP communication:", e)
    print("This is the UDP part. Implement it yourself.")
    return

def reverse_words(string):
    words = string.split()
    reversed_words = words[::-1]
    return " ".join(reversed_words) 
 
def main():
    USAGE = 'usage: %s <server address> <server port> <message>' % sys.argv[0]
 
    try:
        # Get the server address, port and message from command line arguments
        server_address = str(sys.argv[1])
        server_tcpport = int(sys.argv[2])
        message = str(sys.argv[3])
    except IndexError:
        print("Index Error")
    except ValueError:
        print("Value Error")
    # Print usage instructions and exit if we didn't get proper arguments
        sys.exit(USAGE)
 
    send_and_receive_tcp(server_address, server_tcpport, message)
 
 
if __name__ == '__main__':
    # Call the main function when this script is executed
    main()
