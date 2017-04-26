##
# Constants for Ebig sensor-node to room mapping and sensor types
#
# Room locations follow schema: Building-wing-roomNo
# wing can be: NO (if building has no wings), or A,B,C and the like
# roomNo follows the room naming scheme of the building, for instance 1.01 for room 1 on the first floor
#
##
ROOM_LOCATIONS = {
    1: '',
    2: '',
    50: 'Uwe-NO-0.01',  # Location-ID for Uwe's home office
    105: 'Uwe-NO-0.02'  # Location-ID for Uwe's ground floor
}

SENSOR_MAPPING = {
    1: ('TEMP_MIDDLE', 'V_TEMP'),  # Temperature measured in the middle of a room; sub_type=V_TEMP
    2: ('TEMP_WINDOW', 'V_TEMP'),  # Temperature measured on the windows; sub_type=V_TEMP
    3: ('DOOR_MAIN_OPEN', 'V_TRIPPED'),  # Boolean shows if door to main floor is open; sub_type=V_TRIPPED
    4: ('DOOR_LEFT_OPEN', 'V_TRIPPED'),  # Boolean shows if door left (seen from main door) is open; sub_type=V_TRIPPED
    5: ('DOOR_RIGHT_OPEN', 'V_TRIPPED'),
# Boolean shows if door right (seen from main door) is open; sub_type=V_TRIPPED
    6: ('WINDOW_ONE_OPEN', 'V_TRIPPED'),  # Boolean shows if window is open; sub_type=V_TRIPPED
    7: ('WINDOW_TWO_OPEN', 'V_TRIPPED'),  # Boolean shows if window is open; sub_type=V_TRIPPED
    8: ('WINDOW_THREE_OPEN', 'V_TRIPPED'),  # Boolean shows if window is open; sub_type=V_TRIPPED
    9: ('LIGHT_INTENSITY', 'V_LIGHT_LEVEL'),  # Light-intensity measured in the middle of a room; sub_type=V_LIGHT_LEVEL
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
