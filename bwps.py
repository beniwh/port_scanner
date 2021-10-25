#!/usr/bin/python
#BeniW Port Scan

import argparse
import socket
import os
import sys

def Logo():
	print ('''

██████╗ ██╗    ██╗██████╗ ███████╗
██╔══██╗██║    ██║██╔══██╗██╔════╝
██████╔╝██║ █╗ ██║██████╔╝███████╗
██╔══██╗██║███╗██║██╔═══╝ ╚════██║
██████╔╝╚███╔███╔╝██║     ███████║
╚═════╝  ╚══╝╚══╝ ╚═╝     ╚══════╝    

                                ''')

def main():
	Sis()
	Logo()
	Argumentos()
	Conectar()

def Sis():
	if sys.platform != "linux":
		os.system("cls")
	else:
		os.system("clear")

def Argumentos():
	global args
	print ("\n[+] BeniW Port Scan\n")
	print ("[+] Type bwps.py -h to check the manual \n")
	parser = argparse.ArgumentParser()
	parser.add_argument('-v', dest="version", action='version', version='%(prog)s 1.0 | instagram - @bhonori')
	parser.add_argument("-s", dest="host", action="store", help="Type -s to define the site ")
	parser.add_argument("-p", dest="port", action="store", help="Type -p to scan an expercifica port")
	args = parser.parse_args()

def Conectar():
	if (args.host and args.port):
		print ("Target Host: ",args.host)
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.settimeout(2)
		c = s.connect_ex((str(args.host),int(args.port)))
		if c == 0:
			print ("\nPort ",args.port," Open>")
		else:
				print ("\nPort ",args.port," Closed>")
	else:
		quit()
		
main()
