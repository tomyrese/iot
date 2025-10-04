from time import sleep
from grove.adc import ADC
sensor = ADC()

while True:
	value = sensor.read_voltage(0)
	value_1 = sensor.read_raw(0)
	value_2 = sensor.read(0)
	print(value)
	print(value_1)
	print(value_2)
	print('\n')
	sleep(3)
