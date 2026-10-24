from gpiozero import LED
from time import sleep
import random

#Initialize the LED connected to GPIO 17

running = True
blue_1 = LED(4)
blue_2 = LED(19)
red_1 = LED(17)
red_2 = LED(13)
green_1 = LED(27)
green_2 = LED(6)
yellow_1 = LED(22)
yellow_2 = LED(5)

lit_sequence = [blue_1, blue_2, red_1, red_2, green_1, green_2, yellow_1, yellow_2]

print("Starting LED blink program. Press Ctrl + C to exit.")

try:
	while running:
		chosen = lit_sequence[random.randrange(6)]
		chosen.on()
		sleep(1.5)
		chosen.off()
		sleep(1.5)


except KeyboardInterrupt:
	print("\nBlinking is ending...")
