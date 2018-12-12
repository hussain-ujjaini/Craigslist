from src.Craigslist import *
import cherrypy
import json

class app(object):

    @cherrypy.expose
    def index(self):
        return open('views/index.html')

    @cherrypy.expose
    @cherrypy.tools.accept(media='text/plain')
    def api(self, inputbtn):
        if(cherrypy.request.params.get("inputbtn")=="status"):
            return open('views/inputStatus.html')
        elif(cherrypy.request.params.get("inputbtn")=="userid"):
            return open('views/inputUserid.html')
        elif (cherrypy.request.params.get("inputbtn") == "inradius"):
            return open('views/inputxy.html')
        else:
            return "some error occured"

    @cherrypy.expose
    @cherrypy.tools.accept(media='text/plain')
    def getitemslist(self, **params):
        c = Craigslist()
        for k in params:
            if k == "status":
                print "in status check"
                status = cherrypy.request.params.get("status")
                print type(status)
                #status = str(status)
                print type(status)
                statusList = c.getItemsByStatus(status)
                print statusList
                return json.dumps(statusList)

            elif k == "userid":
                print "in userid check"
                userid = cherrypy.request.params.get("userid")
                print userid
                return json.dumps(c.getItemsByUserId(str(userid.encode('ascii'))))

            else:
                return "some error occured"

    @cherrypy.expose
    @cherrypy.tools.accept(media='text/plain')
    def getitemsinradius(self, **params):
        c = Craigslist()
        radius = cherrypy.request.params.get("xy")
        latitude = cherrypy.request.params.get("xx")
        longitude = cherrypy.request.params.get("yy")
        return json.dumps(c.getItemsInRadius(radius, latitude, longitude))


if __name__ == '__main__' :
    cherrypy.quickstart(app())
