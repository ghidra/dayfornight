import csv
import time
import datetime

path = "D:/projects/mill/dayfornight/csv/"

file=open( path +"houstonstrong_01_coded-export-20171101-100412.csv", "r")

counter = 0
counterStop = 20

keep = []
keepStr = []

focus = ["Text","[M] _twitter_id","[M] favorites_count: ","[M] followers_count: ","[M] friends_count: ","[M] hashtag: ","[M] influence_score: ","[M] is_retweet: ","[M] object_posted_time: ","[M] real_name: ","[M] retweetcount: ","[M] username: "]

tmp = []

reader = csv.reader(file)
for line in reader:
	if counter==0:
		for i in range(len(line)):
			rm_a="object_twitter" in line[i]
			rm_b="twitter_entities" in line[i]
			rm_c="twitter_quoted" in line[i]
			if not rm_a and not rm_b and not rm_c:
				if line[i] in focus:
					keep.append(i)
					keepStr.append(line[i])
	else:
		if(counter==1):
			for i in range(len(line)):
				if i in keep:
					tmp.append(line[i])


	counter=counter+1
	# if counter<counterStop:
	# 	print str(len(line))
 #    	t=line[1],line[2]
 #    	print(line[2])
 #    	#print( counter )
 #    	counter=counter+1

for i in range(len(keep)):
	#keepStr[keep.index(i)]
	if "object_posted_time" in keepStr[i]:
		print "TIME: "+ str(time.mktime(datetime.datetime.strptime(tmp[i], "%m/%d/%Y %I:%M:%S %p").timetuple()) )
 	print keepStr[i] + " : " + tmp[i]