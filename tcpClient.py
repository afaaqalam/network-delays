#!/usr/bin/python
import socket
import time
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--ip', help='specify server ip address', required=True, action='store')
parser.add_argument('-p', '--port', help='specify the port number', required=True, type=int, action='store')
parser.add_argument('-s', '--size', help='specify the size of the packet in bytes', type=int, action='store')
parser.add_argument('-r', '--recv', help='specify the number of bytes to receive from socket', type=int, default=4096, action='store')
parser.add_argument('-c', '--count', help='specify the count of packets to send', type=int, default=1, action='store')
args = parser.parse_args()


def Tick():
	return time.time()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (args.ip, args.port)
#print('connecting to %s port %s' %server_address)
sock.connect(server_address)

message = 'A' * int(args.size)
a = []
#print('sending "%s"'%message)

try:
	for i in range(args.count):
		start_time = Tick()
		sock.sendall(message)
#		print('sent')
		amount_received = 0
		amount_expected = len(message)
		while amount_received < amount_expected:
			data = sock.recv(4096)
			end_time = Tick()
			amount_received += len(data)
#			print('received "%s"'% data)
			b = (end_time - start_time)*1000
			a.append(b)

finally:
	print('---socket closed---')
	sock.close()
	print(sum(a)/len(a))
