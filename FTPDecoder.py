from ftplib import FTP
import sys, re

#* means needs a number value

def decode(x,n):
    #split binary string into n-sized bits
	binary = [x[i : i + n] for i in range(0, len(x),n)]

    #covert to ASCII and print
	for ch in binary:
		print(chr(int(ch,2)), end="")

ftp = FTP('jeangourd.com') #could also do FTP(host)
#ftp.connection(host, int(port, *port#))
#if user = "":
ftp.login("anonymous","");
#else:
#ftp.login(user, password)
data = []
 
ftp.dir()

#takes dir listing 
binary_String = ""
#needs to get dir list
#binary_String = 
#decode(binary_String, int(mode,10)) 
ftp.quit()
