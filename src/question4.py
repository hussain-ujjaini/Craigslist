    # Question 4 done by Hussain
    def getItemsInRadius(self, radius, latitude, longitude):
        items = []
        index = 0
        for i in loc:
            lat1 = float(i[0])
            lon1 = float(i[1])

            dst = mpu.haversine_distance((lat1, lon1), (latitude, longitude))
            if dst < radius:
                items.append(datalist[index])
            index += 1
        print items
        return items


