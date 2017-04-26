## Mysensors serial protocol message structure:
# Mysensors serial pattern from: https://www.mysensors.org/download/serial_api_20#examples
# node-id;child-sensor-id;message-type;ack;sub-type;payload\n
##
import serial

from myutils.message import Message


def default_handler(message):
    print(message)


def serial_listen(port, speed=115200, handler=default_handler):
    print("Listening to port: %s" % port)
    ser = serial.Serial(port, speed)
    while True:
        try:
            line = ser.readline()
            print(line)
            message = Message(line.decode('utf8'))
            handler(message)
        except Exception as e:
            print(e)
