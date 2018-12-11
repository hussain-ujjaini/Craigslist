import cherrypy

class Home(object):
    @cherrypy.expose
    def index(self):
        return open('views/index.html')

    @cherrypy.expose
    @cherrypy.tools.accept(media='text/plain')
    def register(self, email=None, psw=None):
        print "in register"
        email = cherrypy.request.params.get("email")
        psw = cherrypy.request.params.get("psw")
        print (email)
        reg = open("views/print.html").read()
        return reg

if __name__ == '__main__' :
    cherrypy.quickstart(Home())
