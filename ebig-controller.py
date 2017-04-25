from myutils.listener import serial_listen


def influx_handler(message):
    print "Store to Influx: %s" % message


serial_listen(port='/dev/cu.wchusbserial1420', handler=influx_handler)
