import socket
import sys
from time import time
from binascii import unhexlify

ZERO = 0.025
ONE = 0.085
port = 31337
debug = False

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.jeangourd.com", port))

data = s.recv(4096)

covert_bin = ""
while (data.rstrip("\n") != "EOF"):
    sys.stdout.write(data)
    sys.stdout.flush()

    t0 = time()
    data = s.recv(4096)
    t1 = time()
    delta = round(t1-t0, 3)
    if (debug):
        print delta
    if (delta >= ONE):
        covert_bin += "1"
    else:
        covert_bin += "0"

s.close()

if(debug):
    print covert_bin

covert = ""
i = 0
while (i < len(covert_bin)):
    #process one byte at a time
    b = covert_bin[i:i + 8]
    #covert it to ASCII
    n = int("0b{}".format(b), 2)
    try:
        covert += unhexlify("{0:x}".format(n))
    except TypeError:
        covert += "?"
    # stop at the string "EOF"
    i += 8

print covert
