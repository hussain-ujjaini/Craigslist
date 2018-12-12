import cherrypy
from src.Craigslist import *

cherrypy.config.update({'server.socket_host' : '127.0.0.1', 'server.socket_port': 10001})
c = Craigslist()
c.managing_json()
class app(object):


    @cherrypy.expose
    def index(self):
        return "Craigslist"
	
    @cherrypy.expose
    def getitem(self, **params):
	
	for i in params:
		if i == "id":
			id = cherrypy.request.params.get("id")
			pid = c.getItemById(id)
			print(pid)
			return json.dumps(pid)
		elif i == "location":
			location = cherrypy.request.params.get("location")
			loc = c.getItemByLocation1(location)
			print("In app: ",loc)
			return json.dumps(loc)

			
		else:
			return "Error"

    @cherrypy.expose
    def getiteminradius(self, **params):
	radius = cherrypy.request.params.get("radius")
	latitude = cherrypy.request.params.get("latitude")
	longitude = cherrypy.request.params.get("longitude")
	points = c.getItemsInRadius(radius, latitude,longitude)
	return json.dumps(points)


if __name__ == '__main__':
    cherrypy.quickstart(app())
    


