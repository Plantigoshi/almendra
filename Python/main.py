import time
from Almendra import AlmendraAPI
from Almendra import PistachoAPI

if __name__ == '__main__':
    almendra = AlmendraAPI('/dev/ttyACM0', 115200)
    pistacho = pistachoAPI()

    while(True):
        frame = almendra.getFrame()
        pistacho.postData(frame)

        try:
            flags = pistacho.getFlags()
	    if flags['Riego']:
		almendra.water()
	    if flags['TempCont']:
                almendra.tempCon()			    
        except:
	    raise Exception('Invalid Frame.')           	

        time.sleep(60 * 3)
