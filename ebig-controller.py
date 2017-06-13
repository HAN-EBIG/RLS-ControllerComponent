from influxdb import InfluxDBClient

from myutils.ebig_constants import decode_room_location
from myutils.ebig_constants import decode_sensor
from myutils.ebig_constants import get_expected_subtype
from myutils.ebig_constants import location_exists
from myutils.ebig_constants import sensor_exists
from myutils.listener import serial_listen


def influx_handler(message):
    print("Message: %s" % message)

    if (location_exists(message.node_id) and sensor_exists(message.child_sensor_id)):
        series = []
        base_datapackage = {
            'measurement': 'room',
            'tags': {
                'roomLocation': decode_room_location(message.node_id),
                'nodeId': message.node_id
            }
        }

        if (message.sub_type != get_expected_subtype(message.child_sensor_id)):
            return

        ebig_sensor = decode_sensor(message.child_sensor_id)

        if (message.sub_type == 'V_TEMP'):
            base_datapackage['fields'] = {ebig_sensor: float(message.payload)}

        elif (message.sub_type == 'V_TRIPPED'):
            base_datapackage['fields'] = {ebig_sensor: bool(message.payload)}

        elif (message.sub_type == 'V_LIGHT_LEVEL'):
            base_datapackage['fields'] = {ebig_sensor: int(message.payload)}

        elif (message.sub_type == 'V_HUM'):
            base_datapackage['fields'] = {ebig_sensor: float(message.payload)}

        elif (message.sub_type == 'V_WATT'):
            base_datapackage['fields'] = {ebig_sensor: float(message.payload)}

        elif (message.sub_type == 'V_KWH'):
            base_datapackage['fields'] = {ebig_sensor: float(message.payload)}

        elif (message.sub_type == 'I_BATTERY_LEVEL'):
            base_datapackage['fields'] = {ebig_sensor: float(message.payload)}
            
        series.append(base_datapackage)
        client = InfluxDBClient('145.74.104.50', 8086, 'sensorcontroller', '@sensorpass@', 'ebig')
        client.write_points(series)


# serial_listen(port='/dev/cu.wchusbserial1420', handler=influx_handler)
serial_listen(port='/dev/ttyUSB0', handler=influx_handler)  # USB serial port on raspberry pi
