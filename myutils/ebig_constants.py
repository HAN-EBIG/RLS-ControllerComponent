ROOM_LOCATIONS = {
    1: '',
    2: '',
    50: 'Uwe-NO-0.01',
    51: 'Uwe-NO-0.02'
}


def decode_room_location(room_location):
    return ROOM_LOCATIONS.get(room_location)


def location_exists(room_location):
    return room_location in ROOM_LOCATIONS.keys()
