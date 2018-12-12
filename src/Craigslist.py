import json
from scipy.spatial import distance
import math

pid = []
loc = []
userId = []
description = []
price = []
status = []
datalist = []

class Craigslist:

    def managing_json(self):
        with open("../data/json_data.json", "r") as read_file:
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
        print len(status)

    #Question1 done by dhwani
    def getsorteddata(self):

    	print "The list printed sorting by price in an ascending order: "
    	print sorted(datalist, key = lambda i: i['price'])
    
    	print "The list printed sorting by price in an descending order:"
    	print sorted(datalist, key = lambda i: i['price'],reverse=True) 

	
    #Question 2 done by jeet
    def getItemById(self, idInput):
      for i in pid:
       # print(i)
        if i==idInput:
          print(i)
          index = pid.index(i)
          print(index)
          print("Item1: ", datalist[index])
          
          
    def getItemByLocation(self, locInput1,locInput2):
      for i in loc:
        if i[0]==locInput1 and i[1]==locInput2:
          print(i)
          index = loc.index(i)
          print("Item2: ", datalist[index])

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
   
    #Question 4 done by Dhwani
    def get_items_in_radius(self,latitudeInDegrees,longitudeInDegrees,distanceInKm):
     lat = math.radians(latitudeInDegrees)
     lon = math.radians(longitudeInDegrees)
     distance = 1000*distanceInKm
    
     test_lat = -154
     test_lon =  140
    
     RADIUS_OF_EARTH  = 6371
     # Radius of the parallel at given latitude
     pradius = RADIUS_OF_EARTH*math.cos(lat)
    
     latMin = lat - distance/RADIUS_OF_EARTH
     latMax = lat + distance/RADIUS_OF_EARTH
     lonMin = lon - distance/pradius
     lonMax = lon + distance/pradius
     rad2deg = math.degrees
     print(rad2deg(latMin), rad2deg(lonMin), rad2deg(latMax), rad2deg(lonMax))
    
     if(test_lat>=latMin and test_lat<=latMax and test_lon>=lonMin and test_lon<=lonMax):
       print("Point lies within the vicinity")
      
     else:
       print("Point outside of the vicinity")



if __name__ == '__main__':
    c = Craigslist()
    c.managing_json()
    #c.getItemByStatus("removed")
    #c.getItemsByUserId("53f6c9c96d1944af0b00000b")
    #c.getItemById("53fcc82a45b6f4db35000001")
    #c.getItemByLocation(36.16857232693774,-115.14401662181169)
    c.getsorteddata()
    c.get_items_in_radius(36.16327763694836,-115.14098095792328,20)
