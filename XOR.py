# Team Name: Charity (Kimberly Atienza, Joesph Bingham, Keith Horace, Darren Johnson, Ryan Parker, Alexander Partain, Emiley Smith, Kenton Wilhelm)
# Date: 4/27/18
# Assignment: XOR cipher

import sys

text = sys.stdin.read() # input from command line

inputkey = open("key", "r", buffering=4096) # open file name 'key' in read mode with buffer of 4096 bytes
key = inputkey.read()

output = "".join(chr(ord(i) ^ ord(j)) for i, j in zip(key, text)) # python xor (^) joined to make string after list

print(output)

inputkey.close()
