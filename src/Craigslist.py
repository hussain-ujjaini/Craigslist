import json

class Craigslist:

    def basic(self):
        with open("../data/json_data.json", "r") as read_file:
            data = json.load(read_file)
            id = []
            loc = []
            userId = []
            description = []
            price = []
            status = []
            for inputs in data:
                id.append(inputs["id"])
                loc.append(inputs["loc"])
                userId.append(inputs["userId"])
                description.append(inputs["description"])
                price.append(inputs["price"])
                status.append(inputs["status"])

	def getItemByStatus(self, status):
		return None

    def getItemsByUserId(self, userid):
        return None

if __name__ == '__main__':
    c = Craigslist()
    c.basic()