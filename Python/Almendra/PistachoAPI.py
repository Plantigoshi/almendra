import urllib2
import base64
import json


class PistachoAPI(object):

    def __init__(self):
        pass

    def postData(self, username, password):
        url = ''
        data = {}
        request = urllib2.Request(url)
        request.add_header('Content-Type', 'application/json')
        result = urllib2.urlopen(request, json.dumps(data))

        return result.read()

    def getData(self):
        url = ''
        return urllib2.urlopen(url).read()

    def getFlags(self):
        url = ''
        return urllib2.urlopen(url).read()
