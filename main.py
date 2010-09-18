from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.api import namespace_manager

class HomeHandler( webapp.RequestHandler ):
    def get(self):
        namespace = namespace_manager.get_namespace()
        self.response.out.write('namespace: %s' % namespace)

def application():
    return webapp.WSGIApplication([ ( '/', HomeHandler ) ], debug=True)

if __name__ == '__main__':
    run_wsgi_app( application() )
