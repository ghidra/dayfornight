import urllib, json
import math

online = False
####################################
key = ""
lon = 95.3698
lat = 29.7604
maxDegree = 1.0 #about 69 miles 111 kilometers
width = 16
height = 10
#lat is north and west. higher vales are more north. 0.001 is like a avenue
#lon is east and south. higher values are west.
#i need to get an aspect ratio to determine our grid
#get width samples and height samples
#as well as the max degrees will fit the largest w/h dime
####################################

aspect = height/float(width)

#starting point in lat lon
x = lon+(maxDegree*0.5)
y = lat+(maxDegree*aspect*0.5)

#scale between each node to fit max degrees of map in
sx = 1/float(width)
sy = 1/float(height)

#time to do some more grids, how many times do i have to do this
for i in range(0,width*height):
	row = math.floor(i/width)
	col = float(i%width)

	stepx = sx*col
	stepy = sy*row

	sample_lon = round((x-stepx)*10000.0)/10000.0
	sample_lat = round((y-stepy)*10000.0)/10000.0
	
	print str(row)+":"+str(col)+"_"+str(sample_lat)+":"+str(sample_lon)
	if col == width-1:
		print '\n'

#https://stackoverflow.com/questions/12965203/how-to-get-json-from-webpage-into-python-script
#i need to just add in time to get historical data
#https://darksky.net/dev/docs/time-machine
url = "https://api.darksky.net/forecast/"+key+"/"+str(lat)+","+str(lon)
if online:
	response = urllib.urlopen(url)
	data = json.loads(response.read())

	#https://stackoverflow.com/questions/5214578/python-print-string-to-text-file
	with open("_"+str(lat)+"_"+str(lon)+".txt", "w") as text_file:
	    text_file.write(str(data))

	print data