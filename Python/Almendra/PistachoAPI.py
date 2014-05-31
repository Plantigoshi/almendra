import urllib2

class PistachoAPI(object):

    def __init__(self):
        pass

    def postData(self, username, password):
        url = ''
	data = {}
	req = urllib2.Request(url)
	base64string = base64.encodestring('%s:%s' % (username, password)).replace('\n', '')
	request.add_header("Authorization", "Basic %s" % base64string)
	request.add_header('Content-Type', 'application/json')
	result = urllib2.urlopen(request, json.dumps(data))

	return result.read()

    def getData(self):
        url = ''

	return urllib2.urlopen(url).read()
	
