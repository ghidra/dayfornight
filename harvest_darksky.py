import urllib, json
import math

online = False
key = ""
lat = 29.7604
lon = 95.3698
#
#lat is north and west. higher vales are more north. 0.001 is like a avenue
#lon is east and south. higher values are west.
#i need to get an aspect ratio to determine our grid
#get width samples and height samples
#as well as the max degrees will fit the largest w/h dime
maxDegree = 1.0 #about 69 miles 111 kilometers
width = 18
height = 10

#time to do some more grids, how many times do i have to do this
for i in range(0,width*height):
	row = math.floor(i/width)
	col = i%width
	print str(row)+":"+str(col)
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