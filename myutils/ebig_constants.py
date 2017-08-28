##
# Constants for Ebig sensor-node to room mapping and sensor types
#
# Measured values as stored in influx measurement "room"
##


# Room locations follow schema: Building-wing-roomNo
# wing can be: NO (if building has no wings), or A,B,C and the like
# roomNo follows the room naming scheme of the building, for instance 1.01 for room 1 on the first floor
# room locations are used as tags in Influx measurement
##
ROOM_LOCATIONS = {
    1: '',
    2: '',
    10: 'Tech-NO-4.22',  # Location-ID for room in the Technovium in Njmegen
    11: 'R26-D-1.04',  # Door node D1.04
    12: 'R26-D-1.04',  # Ceiling node D1.04
    13: 'R26-D-1.04',  # Left radiator node D1.04: WINDOW_ONE
    14: 'R26-D-1.04',  # Right radiator node D1.04
    50: 'Uwe-NO-0.01',  # Location-ID for Uwe's home office
    105: 'Uwe-NO-0.02',  # Location-ID for Uwe's ground floor
    106: 'Jorn-NO-0.01',  # Location-ID for Jorn's ground floor
    107: 'Ties-NO-0.01',  # Location-ID for Ties' ground floor
}

# Sensor ID mapped against field name in Influx, and mysensors sub-type
SENSOR_MAPPING = {
    1: ('TEMP_MIDDLE', 'V_TEMP'),  # Temperature measured in the middle of a room
    2: ('TEMP_WINDOW', 'V_TEMP'),  # Temperature measured on the windows
    5: ('DOOR_MAIN_OPEN', 'V_TRIPPED'),  # Shows if door to main floor is open
    6: ('DOOR_MAIN_TEMP', 'V_TEMP'),  # Shows if door to main floor is open
    7: ('DOOR_LEFT_OPEN', 'V_TRIPPED'),  # Shows if door left (seen from main door) is open
    8: ('DOOR_LEFT_TEMP', 'V_TEMP'),  # Shows if door to main floor is open
    9: ('DOOR_RIGHT_OPEN', 'V_TRIPPED'),  # Shows if door right (seen from main door) is open
    10: ('DOOR_RIGHT_TEMP', 'V_TEMP'),  # Shows if door to main floor is open
    11: ('WINDOW_ONE_OPEN', 'V_TRIPPED'),  # Shows if window is open
    12: ('WINDOW_TWO_OPEN', 'V_TRIPPED'),  # Shows if window is open
    13: ('WINDOW_THREE_OPEN', 'V_TRIPPED'),  # Shows if window is open
    14: ('WINDOW_FOUR_OPEN', 'V_TRIPPED'),  # Shows if window is open
    15: ('WINDOW_FIVE_OPEN', 'V_TRIPPED'),  # Shows if window is open
    20: ('LIGHT_INTENSITY_ROOM', 'V_LIGHT_LEVEL'),  # Light-intensity measured in the middle of a room
    21: ('LIGHT_INTENSITY_BEAMER', 'V_LIGHT_LEVEL'),  # Light-intensity measured in the middle of a room
    25: ('TEMP_RAD1_IN', 'V_TEMP'),  # Temperature measured on the input pipe of a radiator
    26: ('TEMP_RAD1_OUT', 'V_TEMP'),  # Temperature measured on the output pipe of a radiator
    27: ('TEMP_RAD2_IN', 'V_TEMP'),  # Temperature measured on the input pipe of a radiator
    28: ('TEMP_RAD2_OUT', 'V_TEMP'),  # Temperature measured on the output pipe of a radiator
    29: ('TEMP_RAD3_IN', 'V_TEMP'),  # Temperature measured on the input pipe of a radiator
    30: ('TEMP_RAD3_OUT', 'V_TEMP'),  # Temperature measured on the output pipe of a radiator
    35: ('HUMIDITY', 'V_HUM'),  # Humidity measured in the middle of the room
    200: ('POWER_W', 'V_WATT'),  # Actual electricity power delivered (+P) in kW
    201: ('POWER_KWH', 'V_KWH'),  # Meter Reading electricity delivered to client in kWh
    255: ('BATTERY_LEVEL', 'I_BATTERY_LEVEL'),  # Battery-level
}


def decode_room_location(room_location):
    return ROOM_LOCATIONS.get(room_location)


def location_exists(room_location):
    return room_location in ROOM_LOCATIONS.keys()


def decode_sensor(sensor_id):
    return SENSOR_MAPPING.get(sensor_id)[0]


def get_expected_subtype(sensor_id):
    return SENSOR_MAPPING.get(sensor_id)[1]


def sensor_exists(sensor_id):
    return sensor_id in SENSOR_MAPPING.keys()
