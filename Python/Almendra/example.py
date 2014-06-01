import time
from AlmendraAPI import AlmendraAPI

almendra = AlmendraAPI("/dev/ttyUSB0", 115200)
almendra.water()
time.sleep(5)
print almendra.getFrame()
