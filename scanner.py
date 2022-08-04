#!/bin/python3

import sys
import socket
from datetime import datetime

#Define our target
if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1]) #translate hostname to ipv4
else:
	print("Invalid amount of arguments.")
	print("Synatax: python3 scanner.py <ip>")

#Adding a pretty banner
print("-" * 50)
print("Scanning target"+target)
print("Time started: "+str(datetime.now()))
print("-" * 50)

try:
	for port in range(50,85): #1 to 65535 for all ports
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect_ex((target,port)) #return an error indicator 0 open, 1 close
		if result == 0:
			print("Port {} is open".format(port))
		s.close()
			
except KeyboardInterrupt:
	print("\nExiting Program")
	sys.exit()
	
except socket.gaierror:
	print("Hostname could not be resolved")
	sys.exit()

except socket.error:
	print("Couldn't connect to the server")
	sys.exit()
