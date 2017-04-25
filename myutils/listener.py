import serial

from myutils.Message import Message


## Mysensors serial protocol message structure:
# Mysensors serial pattern from: https://www.mysensors.org/download/serial_api_20#examples
# node-id;child-sensor-id;message-type;ack;sub-type;payload\n
##

def default_handler(message):
    print message


def serial_listen(port, speed=115200, handler=default_handler):
    print "Listening to port: %s" % port
    ser = serial.Serial(port, speed)
    while True:
        try:
            line = ser.readline()
            print line
            message = Message(line)
            handler(message)
        except Exception, e:
            print e
