import cgi

from google.appengine.api import users
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.dist import use_library
use_library('django', '0.96')

from controller import *
from model import *

application = webapp.WSGIApplication(
                                     [('/', Daily),
                                      ('/Deal', Deal)],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()