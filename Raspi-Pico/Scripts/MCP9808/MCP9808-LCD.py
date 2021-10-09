# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

"""Simple test for 16x2 character lcd connected to an MCP23008 I2C LCD backpack."""
import time
import board
import busio
import adafruit_mcp9808
import adafruit_character_lcd.character_lcd_i2c as character_lcd

# Modify this if you have a different sized Character LCD
lcd_columns = 16
lcd_rows = 4

# Initialise I2C bus.
i2c_mcp9808 = busio.I2C(scl=board.GP1, sda=board.GP0)  # uses I2C0
mcp = adafruit_mcp9808.MCP9808(i2c_mcp9808, address=0x18)

# Initialise the lcd class
i2c_lcd = busio.I2C(scl=board.GP3, sda=board.GP2)  # uses I2C1
lcd = character_lcd.Character_LCD_I2C(i2c_lcd, lcd_columns, lcd_rows, address=0x27)
#lcd = character_lcd.Character_LCD_I2C(display_bus, lcd_columns, lcd_rows)

#lcd = character_lcd.Character_LCD_I2C(i2c_lcd, lcd_columns, lcd_rows, address=0x27)

# Turn backlight on
#lcd.backlight = True
# Print a two line message
lcd.message = "Hello"
#Wait 5s
time.sleep(5)
lcd.clear()