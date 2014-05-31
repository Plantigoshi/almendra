from serial import Serial


class AlmendraAPI(object):

	def __init__(self, port, baud):
		self.serial = Serial(port, baud)

	def getFrame(self):
		self.serial.write('G')
		return self.serial.readLine()

	def water(self):
		self.serial.write('R')

	def tempCont(self):
		self.serial.write('T')
