import json 
from serial import Serial


class AlmendraAPI(object):

    def __init__(self, port, baud):
        self.serial = Serial(port, baud)

    def getFrame(self):
        self.serial.write('G')
        return json.loads(self.serial.readline())

    def water(self):
        self.serial.write('T')

    def tempCont(self):
        self.serial.write('R')
