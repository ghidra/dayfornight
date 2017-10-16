node = hou.pwd()
geo = node.geometry()

# Add code to modify contents of geo.
# Use drop down menu to select examples.

import json
import os
from pprint import pprint

path="D:/projects/mill/dayfornight/"
d="1508033484"

geo.addAttrib(hou.attribType.Point,"time",0)
geo.addAttrib(hou.attribType.Point,"summary","")
geo.addAttrib(hou.attribType.Point,"precipType","")
geo.addAttrib(hou.attribType.Point,"icon","")
geo.addAttrib(hou.attribType.Point,"temperature",0.0)
geo.addAttrib(hou.attribType.Point,"apparentTemperature",0.0)
geo.addAttrib(hou.attribType.Point,"dewPoint",0.0)
geo.addAttrib(hou.attribType.Point,"humidity",0.0)
geo.addAttrib(hou.attribType.Point,"windSpeed",0.0)
geo.addAttrib(hou.attribType.Point,"windBearing",0)
geo.addAttrib(hou.attribType.Point,"visibility",0)

geo.addAttrib(hou.attribType.Point,"lat",0.0)
geo.addAttrib(hou.attribType.Point,"lon",0.0)

geo.addAttrib(hou.attribType.Point,"id",0)


for f in os.listdir(path):
    if not f.startswith('.'):
        if os.path.isdir(path+f):
            if f==d:
                #for each slice directory... 
                for s in os.listdir(path+f):
                    for dirName, subdirList, fileList in os.walk(path+f+"/"+s):
                        for fname in fileList:
                            filepath = path+f+"/"+s+"/"+fname
                            fnd = fname.split("_")
                                                        
                            p = geo.createPoint()
                            p.setAttribValue("id",int(fnd[0]))
                            #print('\t%s' % fnd[0])
                            
                            with open(filepath) as json_data:
                                d = json.load(json_data)
                                for toplevel in d:
                                    #print toplevel
                                    #if toplevel == 'hourly':
                                        #for hour in range(len(d[toplevel]["data"])):
                                            #print "------------------Hourly"
                                            #for data in d[toplevel]["data"][hour]:
                                                #p.setAttrib(data,d[toplevel]["data"][hour][data])
                                                #print data+":"+str(d[toplevel]["data"][hour][data])
                                    if toplevel == 'currently':
                                        #print "------------------Currently"
                                        for current in d[toplevel]:
                                            if current == "precipType" or current == "summary" or current == "icon":
                                                p.setAttribValue(current,str(d[toplevel][current]))
                                            elif current == "time" or current == "windBearing" or current=="visibility":
                                                p.setAttribValue(current,int(d[toplevel][current]))
                                            elif  current == "temperature" or current == "apparentTemperature" or current == "dewPoint" or current == "humidity" or current == "windSpeed":
                                                p.setAttribValue(current,float(d[toplevel][current]))
                                            #print current+":"+str( d[toplevel][current] )
                                    if toplevel == 'latitude':
                                        p.setAttribValue("lat",float(d[toplevel]));
                                    if toplevel == 'longitude':
                                        p.setAttribValue("lon",float(d[toplevel]));
