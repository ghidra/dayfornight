import urllib, json
import math
import time
import calendar
import os

online = False
####################################
key = ""
lon = 95.3698
lat = 29.7604
maxDegree = 1.0 #about 69 miles 111 kilometers
width = 31
height = 31
#lat is north and west. higher vales are more north. 0.001 is like a avenue
#lon is east and south. higher values are west.
#i need to get an aspect ratio to determine our grid
#get width samples and height samples
#as well as the max degrees will fit the largest w/h dime
####################################

#get the key
file = open('key.txt', 'r') 
key = file.read()
print key

aspect = height/float(width)

#starting point in lat lon
x = lon+(maxDegree*0.5)
y = lat+(maxDegree*aspect*0.5)

#scale between each node to fit max degrees of map in
sx = 1/float(width)
sy = 1/float(height)
	
#time
year="2017"
month="08"
date="25"
hour="23"
minute="00"
seconds="00"

fps = 0.001
timeslices=math.ceil(5*60*fps)
print "5 minutes at "+str(fps)+" fps is: "+str(timeslices)+" time slice queries."
print "multiplied by "+str(width*height)+" for a "+str(width)+"x"+str(height)+" grid."
print "which will cost: $"+str( ((timeslices*width*height)-1000)*0.0001 )
#might be easier to convert that to unix
# time difference of houston from gmt
timezoneDifference = -5*3600
#https://www.epochconverter.com/
#https://docs.python.org/2/library/time.html
counter = 0
print "---------------------------"
for i in range(0,int(timeslices)):
	print "----start:"+str(counter)
	timestr = str(month)+" "+str(date)+" "+str(hour)+":"+str(minute)+":"+str(seconds)+" "+str(year)
	unixTime = calendar.timegm(time.strptime(timestr, "%m %d %H:%M:%S %Y"))
	unixTime+=timezoneDifference
	print "date: "+timestr
	print "epoch time: "+str(unixTime)

	directory="slice_"+str(counter)
	if not os.path.exists(directory):
		os.makedirs(directory)
		print "made directory: "+directory

#https://stackoverflow.com/questions/12965203/how-to-get-json-from-webpage-into-python-script
#i need to just add in time to get historical data
#https://darksky.net/dev/docs/time-machine
	
	for i in range(0,width*height):
		row = math.floor(i/width)
		col = float(i%width)

		stepx = sx*col
		stepy = sy*row

		sample_lon = round((x-stepx)*10000.0)/10000.0
		sample_lat = round((y-stepy)*10000.0)/10000.0
		
		#print str(counter)+": "+str(int(row))+","+str(int(col))+" - "+str(sample_lat)+","+str(sample_lon)
		#if (col==width-1):
		#	print "\n"

		url = "https://api.darksky.net/forecast/"+key+"/"+str(sample_lat)+","+str(sample_lon)+","+str(unixTime)

		if online:
			response = urllib.urlopen(url)
			data = json.loads(response.read())

			#https://stackoverflow.com/questions/5214578/python-print-string-to-text-file
			#with open("_"+str(lat)+"_"+str(lon)+".txt", "w") as text_file:
			with open(diretory+"/coords_"+str(lat)+"_"+str(lon)+"_"+str(counter)+".txt", "w") as text_file:
			    text_file.write(str(data))

			#print data