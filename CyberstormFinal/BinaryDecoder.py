# Name: Ryan Parker
# Date: 3/28/18
# Assignment: Binary Decoder

# To run: python Parker_Program1.py

import sys # imports function to print later
string = raw_input() # assigns input to 'string'

if(len(string) % 7 == 0): # If code is 7-bit
    for i in range(0, (len(string)/7)):
        sys.stdout.write(chr(int(string[i*7:i*7+7], base=2))), # convert to ASCII(int(String[position: position+7], in binary))
    print('')

elif(len(string) % 8 == 0): #if code is 8-bit
    for i in range(0, (len(string)/8)):
        sys.stdout.write(chr(int(string[i*8:i*8+8], base=2))), # convert to ASCII(int(String[position: position+8], in binary))
    print('')

else: # failsafe in case binary is misentered
    print('Binary is neither 7 nor 8 bit, please try again')
