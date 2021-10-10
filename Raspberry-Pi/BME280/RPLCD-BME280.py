#!/usr/bin/python3


from RPLCD import i2c
from time import sleep
import time
import board
from adafruit_bme280 import basic as adafruit_bme280

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

# Create sensor object, using the board's default I2C bus.
i2c = board.I2C()  # uses board.SCL and board.SDA
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c, address=0x76)

# change this to match the location's pressure (hPa) at sea level
bme280.sea_level_pressure = 1010.0

while True:

    # Define functions to allow RPLCD to output sensor data
    def read_temp():
        tempC = bme280.temperature
        temp = tempC * 9/5.0 + 32
        temp = str(round(temp, 2))
        temp = str(temp)
        return temp

    def read_humidity():
        relative_humidity = bme280.relative_humidity
        humidity = str(round(relative_humidity, 2))
        humidity = str(humidity)
        return humidity
    
    def read_baro_pressure():
        pressure = bme280.pressure
        pressure = str(round(pressure, 2))
        pressure = str(pressure)
        return pressure


    # Print output to terminal
    print("Temp: " + read_temp() + "F")
    print("Humidity: " + read_humidity() + "%")
    print("Pressure: " + read_baro_pressure() + "hPa")

    # Print output to LCD
    lcd.write_string("Temp: " + read_temp() + "F")
    lcd.crlf()
    lcd.write_string("Humidity: " + read_humidity() + "%")
    lcd.crlf()
    lcd.write_string("Pressure: " + read_baro_pressure() + "hPa")
    sleep(30)
    lcd.clear()
    sleep(0.5)
    #lcd.close(clear=True)