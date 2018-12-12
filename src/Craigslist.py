import json
from scipy.spatial import distance
from math import sin,cos, radians, atan2, sqrt
pid = []
loc = []
userId = []
description = []
price = []
status = []
datalist = []

class Craigslist:

    def managing_json(self):
        with open("/home/meditab/Craigslist/data/json_data.json", "r") as read_file:
            data = json.load(read_file)
            print len(data)
            for inputs in data:
                pid.append(inputs["id"])
                loc.append(inputs["loc"])
                userId.append(inputs["userId"])
                description.append(inputs["description"])
                price.append(inputs["price"])
                status.append(inputs["status"])
                datalist.append(inputs)
        print len(loc)
	
    #Question 2 done by jeet
    def getItemById(self, idInput):
      print("In getItemId: ", idInput[0:],pid)
      for i in pid:
        print(123)
	print("i:",i)
	print("input id: ",i,idInput)
        if i==idInput:
          print(idInput)
          index = pid.index(i)
          print("Item1: ", datalist[index])
      	  return datalist[index]
          
          
    def getItemByLocation(self, locInput1,locInput2):
      for i in loc:
        if i[0]==locInput1 and i[1]==locInput2:
          print(i)
          index = loc.index(i)
          print("Item2: ", datalist[index])
	  return datalist[index]

    def getItemByLocation1(self, locInput1):
      
      for i in loc:
	j=i
	print("Compare:",str(j),locInput1)
	j = str(j).replace(" ", "")
        if j == locInput1:
          index = loc.index(i)
          print("Item2: ", datalist[index])
      	  return datalist[index] 	

    # Question 3 done by Hussain
    def getItemByStatus(self, statusInput):

        statusList = []
        for i in range(0, len(status)-1):
            print i
            if status[i] == statusInput:
                #print data[0]
                statusList.append(datalist[i])
        print statusList
        return statusList


    def getItemsByUserId(self, useridInput):
        userIdList = []
        for i in range(len(userId)-1):
            if userId[i] == useridInput:
                userIdList.append(datalist[i])
        print userIdList
        return userIdList

     #Question 4 by jeet
    def getItemsInRadius(self, radius, latitude, longitude):
        items = []
        index = 0
        for i in loc:
	    #i[0] = (i[0]*3.14)/180
	    #i[1] = (i[1]*3.14)/180
	    #latitude = latitude*3.14/180
	    #longitude = longitude*3.14/180
            #dist = math.acos(math.sin(latitude) * math.sin(i[0]) + math.cos(latitude)*math.cos(i[0]) *(math.cos(longitude)-math.cos(i[1]))*6371)
            r = 6371
	    lat1 = i[0]
	    lon1 = i[1]
	    lat2 = latitude
	    lon2 = longitude
	    dist_lat = float(lat2) - float(lat1)
	    dist_lon = float(lon2) - float(lon1)
 	    

	    a = sin(dist_lat / 2)**2 + cos(float(lat1)) * cos(float(lat2)) * sin(dist_lon / 2)**2  
    	    c = 2 * atan2(sqrt(a), sqrt(1 - a))  
            dist = r * c
	    
            if (dist < radius):
		index = loc.index(i)
                items.append(datalist[index])
            
        print items
        return items

    


if __name__ == '__main__':
    c = Craigslist()
    c.managing_json()
    #c.getItemByStatus("removed")
    #c.getItemsByUserId("53f6c9c96d1944af0b00000b")
    #c.getItemById("53fcc82a45b6f4db35000001")
    #c.getItemByLocation(36.16857232693774,-115.14401662181169)
    #c.getItemsInRadius(20, 20,100)
    #c.getItemByLocation1([36.16857232693774, -115.14401662181169])
