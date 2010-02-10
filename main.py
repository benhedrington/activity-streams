#!/usr/bin/env python
import wsgiref.handlers
import os

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

class notfoundHandler(webapp.RequestHandler):
  def get(self):
    throwNotFound(self)

class MainHandler(webapp.RequestHandler):
  def get(self):
    template_values = {
      'foo': "bar",
      'bar': "foo"
    }
    path = os.path.join(os.path.dirname(__file__), 'templates/index.html')
    self.response.headers['Content-Type'] = 'text/html'
    self.response.out.write(template.render(path, template_values))

application = webapp.WSGIApplication([
  ('/', MainHandler),
  ('/.*', notfoundHandler)
], debug=True)

def main():
  wsgiref.handlers.CGIHandler().run(application)

if __name__ == '__main__':
  main()