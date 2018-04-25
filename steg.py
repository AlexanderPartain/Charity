import sys

#initialize variables
method = ''
storeRetrieve = ''
interval = 0
offset = 0
wrapperFile = ''
hiddenFile = ''
sentinel = [0x0, 0xff, 0x0, 0x0, 0xff, 0x0]

#Set input to be assigned to correct variable
try:
    argMethod = sys.argv[1]
    argStoreRetrieve = sys.argv[2]
    argOffset = sys.argv[3][2:]
    argInterval = sys.argv[4][2:]
    argWrapperFile = sys.argv[5][1:]
    argHiddenFile = sys.argv[6][1:]
except:
    print "Not correct form"

#Function for storing stegged image
def store(method, offset, interval, wrapperFile, hiddenFile):
    i = 0
    hiddenBin = []
    storage = []

    image = open(hiddenFile, 'rb')
    pixValue = image.read(1)
    while(pixValue != ""):
        hiddenBin.append(format(ord(pixValue), '08b'))
        pixValue = image.read(1)

    for sent in sentinel:
        hiddenBin.append(format(ord(chr(sent)), '08b'))

    image = open(wrapperFile, 'rb')
    pixValue = image.read(1)
    while(pixValue != ""):
        storage.append(format(ord(pixValue), '08b'))
        pixValue = image.read(1)

    for j in hiddenBin:
        if(method == '-B'):
            storage[offset+interval*i] = j
        else:
            storage[offset+interval*i] &= 11111110
            storage[offset+interval*i] |= ((j & 10000000) >> 7)
        i += 1

    for byte in storage:
        sys.stdout.write(chr(int(byte, 2)))

#Function when retrieving stegged message
def retrieve(method, offset, interval, wrapperFile):
    #open image
    image = open(wrapperFile, 'rb')

    #initialize variables
    i = 0
    storage = []
    byte_count = 0

    #If retrieving in bit mode
    if(method == '-b'):
        pixValue = image.read(1) #Read byte 
        cur_byte = ''

        #Continue reading bytes until no more message or you reach the seninel
        while (pixValue != "" and sentinel != storage):

            #Are we on a least significant bit
            if (byte_count == offset + i*8*interval + len(cur_byte)*interval):
                pixValue = bin(ord(pixValue))[2:]
                cur_byte += pixValue[len(pixValue) - 1] #Take lest significant byte and add it to the current byte

                #Have we reach a full byte
                if (len(cur_byte) == 8):
                    #If storage checking for the sentinel is the same size as the sentinel then get rid of the index 0 
                    if(len(storage) == len(sentinel)):
                        storage.pop(0)
                    storage.append(int(cur_byte, 2))

                    sys.stdout.write(chr(int(cur_byte, 2))) #write byte to output

                    #reset cur_byte
                    cur_byte = ''
                    i += 1
                    
            byte_count += 1
            pixValue = image.read(1) #Read again
    else:
        #Retrieve in Byte more
        pixValue = image.read(1)

        #Keep cycling through unti reach sentinel or end of image
        while (pixValue != "" and sentinel != storage):

            #If current byte is a byte in interval
            if (byte_count == offset + i*interval):
                if(len(storage) == len(sentinel)):
                    storage.pop(0)
                storage.append(ord(pixValue))

                sys.stdout.write(pixValue) #write to output
                i += 1
            byte_count += 1
            pixValue = image.read(1)


#Variable to go along with input               
storeRetrieve = argStoreRetrieve
hiddenFile = argHiddenFile

#Choose to either store or receive message. Call correct function depending on what is chosen.
if (storeRetrieve == '-s'):
    store(argMethod, int(argOffset), int(argInterval), argWrapperFile, argHiddenFile)
elif (argStoreRetrieve == '-r'):
    retrieve(argMethod, int(argOffset), int(argInterval), argWrapperFile);
