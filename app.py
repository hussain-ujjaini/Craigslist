import cherrypy
from src.Craigslist import *

cherrypy.config.update({'server.socket_port': 8080})

class app(object):
    
    @cherrypy.expose
    def index(self):
        #name = cherrypy.request.json.get('name')
        return "Hello"
    
    @cherrypy.expose
    def index(self):
	print "in sort"
	c = Craigslist()
        c.getsorteddata()
	json.dumps()

if __name__ == '__main__':
    
    cherrypy.quickstart(app())
    #cherrypy.quickstart(API(), "/api", API_CONFIG) 
