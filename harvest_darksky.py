import urllib, json

key=""
lat = 29.7604
lon = 95.3698

#https://stackoverflow.com/questions/12965203/how-to-get-json-from-webpage-into-python-script
#i need to just add in time to get historical data
#https://darksky.net/dev/docs/time-machine
url = "https://api.darksky.net/forecast/"+key+"/"+str(lat)+","+str(lon)
response = urllib.urlopen(url)
data = json.loads(response.read())

#https://stackoverflow.com/questions/5214578/python-print-string-to-text-file
with open("_"+str(lat)+"_"+str(lon)+".txt", "w") as text_file:
    text_file.write(str(data))

print data