import os
import glob
import re
import json
from pprint import pprint

p = "D:/projects/houdini/day_for_night/geo/rain/"
# f = "8_25_23.txt"
fs = []

# with open(p+f) as data_file:    
#     data = json.load(data_file)

# #pprint(data)
# print data["features"][0]["geometry"]["coordinates"][0]
# print data["features"][0]["geometry"]["Text"]
# #print data["features"][0]["geometry"]["type"]
# print data["features"][0]["properties"]["Rainfall"]
# print data["features"][0]["properties"]["SiteId"]



##############################

# for dirName, subdirList, fileList in os.walk(p):
# 	for fname in fileList:
# 	    filepath = p+"/"+fname
# 	    print filepath
	    # fnd = fname.split("_")
	                                
	    # p = geo.createPoint()
	    # p.setAttribValue("id",int(fnd[0]))
	    # #print('\t%s' % fnd[0])
	    
	    # with open(filepath) as json_data:
	    #     d = json.load(json_data)
	    #     for toplevel in d:

##############################
#https://stackoverflow.com/questions/12093940/reading-files-in-a-particular-order-in-python

#sort the file names
numbers = re.compile(r'(\d+)')
def numericalSort(value):
    parts = numbers.split(value)
    parts[1::2] = map(int, parts[1::2])
    return parts

for infile in sorted(glob.glob(p+'*.txt'), key=numericalSort):
	fs.append(infile)

##############################
# for path in fs:
# 	print path

frame=0
with open(fs[frame]) as data_file:    
    data = json.load(data_file)

for i in range(len(data["features"])):
	print data["features"][i]["geometry"]["coordinates"][0]
	print data["features"][i]["geometry"]["Text"]
	print data["features"][i]["geometry"]["type"]
	print data["features"][i]["properties"]["Rainfall"]
	print data["features"][i]["properties"]["SiteId"]
#print len(data["features"])