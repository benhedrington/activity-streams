#!/usr/bin/env python
import wsgiref.handlers
import os

from google.appengine.ext import db
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template

def throwNotFound(self):
  self.error(404)
  template_values = {
     'foo': 'bar',
  }
  path = os.path.join(os.path.dirname(__file__), 'templates/404.html')
  self.response.headers['Content-Type'] = 'text/html'
  self.response.out.write(template.render(path, template_values))
  
class schemaHandler(webapp.RequestHandler):
  def get(self, ver, name):
    filestring = 'schema/'+ver+'/'+name+'.html'
    if os.path.isfile(filestring):
      filepath = os.path.join(os.path.dirname(__file__), filestring)
      template_values = {
         'ver': ver,
         'name': name,
         'incpath': filepath,
      }
      path = os.path.join(os.path.dirname(__file__), 'templates/schema.html')
      self.response.headers['Content-Type'] = 'text/html'
      self.response.out.write(template.render(path, template_values))
    else:
      throwNotFound(self)

class notfoundHandler(webapp.RequestHandler):
  def get(self):
    throwNotFound(self)

application = webapp.WSGIApplication([
  (r'/schema/(.*)/(.*)/', schemaHandler),
  (r'/schema/(.*)/(.*)', schemaHandler),
  ('/.*', notfoundHandler)
], debug=True)

def main():
  wsgiref.handlers.CGIHandler().run(application)

if __name__ == '__main__':
  main()