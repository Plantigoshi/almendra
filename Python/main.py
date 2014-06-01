import time
from Almendra import AlmendraAPI
from Almendra import PistachoAPI

if __name__ == '__main__':
    almendra = AlmendraAPI.AlmendraAPI('/dev/ttyUSB0', 115200)
    pistacho = PistachoAPI.PistachoAPI()

    while(True):
        frame = almendra.getFrame()
        pistacho.postData(frame, 1)

	if pistacho.wateringFlag(1) == 'true':
	    almendra.water()      

	if pistacho.temperatureFlag(1) == 'true':
	    almendra.tempCont()
     	
        time.sleep(1)
