import time
from Almendra import AlmendraAPI
from Almendra import PistachoAPI

if __name__ == '__main__':
    almendra = AlmendraAPI('/dev/ttyACM0', 115200)
    pistacho = pistachoAPI()

    while(True):
	frame = almendra.getFrame()
	pistacho.postData(frame)

	time.sleep(60)
