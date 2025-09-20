import time
from grove.grove_mini_pir_motion_sensor import GroveMiniPIRMotionSensor
from grove.grove_relay import GroveRelay

sensor = GroveMiniPIRMotionSensor(16)

relay = GroveRelay(12)

def on_detect():
	print('motion detected')
	relay.on()
	print('relay on')
	time.sleep(1)
	relay.off()
	print('relay off')
sensor.on_detect = on_detect
while True:
	time.sleep(1)
