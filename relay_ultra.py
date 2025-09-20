import time
from grove.grove_relay import GroveRelay
from grove.grove_ultrasonic_ranger import GroveUltrasonicRanger
from seeed_dht import DHT
from grove.display.jhd1802 import JHD1802

sensor = GroveUltrasonicRanger(5)
lcd = JHD1802()

relay = GroveRelay(16)
while True:
	lcd.setCursor(0, 0)
	lcd.clear()
	distance = sensor.get_distance()
	print('{} cm'.format(distance))
	if distance < 20:
		relay.on()
		print('relay on')
		lcd.write('relay on')
	else:
		relay.off()
		print('relay off')
		lcd.write('relay off')
	time.sleep(1)

