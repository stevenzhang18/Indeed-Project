#!/usr/bin/env python

import jinja2
import os
import datetime
import webapp2


jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))


class HomePage(webapp2.RequestHandler):
  def get(self):
    template = jinja_environment.get_template('base.template')
    self.response.out.write(template.render())

app = webapp2.WSGIApplication([
  ('/', HomePage)],
  debug=True)
