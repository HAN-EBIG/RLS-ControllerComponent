# https://www.mysensors.org/download/serial_api_14

MESSAGE_TYPES = {

    # Sent by a node when they present attached sensors. This is usually done
    # in setup() at startup.
    0: 'M_PRESENTATION',

    # This message is sent from or to a sensor when a sensor value should be
    # updated
    1: 'M_SET',

    # Requests a variable value (usually from an actuator destined for controller).
    2: 'M_REQ',

    # This is a special internal message. See table below for the details
    3: 'M_INTERNAL',

    4: 'M_STREAM'  # Used for OTA firmware updates

    ### PRESENTATION
}

PRESENTATION = {
    0: 'S_DOOR',  # Door and window sensors
    1: 'S_MOTION',  # Motion sensors
    2: 'S_SMOKE',  # Smoke sensor
    3: 'S_LIGHT',  # Light Actuator (on/off)
    4: 'S_DIMMER',  # Dimmable device of some kind
    5: 'S_COVER',  # Window covers or shades
    6: 'S_TEMP',  # Temperature sensor
    7: 'S_HUM',  # Humidity sensor
    8: 'S_BARO',  # Barometer sensor (Pressure)
    9: 'S_WIND',  # Wind sensor
    10: 'S_RAIN',  # Rain sensor
    11: 'S_UV',  # UV sensor
    12: 'S_WEIGHT',  # Weight sensor for scales etc.
    13: 'S_POWER',  # Power measuring device ,like power meters
    14: 'S_HEATER',  # Heater device
    15: 'S_DISTANCE',  # Distance sensor
    16: 'S_LIGHT_LEVEL',  # Light sensor
    17: 'S_ARDUINO_NODE',  # Arduino node device
    18: 'S_ARDUINO_RELAY',  # Arduino repeating node device
    19: 'S_LOCK',  # Lock device
    20: 'S_IR',  # Ir sender/receiver device
    21: 'S_WATER',  # Water meter
    22: 'S_AIR_QUALITY',  # Air quality sensor e.g. MQ-2
    23: 'S_CUSTOM',  # Use this for custom sensors where no other fits.
    24: 'S_DUST',  # Dust level sensor
    25: 'S_SCENE_CONTROLLER',  # Scene controller device':

}

SET_REQ = {
    # ,## set, req
    0: 'V_TEMP',  # Temperature
    1: 'V_HUM',  # Humidity
    2: 'V_LIGHT',  # Light status. 0 = off 1 = on
    3: 'V_DIMMER',  # Dimmer value. 0-100%
    4: 'V_PRESSURE',  # Atmospheric Pressure
    # Whether forecast. One of "stable", "sunny", "cloudy", "unstable",
    # "thunderstorm" or "unknown"
    5: 'V_FORECAST',
    6: 'V_RAIN',  # Amount of rain
    7: 'V_RAINRATE',  # Rate of rain
    8: 'V_WIND',  # Windspeed
    9: 'V_GUST',  # Gust
    10: 'V_DIRECTION',  # Wind direction
    11: 'V_UV',  # UV light level
    12: 'V_WEIGHT',  # Weight (for scales etc)
    13: 'V_DISTANCE',  # Distance
    14: 'V_IMPEDANCE',  # Impedance value
    15: 'V_ARMED',  # Armed status of a security sensor. 1=Armed, 0=Bypassed
    16: 'V_TRIPPED',  # Tripped status of a security sensor. 1=Tripped, 0=Untripped
    17: 'V_WATT',  # Watt value for power meters
    18: 'V_KWH',  # Accumulated number of KWH for a power meter
    19: 'V_SCENE_ON',  # Turn on a scene
    20: 'V_SCENE_OFF',  # Turn of a scene
    # Mode of header. One of "Off", "HeatOn", "CoolOn", or "AutoChangeOver"
    21: 'V_HEATER',
    22: 'V_HEATER_SW',  # Heater switch power. 1=On, 0=Off
    23: 'V_LIGHT_LEVEL',  # Light level. 0-100%
    24: 'V_VAR1',  # Custom value
    25: 'V_VAR2',  # Custom value
    26: 'V_VAR3',  # Custom value
    27: 'V_VAR4',  # Custom value
    28: 'V_VAR5',  # Custom value
    29: 'V_UP',  # Window covering. Up.
    30: 'V_DOWN',  # Window covering. Down.
    31: 'V_STOP',  # Window covering. Stop.
    32: 'V_IR_SEND',  # Send out an IR-command
    33: 'V_IR_RECEIVE',  # This message contains a received IR-command
    34: 'V_FLOW',  # Flow of water (in meter)
    35: 'V_VOLUME',  # Water volume
    36: 'V_LOCK_STATUS',  # Set or get lock status. 1=Locked, 0=Unlocked
    37: 'V_DUST_LEVEL',  # Dust level
    38: 'V_VOLTAGE',  # Voltage level
    39: 'V_CURRENT',  # Current level
}

INTERNAL = {
    0: 'I_BATTERY_LEVEL',  # Use this to report the battery level (in percent 0-100).
    1: 'I_TIME',
    # Sensors can request the current time from the Controller using this message. The time will be reported as the seconds since 1970
    2: 'I_VERSION',  # Used to request gateway version from controller.
    3: 'I_ID_REQUEST',  # Use this to request a unique node id from the controller.
    4: 'I_ID_RESPONSE',  # Id response back to sensor. Payload contains sensor id.
    5: 'I_INCLUSION_MODE',  # Start/stop inclusion mode of the Controller (1=start, 0=stop).
    6: 'I_CONFIG',  # Config request from node. Reply with (M)etric or (I)mperal back to sensor.
    7: 'I_FIND_PARENT',
    # When a sensor starts up, it broadcast a search request to all neighbor nodes. They reply with a   'I_FIND_PARENT_RESPONSE':.
    8: 'I_FIND_PARENT_RESPONSE',  # Reply message type to   'I_FIND_PARENT': request, #.
    9: 'I_LOG_MESSAGE',  # Sent by the gateway to the Controller to trace-log a message
    10: 'I_CHILDREN',
    # A message that can be used to transfer child sensors (from EEPROM routing table) of a repeating node.
    11: 'I_SKETCH_NAME',  # Optional sketch name that can be used to identify sensor in the Controller GUI
    12: 'I_SKETCH_VERSION',
    # Optional sketch version that can be reported to keep track of the version of sensor in the Controller GUI.
    13: 'I_REBOOT',  # Used by OTA firmware updates. Request for node to reboot.
    14: 'I_GATEWAY_READY',  # Send by gateway to controller when startup is complete.
}


def decode_message_type(message_type):
    return MESSAGE_TYPES.get(message_type)


def decode_sub_type(message_type, sub_type):
    if message_type == 'M_PRESENTATION':
        lookup_dict = PRESENTATION
    elif message_type in ['M_SET', 'M_REQ']:
        lookup_dict = SET_REQ
    elif message_type == 'M_INTERNAL':
        lookup_dict = INTERNAL
    return lookup_dict.get(sub_type)


def test_decode_message_type():
    assert decode_message_type(0) == 'M_PRESENTATION'
    assert decode_message_type(2) == "M_REQ"


def test_decode_sub_type():
    assert decode_sub_type('M_SET', 38) == 'V_VOLTAGE'
    assert decode_sub_type('M_PRESENTATION', 19) == "S_LOCK"
