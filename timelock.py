import datetime
import time
import hashlib

######## epoch input time ################
	
#print time.time()	#epoch time: needs to be like datetime format
print 'epoch time: ',  time.strftime('%Y %m %d %H %M %S', time.localtime(time.time()))
	#testing out epoch...but needs to get input/file


################ computer time ############3

format = "%Y %m %d %H %M %S"

date =  datetime.datetime.today().replace(microsecond=0) 
	#datetime.datetime combinbation fo date and a time
	#YYYY,MM,DD,HR,MIN,SS,MSS,tzinfo
	#replace() replaces a time with desire input: forces change

print 'date :', date #to check computer time

d = date.strftime(format) 	#converts format to Year, month, day, hr, min, s
		#strftime changes format
print 'strftime:', d

#d1 = datetime.datetime.strptime(d, format)	another way to convert
#print 'strptime:', d1.strftime(format) 

orig_date = str(d)	#convert time to string
time = datetime.datetime.strptime(str(orig_date), '%Y %m %d %H %M %S')
t =  time.strftime('%Y %m %d %H %M %S')
print t

############### Md5 Sum calculator ##############
m = hashlib.md5()
m.update(t) 
print m.hexdigest()
m.update(t)
string =  m.hexdigest()
print string


