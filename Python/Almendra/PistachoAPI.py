import urllib2
import base64
import json


class PistachoAPI(object):

    def __init__(self):
        pass

    def postData(self, data):
        url = 'http://plantigoshi.herokuapp.com/'
        request = urllib2.Request(url)
        request.add_header('Content-Type', 'application/json')
        result = urllib2.urlopen(request, json.dumps(data))

        return result.read()

    def getData(self):
        url = 'http://plantigoshi.herokuapp.com/'
        return urllib2.urlopen(url).read()

    def getFlags(self):
        url = 'http://plantigoshi.herokuapp.com/'
        return urllib2.urlopen(url).read()
