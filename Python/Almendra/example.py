import time
from PistachoAPI import PistachoAPI
from AlmendraAPI import AlmendraAPI

pistacho = PistachoAPI()
almendra = AlmendraAPI("/dev/ttyUSB0", 115200)
almendra.water()
time.sleep(5)
pistacho.postData(almendra.getFrame(), 1)
