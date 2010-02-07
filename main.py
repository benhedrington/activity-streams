#!/usr/bin/env python
import wsgiref.handlers
import os

from google.appengine.ext import db
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template

class MainHandler(webapp.RequestHandler):
  def get(self):
    template_values = {
      'foo': "bar",
      'bar': "foo"
    }
    path = os.path.join(os.path.dirname(__file__), 'templates/index.html')
    self.response.headers['Content-Type'] = 'text/html'
    self.response.out.write(template.render(path, template_values))

def main():
  application = webapp.WSGIApplication(
                                       [('/', MainHandler)],
                                       debug=True)
  wsgiref.handlers.CGIHandler().run(application)

if __name__ == "__main__":
  main()
