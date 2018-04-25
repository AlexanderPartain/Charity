import datetime
import time
import hashlib
import sys
#IN PYTHON 3

######## epoch input time ################
p = "%Y %m %d %H %M %S"
#debug/setting epoch test
#epoch = int(time.mktime(time.strptime('2017 01 01 00 00 00', p)))
#print ('new epoch: ',epoch)

set_epoch = []

#getting epoch time from input
set_epoch = list(map(int, str(sys.stdin.read()).strip().split(" "))) 

epoch = datetime.datetime(set_epoch[0], set_epoch[1], set_epoch[2], set_epoch[3], set_epoch[4],set_epoch[5],0).replace(microsecond=0)
epoch = datetime.datetime.utcfromtimestamp(epoch.timestamp()) 

#get acutally epoch times
real_epoch = int(time.time()) 

################ computer time ##################
#debugging with a set epoch
#sys_time = int(time.mktime(time.strptime('2015 05 15 14 00 00', p)))
#comment this out if debuggin w/out set epoch 
#sys_time = datetime.datetime.utcfromtimestamp(sys_time)

time = datetime.datetime.today().replace(microsecond=0) ##gets system time
time = time.strftime(p) #reformates it
time = str(time) #strings time
set_time = list(map(int, str(time).strip().split(" "))) 

sys_time = datetime.datetime(set_time[0], set_time[1], set_time[2], set_time[3], set_time[4], set_time[5],0).replace(microsecond=0)
sys_time = datetime.datetime.utcfromtimestamp(sys_time.timestamp())

############### subtracting the sys_time and epoch ####################################

result = int((sys_time - epoch).total_seconds())
result = result - (result%60)
#result = real_epoch - epoch #epoch takes the unix epoch - the time input as epoch

orig_date = str(result)	#convert time to string

############### Md5 Sum calculator ########################################

list1 = list(hashlib.md5(str(hashlib.md5(str(result).encode('utf-8')).hexdigest()).encode('utf-8')).hexdigest())

############# Concat the 1st 2 letters(L-R) and 1st 2 num (R-L)#############################
final = ""

i = 0
while i < len(list1):
    if list1[i].isalpha(): #checks to see if index is a char
        final += list1[i]
        list1.pop(i) 

        if len(final) > 1:
            break
    else:
        i +=1

i = len(list1) - 1 #looks at list from the tail
while i >=0:
	if list1[i].isnumeric(): #checks to see if index is a num
		final += list1[i]
		if len(final) > 3:
			break
	i -= 1

if len(final) < 4:
	for ch in list1:
		if ch.isalpha():
			final += ch
		if len(final) > 3:
			break
print (final) 

