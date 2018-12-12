import json
import mpu
import geopy
from geopy.distance import geodesic, vincenty

# Global Parameters
pid = []
loc = []
userId = []
description = []
price = []
status = []
datalist = []
sorted_data = []


class Craigslist:

    # Performs list seperation for each attribute in json object
    def managing_json(self):
        with open("/home/meditab/Documents/Craigslist/data/json_data.json", "r") as read_file:
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

    # Returns the items for matching status value
    def getItemsByStatus(self, statusInput):
        c = Craigslist()
        c.managing_json()
        statusList = []
        for i in range(0, len(status)-1):
            print i
            if status[i] == statusInput:
                statusList.append(datalist[i])
                print statusList
        return statusList

    # Returns the items for matching userid value
    def getItemsByUserId(self, useridInput):
        c = Craigslist()
        c.managing_json()

        userIdList = []
        for i in range(len(userId)-1):
            if userId[i] == useridInput:
                userIdList.append(datalist[i])
        return userIdList


    # Returns the items for records lying inside radius value
    def getItemsInRadius(self, radius, latitude, longitude):
        c = Craigslist()
        c.managing_json()

        itemlist = []
        index = 0
        for i in loc:
            lat1 = float(i[0])
            lon1 = float(i[1])

            print "lat1: ", lat1
            print "lon1: ", lon1
            print "lat2: ", latitude
            print "lon1: ", longitude
            print "radius: ", radius
            '''
            # using mpu
            dst = mpu.haversine_distance((lat1, lon1), (latitude, longitude))
            '''

            # using geopy library
            loc1 = (lat1, lon1)
            loc2 = (latitude, longitude)

            # geopy distance calculation for 2 inputs in (lat,long) format
            dst = geopy.distance.geodesic(loc1, loc2).miles
            print "dst: ", dst
            if float(dst) < float(radius):
                itemlist.append(datalist[index])
            index += 1
        return itemlist

if __name__ == '__main__':
    c = Craigslist()
    c.managing_json()
    #c.getItemsByStatus("removed")
    #c.getItemsByUserId("53f6c9c96d1944af0b00000b")
    c.getItemsInRadius(15, 36.166540711883776,-115.14080871936427)
    #c.sortByPrice()
