import board
import adafruit_thermistor

thermistor = adafruit_thermistor.Thermistor(board.GP26, 10000.0, 10000.0, 25.0, 3950.0, high_side=False)

NTCtempC = thermistor.temperature
NTCtempF = NTCtempC * 9/5.0 + 32

print(NTCtempF)