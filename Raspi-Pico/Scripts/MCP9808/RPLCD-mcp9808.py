#!/usr/bin/python3


from RPLCD import i2c
from time import sleep
import time
import board
import adafruit_mcp9808

# constants to initialise the LCD
lcdmode = 'i2c'
cols = 20
rows = 4
charmap = 'A00'
i2c_expander = 'PCF8574'

# Generally 27 is the address;Find yours using: i2cdetect -y 1 
address = 0x27 
port = 1 # 0 on an older Raspberry Pi

# Initialise the LCD
lcd = i2c.CharLCD(i2c_expander, address, port=port, charmap=charmap,
                  cols=cols, rows=rows)

#Beginning of my code

i2c = board.I2C()  # uses board.SCL and board.SDA

# To initialise using the default address:
mcp = adafruit_mcp9808.MCP9808(i2c,address=0x18)

# To initialise using a specified address:
# Necessary when, for example, connecting A0 to VDD to make address=0x19
# mcp = adafruit_mcp9808.MCP9808(i2c_bus, address=0x19)

while True:
    tempC = mcp.temperature
    tempF = tempC * 9 / 5 + 32

    def lcd_temp():
        temp = tempF
        return temp

print(lcd_temp)    
lcd.write_string(lcd_temp(tempF))
lcd.crlf()
lcd.write_string(tempF)
sleep(3)

lcd.clear()
sleep(5)
lcd.close(clear=True)