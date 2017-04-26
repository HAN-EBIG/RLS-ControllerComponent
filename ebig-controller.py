from influxdb import InfluxDBClient

from myutils.ebig_constants import decode_room_location
from myutils.ebig_constants import location_exists
from myutils.listener import serial_listen


def influx_handler(message):
    print("Message: %s" % message)
    if (location_exists(message.node_id)):
        series = []
        # datapackage = {
        #     'measurement':'room',
        #     'tags': {
        #         'roomLocation': 'Tech-No-422'
        #     },
        #     'fields':{
        #         'doorMainOpen':int(message.payload)
        #     }
        # }

        datapackage = {
            'measurement': 'room',
            'tags': {
                'roomLocation': decode_room_location(message.node_id)
            }
        }

        if (message.sub_type == 'V_TEMP'):
            datapackage['fields'] = {'tempMiddle': float(message.payload)}
            series.append(datapackage)
            client = InfluxDBClient('145.74.104.50', 8086, '', '', 'ebig')
            client.write_points(series)




serial_listen(port='/dev/cu.wchusbserial1420', handler=influx_handler)
