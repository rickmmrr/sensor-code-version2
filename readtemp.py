# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

# -*- coding: utf-8 -*-

import time
import board
# for temp
import adafruit_ahtx0

# Create sensor object, communicating over the board's default I2C bus
i2c = board.I2C()  # uses board.SCL and board.SDA

total_reads = 15
index = 0
temparray = [0] * total_reads
humidityarray = [0] * total_reads

while True:
    sensor = adafruit_ahtx0.AHTx0(i2c)
    if index == total_reads:

        totaltemp = sum(temparray) / total_reads
        totalhumidity = sum(humidityarray) / total_reads

        #set the current temperature setting
        #******************************************
        with open("/home/pi/python/test/set_temp.txt", "w") as outfile:
            outfile.write("%0.0f " % totaltemp )
        with open("/home/pi/python/test/set_humidity.txt", "w") as outfile:
            outfile.write("%0.0f " % totalhumidity )
        #********************************************

        print("\nTemperature: %0.0f " % totaltemp )
        print("Humidity: %0.0f " % totalhumidity)


        index = 0
    else:
        f = (sensor.temperature * 1.8) + 32
        u = sensor.relative_humidity
        temparray[index] = f
        humidityarray[index] = u
        index = index + 1


    time.sleep(.250)

