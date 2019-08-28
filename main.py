import sys
import os
import requests
from http.server import HTTPServer, BaseHTTPRequestHandler

class Redirect(BaseHTTPRequestHandler):
   def do_GET(self):
       self.send_response(301)
       r = requests.get('http://news.tvb.com/live/inews')
       self.send_header('Location', r.text[r.text.find('vjvars.vdo_url') + 18:r.text[r.text.find('vjvars.vdo_url') + 18:].find('"') + r.text.find('vjvars.vdo_url') + 18])
       self.end_headers()

print('sbfuysguyfgeuirguigbuie')
HTTPServer(("", environ['PORT'], Redirect)).serve_forever()
