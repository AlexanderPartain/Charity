# Team Name: Charity (Kimberly Atienza, Joesph Bingham, Keith Horace, Darren Johnson, Ryan Parker, Alexander Partain, Emiley Smith, Kenton Wilhelm)
# Date: 4/6/18
# Assignment: FTP Decoder


from ftplib import FTP
import sys

ftp = FTP()
ftp.connect('138.47.132.200', "8008")
ftp.login('good','goodGOODgood');
data = []
perm = []
perm2 = []
binary = []
templist =[]
final = ""
binaryMessage = "";
ftp.cwd(".lookee-here")
ftp.cwd("now-in-here")
ftp.dir(data.append)


i = 0
j = 0
for line in data:
    perm.append(data[i][:10])   
    i += 1

for line in perm:           # converts data into binary
    binary.append("")
    for a in perm[j]:
        if a == '-':
            binary[j]+= "0"
        else:
            binary[j]+= "1"
    j += 1

for line in binary:         # adds all binary strings into a single line
    binaryMessage += line


for i in range(0,len(binaryMessage),10): # makes new array of binary bits that fit into 7-bit ascii
    templist.append(binaryMessage[i:i+10])

for i in templist: # ignores 7-bit messages if one of the first three bits is 1
    if (int(i[0:3]) == 0):
        final += i[3:]


x = len(binaryMessage) % 7 # sets binaryMessage to be 10-bit binary conversion
binaryMessage = binaryMessage[0:len(binaryMessage)-x]




# print functions

if(len(final) % 7 == 0): # If code is 7-bit
    print('')
    print("This is the message decoded using 7-bits:")
    for i in range(0, (len(final)//7)):
        sys.stdout.write(chr(int(final[i*7:i*7+7], base=2))), # convert to ASCII(int(String[position: position+7], in binary))
    print('')

if(len(binaryMessage) % 7 == 0): # If code is 10-bit
    print('')
    print("This is the message decoded using 10-bits:")
    for i in range(0, (len(binaryMessage)//7)):
        sys.stdout.write(chr(int(binaryMessage[i*7:i*7+7], base=2))), # convert to ASCII(int(String[position: position+7], in binary))
    print('')


elif(len(binaryMessage) % 8 == 0): #if code is n-bits long (to be changed if necessary, currently 8)
    for i in range(0, (len(binaryMessage)//8)):
        sys.stdout.write(chr(int(binaryMessage[i*8:i*8+8], base=2))), # convert to ASCII(int(String[position: position+8], in binary))
    print('')

    
    
ftp.quit()
