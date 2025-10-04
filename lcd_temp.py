#!/usr/bin/env python3

import time
from seeed_dht import DHT
from grove.display.jhd1802 import JHD1802

def main():
	lcd = JHD1802()
	sensor = DHT('11', 5)
	while True:
		lcd.clear()
		humi, temp = sensor.read()
		print('temp {}C, humi {}%'.format(temp, humi))
		lcd.setCursor(0, 0)
		lcd.write('temp: {0:2}C'.format(temp))
		lcd.setCursor(1,0)
		lcd.write('humi: {0:5}%'.format(humi))
		time.sleep(1)
if __name__ == '__main__':
	main()
