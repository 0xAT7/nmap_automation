import socket
import os
import sys
import threading
import colorama
from colorama import Fore, Style

print(Style.BRIGHT + Fore.RED + '''

	    ___  ______  _____
	   /   |/_  __/ /__  /
	  / /| | / /      / / 
	 / ___ |/ /      / /  
	/_/  |_/_/_____ /_/   
	         /_____/
''')
print(Fore.YELLOW + '''              CODED BY : A.Tarek
''')


def process():
	try:
		filepath = sys.argv[1]
		with open (filepath,'r') as file:
			for line in file:
				try:
					ip = socket.gethostbyname(str(line.strip()))
					finall=open('result.txt','a')
					finall.write('{}\n'.format(ip))
				except:
					pass
	except:
		print ("Please enter exist subdomains file\n"+Fore.GREEN+"Usage: python nmap.py subdomains.txt")
		sys.exit(1)
process()

print(Fore.GREEN + "Extracting IPs Done!....")
print(Fore.YELLOW + "Time to Nmap....")
print(Fore.GREEN + ''' ''')
os.system('sort -u result.txt > IPs.txt && nmap -iL IPs.txt -o nmap-result.txt && rm -r result.txt')
