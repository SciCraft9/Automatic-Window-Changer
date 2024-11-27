import serial
import os

# replace with the name of the serial port the Arduino is connected to
ser = serial.Serial('COM9', 9600) 

door_state = False  # assume door is closed at startup

while True:
    if ser.in_waiting > 0:
        line = ser.readline().decode().rstrip()
        if line == 'door opened' and not door_state:
            door_state = True
            # replace with the command to change the window when the door is opened
            os.system('start microsoft-edge:https://www.youtube.com/watch?v=LpsYlYM-o0Y&t=2624s')
        elif line == 'door closed' and door_state:
            door_state = False
            # replace with the command to change the window when the door is closed
            