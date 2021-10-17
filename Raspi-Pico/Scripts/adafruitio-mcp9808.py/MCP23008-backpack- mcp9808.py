# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

"""Simple test for 16x2 character lcd connected to an MCP23008 I2C LCD backpack."""
import time
import board
import busio
import adafruit_character_lcd.character_lcd_i2c as character_lcd
import adafruit_mcp9808

# Modify this if you have a different sized Character LCD
lcd_columns = 20
lcd_rows = 4

# Initialise I2C buses
i2c = busio.I2C(scl=board.GP1, sda=board.GP0)  # uses I2C0
mcpi2c = busio.I2C(scl=board.GP3, sda=board.GP2)  # uses I2C1

# Initialise the lcd class
lcd = character_lcd.Character_LCD_I2C(i2c, lcd_columns, lcd_rows)
mcp = adafruit_mcp9808.MCP9808(mcpi2c, address=0x18)

# Initialize the MCP9808
mcp = adafruit_mcp9808.MCP9808(mcpi2c)

while True:
    
    # Define functions to allow RPLCD to output sensor data
    def read_temp():
        tempC = mcp.temperature
        temp = tempC * 9/5.0 + 32
        temp = str(round(temp, 2))
        temp = str(temp)
        return temp
    
    # Turn backlight on
    lcd.backlight = True

    lcd.message = "    MCP9808 Temp\n\n" + read_temp() + "F"

    time.sleep(30)
    lcd.clear()