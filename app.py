from src.Craigslist import *
import cherrypy
import json

class app(object):

    # Marks the beginning of API
    @cherrypy.expose
    def index(self):
        return open('views/index.html')

    # Redirects the requests as per value received by user
    @cherrypy.expose
    @cherrypy.tools.accept(media='text/plain')
    def api(self, inputbtn):
        # Redirect for status input
        if(cherrypy.request.params.get("inputbtn")=="status"):
            return open('views/inputStatus.html')
        # Redirect for userid input
        elif(cherrypy.request.params.get("inputbtn")=="userid"):
            return open('views/inputUserid.html')
        # Redirect for radius input
        elif (cherrypy.request.params.get("inputbtn") == "inradius"):
            return open('views/inputxy.html')
        else:
            return "some error occured"

    # Provides response to the status or userid given by user in json format
    @cherrypy.expose
    @cherrypy.tools.accept(media='text/plain')
    def getitemslist(self, **params):
        c = Craigslist()
        for k in params:
            # json response for matching status value
            if k == "status":
                print "in status check"
                status = cherrypy.request.params.get("status")
                print type(status)
                #status = str(status)
                print type(status)
                statusList = c.getItemsByStatus(status)
                print statusList
                return json.dumps(statusList)
            # json response for matching userid value
            elif k == "userid":
                print "in userid check"
                userid = cherrypy.request.params.get("userid")
                print userid
                return json.dumps(c.getItemsByUserId(str(userid)))

            else:
                return "some error occured"

    # Provides the list of records lying under the given radius as per latitude and longitude
    @cherrypy.expose
    @cherrypy.tools.accept(media='text/plain')
    def getitemsinradius(self, **params):
        c = Craigslist()
        radius = cherrypy.request.params.get("radius")
        latitude = cherrypy.request.params.get("latitude")
        longitude = cherrypy.request.params.get("longitude")
        return json.dumps(c.getItemsInRadius(radius, latitude, longitude))


if __name__ == '__main__' :
    cherrypy.quickstart(app())
