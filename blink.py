from gpiozero import LED
from time import sleep

#Initialize the LED connected to GPIO 17
led = LED(17)

print("Starting LED blink program. Press Ctrl + C to exit.")

Looping  = True



while Looping:
	led.on() #Turn LED on
	sleep(1) #Wait for one sec
	led.off() #Turn LED off
	sleep(1) #Wait for 1 second

#except KeyboardInterrupt:
#	print("\nProgram ending...")


