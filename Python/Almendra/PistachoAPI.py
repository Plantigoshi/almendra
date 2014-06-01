import urllib2
import base64
import json


class PistachoAPI(object):

    def __init__(self):
        self.host = 'http://plantigoshi.herokuapp.com/'

    def postData(self, data, plant):
        url = self.host + 'plants/' + str(plant) + '/sync' 
        request = urllib2.Request(url)
        request.add_header('Content-Type', 'application/json')
        result = urllib2.urlopen(request, json.dumps({'data' : data}))

        return result.read()

    def getData(self):
        url = self.host
        return urllib2.urlopen(url).read()

    def getFlags(self):
        url = self.host
        return urllib2.urlopen(url).read()
