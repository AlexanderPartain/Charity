from ftplib import FTP
import sys, re

def paramsList():
	pass

def directoryList():
	pass

#split binary string into n-sized bits
def decode(x,n):
   
	binary = [x[i : i + n] for i in range(0, len(x),n)]

    #covert to ASCII and print
	for ch in binary:
		print(chr(int(ch,2)), end="")

#Establishes FTP connection
ftp = FTP('jeangourd.com') #could also do FTP(host)
#ftp.connection(host, int(port, *port#))
#if user = "":
ftp.login("anonymous","");
#else:
#ftp.login(user, password)
data = []
ftp.dir()

#Takes directory listing 
binary_String = ""
#needs to get directory list
#binary_String = 
#decode(binary_String, 10) takes line to decode, number of bytes to solve it by
ftp.quit()
