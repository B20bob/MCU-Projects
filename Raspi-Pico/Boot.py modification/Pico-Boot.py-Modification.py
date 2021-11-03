import board
import time
from digitalio import DigitalInOut,Pull

led = DigitalInOut(board.LED)
led.switch_to_output()

safe = DigitalInOut(board.GP14) # <----- choose your pin with a button on it
safe.switch_to_input(Pull.UP)

def reset_on_pin():
	if safe.value is False:
		import microcontroller
		microcontroller.on_next_reset(microcontroller.RunMode.SAFE_MODE)
		microcontroller.reset()

led.value = False
for x in range(16):
	reset_on_pin()
	led.value = not led.value
	time.sleep(0.1)