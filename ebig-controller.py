from influxdb import InfluxDBClient

from myutils.listener import serial_listen

ROOM_LOCATIONS = {
    1: '',
    2: '',
    50: 'Uwe-NO-0.01',
    51: 'Uwe-NO-0.02'
}

def influx_handler(message):
    print "Message: %s" % message
    if (message.node_id in ROOM_LOCATIONS.keys()):
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
                'roomLocation': ROOM_LOCATIONS.get(message.node_id)
            }
        }

        if (message.sub_type == 'V_TEMP'):
            datapackage['fields'] = {'tempMiddle': float(message.payload)}
            series.append(datapackage)
            client = InfluxDBClient('145.74.104.50', 8086, '', '', 'ebig')
            client.write_points(series)




serial_listen(port='/dev/cu.wchusbserial1420', handler=influx_handler)
