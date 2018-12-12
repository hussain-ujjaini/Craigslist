import cherrypy
from src.Craigslist import *

cherrypy.config.update({'server.socket_host' : '127.0.0.1', 'server.socket_port': 10001})
c = Craigslist()

class app(object):


    @cherrypy.expose
    def index(self):
        return "Craigslist"

    @cherrypy.expose
    def getlocation(self, location1 = [36.16857232693774, -115.14401662181169]):
	
	loc = c.getItemByLocation1(location1)
	print(loc)
	return json.dumps(loc)

    @cherrypy.expose
    def getitem(self, id ='123'):
	#cherrypy.request.params.get(idInput)
	#print(uid)
	print("In getitem: ",id)
	pid = c.getItemById(id)
	print(pid)
	return json.dumps(pid)


if __name__ == '__main__':
    cherrypy.quickstart(app())
