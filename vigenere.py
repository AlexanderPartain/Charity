# Joseph Bingham
# 3/25/2018
# The purpose of this program is to take input and either encode or
# decode the input using the Vigenere Cipher. The user must specify if
# they would like to encode(-e) or decode(-d) and specify a key to use.
######################################################################
import sys

#Create list of a-z characters
alpha = list(map(chr, range(97, 123)))

#initialize variables
counter = 0
answer = ""

#take in tow arguments to decide on key and either encode or decode
arg1 = sys.argv[1]
arg2 = sys.argv[2]

#make key lowercase and no spaces
key = arg2.replace(" ", "").lower()

def encode():
    global counter
    global answer
    global entry
    for i in entry:
        l = i.lower()
        
        #check if reached the end of key
        if(counter >= len(key)):
            counter=0
        #check if character is in the alphabet    
        if(i.lower() in alpha):
            if(i.lower() == i):
                #algorithm for vignere cipher
                num = alpha.index(l) + alpha.index(key[counter]) 
                result = num % 26
                answer += alpha[result].lower()
            #if the current letter is uppercase
            else:
                num = alpha.index(l) + alpha.index(key[counter])
                result = num % 26
                answer += alpha[result].upper()
            
            counter += 1 #increment counter to go to next letter in key
        else:
            answer += i

def decode():
    global counter
    global answer
    global entry
    #If first argument is to decode. Use same steps but different algorithm.            
    for i in entry:
        l = i.lower()
        if(counter >= len(key)):
            counter=0
        if(i.lower() in alpha):
            if(i.lower() == i):
                num = 26 + alpha.index(l) - alpha.index(key[counter])
                result = num % 26
                answer += alpha[result].lower()
            else:
                num = 26 + alpha.index(l) - alpha.index(key[counter])
                result = num % 26
                answer += alpha[result].upper()

            counter += 1
        else:
            answer += i

#Check if stdin was passed in
if not (sys.stdin.isatty()):    
    entry = sys.stdin.readline()
    if(arg1 == '-e'):
            encode()
    elif(arg1 == '-d'):
            decode()
    print(answer)
else:
    #Run loop for continuous cyphering
    while True:
        counter = 0
        answer = ""
        entry = input()
        if(arg1 == '-e'):
            encode()
        elif(arg1 == '-d'):
            decode()
        print(answer)
        
        
