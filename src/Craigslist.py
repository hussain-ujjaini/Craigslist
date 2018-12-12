import json
import mpu

pid = []
loc = []
userId = []
description = []
price = []
status = []
datalist = []
sorted_data = []
class Craigslist:

    def managing_json(self):
        with open("/home/meditab/Documents/Craigslist/data/json_data.json", "r") as read_file:
            data = json.load(read_file)
            #sorted_data = sorted(data, key=lambda k:k['price'])
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

    def sortByPrice(self):
        print sorted_data
        return sorted_data

    # Question 3 done by Hussain
    def getItemsByStatus(self, statusInput):
        c = Craigslist()
        c.managing_json()
        statusList = []
        for i in range(0, len(status)-1):
            print i
            if status[i] == statusInput:
                #print data[0]
                statusList.append(datalist[i])
                print statusList
        #print statusList
        return statusList


    def getItemsByUserId(self, useridInput):
        c = Craigslist()
        c.managing_json()

        userIdList = []
        for i in range(len(userId)-1):
            if userId[i] == useridInput:
                userIdList.append(datalist[i])
        #print userIdList
        return userIdList


    # Question 4 done by Hussain
    def getItemsInRadius(self, radius, latitude, longitude):
        c = Craigslist()
        c.managing_json()

        items = []
        index = 0
        for i in loc:
            lat1 = float(i[0])
            lon1 = float(i[1])

            print "lat1: ", lat1
            print "lon1: ", lon1
            print "lat2: ", latitude
            print "lon1: ", longitude
            dst = mpu.haversine_distance((lat1, lon1), (latitude, longitude))
            if dst < radius:
                items.append(datalist[index])
            index += 1
        #print items
        return items

if __name__ == '__main__':
    c = Craigslist()
    c.managing_json()
    #c.getItemsByStatus("removed")
    #c.getItemsByUserId("53f6c9c96d1944af0b00000b")
    c.getItemsInRadius(15, 36.166540711883776,-115.14080871936427)
    #c.sortByPrice()
