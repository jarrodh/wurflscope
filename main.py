#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from google.appengine.ext import db
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app

import datetime
import os


#from device import Device


class MainHandler(webapp.RequestHandler):
    def get(self):
#        device = Device(name = "TestPhone", user_agent = "Some_UserAgent")
#        device.put()
        
 #       devices = db.GqlQuery("SELECT * FROM Device")
 #       dev = devices.fetch(1)
        
#        self.response.out.write('Device Name is: %s' % dev[0].name)

        path = os.path.join(os.path.dirname(__file__), 'templates/main.html')
        page = template.render(path, {}) #, template_values)
        self.response.out.write(page)
        
    def post(self):
        template_values = { 
            "device": "HTC Hero"
            }
        
        path = os.path.join(os.path.dirname(__file__), 'templates/main.html')
        page = template.render(path, template_values)
        self.response.out.write(page)


def main():
    application = webapp.WSGIApplication([("/", MainHandler)],
                                         debug=True)
    run_wsgi_app(application)


if __name__ == "__main__":
    main()
