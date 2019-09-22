from gpiozero import LED
from time import sleep

red = LED(14)
yellow = LED(15)
green = LED(18)

while True:
	red.on()
	sleep(5)

	yellow.on()
	sleep(1)

	red.off()
	yellow.off()
	green.on()
	sleep(5)

	green.off()
	yellow.on()
	sleep(1)

	yellow.off()
