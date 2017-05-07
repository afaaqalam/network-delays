#!/usr/bin/python
import socket
import time
import os
import argparse
import multiprocessing

def perform():
    while True:
    #	print('Waiting for a connection')
    	connection, address = sock.accept()
    	try:
    		print('Child %s got a connection from %s' %(os.getpid(), address))
    		#time.sleep(5)
    		while True:
    			data = connection.recv(args.recv)
    			#print('Received: %s' %data)
    			if data:
    #				print('sending data back')
    				time.sleep(args.sleep)
    				#compute(args.num)
    				connection.sendall(data)
    			else:
    #				print('no more data from client')
    				break
    	finally:
            print('Child %s is done' %(os.getpid()))
            connection.close()

parser = argparse.ArgumentParser()
parser.add_argument('--ip', '-i', help='specify server ip address', required=True, action='store')
parser.add_argument('--port', '-p', help='specify server port number', required=True, type=int, action='store')
parser.add_argument('--sleep', '-s', help='specify sleep time in seconds', type=int, default=0, action='store')
parser.add_argument('--recv', '-r', help='specify bytes to receive from the socket', type=int, default=4096, action='store')
args = parser.parse_args()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (args.ip, args.port)
print('Listening on %s port %s' %server_address)
sock.bind(server_address)
sock.listen(5)

p1 = multiprocessing.Process(target=perform)
p1.start()
p2 = multiprocessing.Process(target=perform)
p2.start()
