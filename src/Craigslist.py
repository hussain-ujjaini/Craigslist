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

    # Question 4 done by Hussain
    def getItemsInRadius(self, radius, latitude, longitude):
        items = []
        index = 0
        for i in loc:
            lat = latitude -
            x1 = (radius * math.cos(latitude) * math.cos(longitude), radius * math.cos(latitude) * math.sin(longitude))
            x2 = (float(i[0]), float(i[1]))
            dst = distance.euclidean(x1, x2)
            if dst < radius:
                items.append(datalist[index])
            index += 1
        print items
        return items


if __name__ == '__main__':
    c = Craigslist()
    c.managing_json()
    #c.getItemByStatus("removed")
    #c.getItemsByUserId("53f6c9c96d1944af0b00000b")
    c.getItemsInRadius(40, 36.166540711883776,-115.14080871936427)