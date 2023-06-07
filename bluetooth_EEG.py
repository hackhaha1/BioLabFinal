import serial
import csv
import keyboard
import time
from time import sleep

ser = serial.Serial()
ser.baudrate = 9600
ser.port = 'COM8'

ser.open()

# startflag = False
# endflag = False

counter = 0

print("bluetooth connected")

with open('EEG_0519_6.csv', 'w', newline='') as file:
    writer = csv.writer(file)

# while (not startflag and not endflag):
#    if (keyboard.is_pressed('e')):
#        startflag = True
while not keyboard.is_pressed('s'):
    if (counter < 600):
        #   print(ser.isOpen())
        h1 = ser.read().decode("utf-8")
        f1 = ord(h1)
        print(f1)

        data = []
        data.append(f1)
        with open('EEG_0519_6.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(data)
            
        counter += 1

    else:
        h1 = ser.read().decode("utf-8")
        if (keyboard.is_pressed('a')):
            counter = 0
